#!/usr/bin/env bash
#
# air_sync.sh — keep the AIR_review public API snapshot in sync with GitHub.
#
# Runs on the server (via systemd timer or cron). On each run it:
#   1. git fetch the tracked branch
#   2. compares local HEAD vs remote HEAD  -> exits early if unchanged
#   3. git reset --hard to the remote commit (deploy clone, no local edits)
#   4. regenerates the snapshot via generate_air_api_snapshot.py
#   5. atomically publishes it into the live snapshot dir the API reads
#
# It never contacts GitHub at API request time; this is the only thing that
# talks to GitHub, on a schedule. Safe to run frequently (a no-op fetch is cheap).
#
# Configuration via environment variables (with sensible defaults):
#   AIR_REPO_DIR     path to the server-side AIR_review checkout
#   AIR_BRANCH       branch to track                      (default: main)
#   AIR_SNAPSHOT_DIR live dir the Django API serves from
#                    (default: /var/www/scholarsrepublic/air_api_snapshot)
#   AIR_BASE_URL     public base URL for api_url fields   (default: https://scholarsrepublic.org)
#   AIR_PYTHON       python interpreter                   (default: python3)
#   AIR_LOG          log file                             (default: $AIR_REPO_DIR/air_sync.log)
#   AIR_FORCE        set to 1 to rebuild even with no change
#
# Exit codes: 0 = up to date or republished; non-zero = error.

set -euo pipefail

AIR_REPO_DIR="${AIR_REPO_DIR:-/var/www/scholarsrepublic/AIR_review}"
AIR_BRANCH="${AIR_BRANCH:-main}"
AIR_SNAPSHOT_DIR="${AIR_SNAPSHOT_DIR:-/var/www/scholarsrepublic/air_api_snapshot}"
AIR_BASE_URL="${AIR_BASE_URL:-https://scholarsrepublic.org}"
AIR_PYTHON="${AIR_PYTHON:-python3}"
AIR_LOG="${AIR_LOG:-${AIR_REPO_DIR}/air_sync.log}"
AIR_FORCE="${AIR_FORCE:-0}"

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
GENERATOR="${SCRIPT_DIR}/generate_air_api_snapshot.py"

log() { printf '%s %s\n' "$(date -u +%Y-%m-%dT%H:%M:%SZ)" "$*" | tee -a "$AIR_LOG"; }

# Prevent overlapping runs (timer + manual). flock if available, else lockdir.
LOCK="/tmp/air_sync.lock"
if command -v flock >/dev/null 2>&1; then
  exec 9>"$LOCK"
  if ! flock -n 9; then
    log "another air_sync is running; exiting"
    exit 0
  fi
fi

[ -d "$AIR_REPO_DIR/.git" ] || { log "ERROR: $AIR_REPO_DIR is not a git checkout"; exit 1; }
[ -f "$GENERATOR" ] || { log "ERROR: generator not found at $GENERATOR"; exit 1; }

cd "$AIR_REPO_DIR"

# Never block on a credential prompt; abort a stalled fetch instead of hanging
# forever (a hang would hold the lock and wedge every later run).
export GIT_TERMINAL_PROMPT=0
GIT_FETCH_TIMEOUT="${GIT_FETCH_TIMEOUT:-60}"

log "fetching origin/$AIR_BRANCH ..."
if ! timeout -k 10s "${GIT_FETCH_TIMEOUT}" git \
      -c http.lowSpeedLimit=1000 -c http.lowSpeedTime=20 \
      fetch --quiet --prune origin "$AIR_BRANCH"; then
  log "WARNING: git fetch failed/timed out; keeping existing snapshot, will retry next run"
  exit 0
fi

LOCAL="$(git rev-parse HEAD)"
REMOTE="$(git rev-parse "origin/${AIR_BRANCH}")"

# Commit currently reflected in the published snapshot (self-healing guard:
# rebuild if it drifts from HEAD even when the remote hasn't moved, e.g. if a
# commit was authored on this clone).
PUBLISHED=""
if [ -f "${AIR_SNAPSHOT_DIR}/health.json" ]; then
  PUBLISHED="$(grep -oE '[0-9a-f]{40}' "${AIR_SNAPSHOT_DIR}/health.json" | head -1)"
fi

if [ "$LOCAL" = "$REMOTE" ] && [ "$LOCAL" = "$PUBLISHED" ] && [ "$AIR_FORCE" != "1" ]; then
  log "no change (HEAD=$LOCAL, published=$PUBLISHED); nothing to do"
  exit 0
fi

log "rebuild needed (HEAD=$LOCAL remote=$REMOTE published=${PUBLISHED:-none}); updating working tree"
git checkout --quiet "$AIR_BRANCH" 2>/dev/null || git checkout --quiet -B "$AIR_BRANCH" "origin/${AIR_BRANCH}"
git reset --hard --quiet "origin/${AIR_BRANCH}"   # deploy clone: discard nothing of value

# Build snapshot into a staging dir inside the repo, then publish atomically.
STAGING="${AIR_REPO_DIR}/air_api_snapshot"
log "regenerating snapshot ..."
"$AIR_PYTHON" "$GENERATOR" --out "$STAGING" --base-url "$AIR_BASE_URL"

# Publish: rsync staging -> live (in-place, --delete removes stale files).
mkdir -p "$AIR_SNAPSHOT_DIR"
if command -v rsync >/dev/null 2>&1; then
  rsync -a --delete "${STAGING}/" "${AIR_SNAPSHOT_DIR}/"
else
  # Fallback without rsync: swap directories (brief window).
  rm -rf "${AIR_SNAPSHOT_DIR}.old"
  [ -d "$AIR_SNAPSHOT_DIR" ] && mv "$AIR_SNAPSHOT_DIR" "${AIR_SNAPSHOT_DIR}.old"
  cp -a "$STAGING" "$AIR_SNAPSHOT_DIR"
  rm -rf "${AIR_SNAPSHOT_DIR}.old"
fi

NEW_COMMIT="$(git rev-parse HEAD)"
log "published snapshot for commit $NEW_COMMIT to $AIR_SNAPSHOT_DIR"
log "done"
