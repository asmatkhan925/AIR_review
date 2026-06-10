# AIR_review Public Snapshot API

A public, cache-resistant API that lets any external assistant (e.g. ChatGPT)
read the **latest** state of the `AIR_review` repository without hitting
GitHub's stale `raw.githubusercontent.com` cache.

- **Base URL:** `https://scholarsrepublic.org/api/air/`
- **Repository:** `asmatkhan925/AIR_review`
- **No login, cookies, CAPTCHA, or JS rendering. Plain JSON / CSV / Markdown / BibTeX / text.**

---

## 1. Purpose

ChatGPT's browser cannot reliably read fresh GitHub raw files — it sees cached
matrices and cache-miss errors. This API solves that by serving a **generated
local snapshot** of an allowlist of project files from `scholarsrepublic.org`,
with aggressive no-store cache headers and integrity metadata (commit hash,
SHA-256, row/column counts, validations).

## 2. Architecture

```
AIR_review repo (local)                    scholarsrepublic.org server
┌───────────────────────────┐             ┌──────────────────────────────────┐
│ scripts/                   │             │ nginx  /api/  ──► Django :8000     │
│  generate_air_api_snapshot │  upload     │   apps/air_review/  (read-only)    │
│        │                   │  rsync /    │        │                           │
│        ▼                   │  scp        │        ▼                           │
│  air_api_snapshot/         │ ──────────► │  AIR_SNAPSHOT_DIR/                 │
│   manifest.json            │             │   manifest.json, latest.json,      │
│   latest.json              │             │   health.json, files/...           │
│   health.json              │             │                                    │
│   files/<mirrored paths>   │             │  GET /api/air/* serves this only   │
└───────────────────────────┘             └──────────────────────────────────┘
```

- The generator runs **inside the AIR_review repo**, reads the current git
  commit, hashes/validates allowlisted files, and writes `air_api_snapshot/`.
- You upload that folder to the server's `AIR_SNAPSHOT_DIR`.
- A small Django app (`apps.air_review`) serves the snapshot. **It never calls
  GitHub at request time**, so the API works even if GitHub is down.

## 3. Endpoints

| Method | Path | Returns |
|--------|------|---------|
| GET | `/api/air/health` | `{status, service, commit, generated_at_utc}` |
| GET | `/api/air/latest` | Compact state + key file URLs + `chatgpt_verification_targets` |
| GET | `/api/air/manifest` | Full `manifest.json` (per-file hashes, counts, validations) |
| GET | `/api/air/file?path=<allowlisted-path>` | Raw file content |

`OPTIONS` is handled on every endpoint (CORS preflight, `204`). Both
slash and non-slash forms resolve with **no redirect**.

> **Note on `&commit=`:** the API serves a single live snapshot, so a
> `commit` query parameter is accepted but ignored — the served bytes are
> always the latest generated commit, which is reported in `X-AIR-Commit` and
> in `manifest.json`. Compare that commit to verify freshness.

### Example `/api/air/latest`

```json
{
  "project": "AIR_review",
  "repository": "asmatkhan925/AIR_review",
  "commit": "<current commit>",
  "branch": "main",
  "generated_at_utc": "2026-06-10T12:00:00Z",
  "frozen_blocks": ["A", "B", "C", "D", "E", "F"],
  "status": "ok",
  "manifest_url": "https://scholarsrepublic.org/api/air/manifest",
  "key_files": {
    "seed_paper_map": "https://scholarsrepublic.org/api/air/file?path=05_synthesis_matrices/seed_paper_map.csv",
    "evaluation_robustness_matrix": "https://scholarsrepublic.org/api/air/file?path=05_synthesis_matrices/evaluation_robustness_matrix.csv",
    "evidence_to_claim_matrix": "https://scholarsrepublic.org/api/air/file?path=05_synthesis_matrices/evidence_to_claim_matrix.csv",
    "references_bib": "https://scholarsrepublic.org/api/air/file?path=03_references/references.bib"
  },
  "chatgpt_verification_targets": {
    "must_find_in_seed_map": ["BF24", "BF25"],
    "must_find_in_evidence_to_claim_matrix": ["C-F1", "C-F8"],
    "must_find_in_evaluation_robustness_matrix": ["BF24", "BF25"],
    "current_commit": "<current commit>"
  }
}
```

## 4. Allowlisted files

Only these exact relative paths are ever served (404 if absent, 403 if not on
this list). `LATEST_REPO_STATE.md` and `repo_manifest.json` are optional.

```
README.md
LATEST_REPO_STATE.md
repo_manifest.json
00_project_management/decision_log.md
01_scope_and_planning/research_questions.md
01_scope_and_planning/review_methodology.md
02_literature_search/search_log.csv
03_references/citation_verification_log.csv
03_references/references.bib
05_synthesis_matrices/seed_paper_map.csv
05_synthesis_matrices/dataset_benchmark_matrix.csv
05_synthesis_matrices/foundation_model_matrix.csv
05_synthesis_matrices/data_centric_strategy_matrix.csv
05_synthesis_matrices/adaptation_strategy_matrix.csv
05_synthesis_matrices/pseudo_labeling_kd_matrix.csv
05_synthesis_matrices/evaluation_robustness_matrix.csv
05_synthesis_matrices/evidence_to_claim_matrix.csv
06_review_outline/section_argument_map.md
07_draft_sections/01_introduction.md
12_manuscript/main_manuscript.md
```

The allowlist lives in **two places that must stay in sync**:
- `scripts/generate_air_api_snapshot.py` → `ALLOWLIST` (decides what is copied)
- server `apps/air_review/allowlist.py` → `ALLOWLIST` (decides what is served)

## 5. Cache-control policy

Every response sends:

```
Cache-Control: no-store, no-cache, must-revalidate, max-age=0, s-maxage=0
Pragma: no-cache
Expires: 0
X-AIR-Commit: <commit>
X-AIR-Generated-At: <timestamp>
X-AIR-Source: scholarsrepublic-api
Access-Control-Allow-Origin: *
Access-Control-Allow-Methods: GET, OPTIONS
Access-Control-Allow-Headers: Content-Type
```

## 6. Security policy

- **Strict allowlist** — no arbitrary filesystem reads; exact path match only.
- Rejects `..`, absolute paths, `\` backslashes, null bytes, and hidden
  (`.`-prefixed) segments; resolved path must stay inside `AIR_SNAPSHOT_DIR/files`.
- Serves **only** the generated snapshot. `.env`, `.git`, `wp-config.php`,
  SSH keys, credentials, unrelated uploads, and server config are unreachable.
- Snapshot lives outside `media/`/`static/`, so nginx never serves it directly.
- Read-only `GET`/`OPTIONS`; `POST`/`PUT`/etc. return `405`.

## 7. Deployment steps

See `README_AIR_API_ADDITIONS.md` (in this bundle) for the file map. Summary:

**On the AIR_review repo (local):**
```bash
python scripts/generate_air_api_snapshot.py
# produces ./air_api_snapshot/
```

**Upload to the server (pick one):**
```bash
# rsync (recommended)
rsync -avz --delete air_api_snapshot/ \
  user@scholarsrepublic.org:/var/www/scholarsrepublic/air_api_snapshot/

# or scp
scp -r air_api_snapshot/* \
  user@scholarsrepublic.org:/var/www/scholarsrepublic/air_api_snapshot/
```

**On the server (one-time):** the Django app `apps.air_review` is already wired
into `INSTALLED_APPS` and `config/urls.py`. Set `AIR_SNAPSHOT_DIR` if you used a
non-default location, then reload:
```bash
sudo systemctl restart scholars-backend
```

No nginx change is required: `/api/` already proxies to Django. If a CDN/cache
sits in front, add a bypass rule for `/api/air/*` (see Troubleshooting).

## 7b. Automatic GitHub sync (keep the snapshot fresh)

`scripts/air_sync.sh` polls GitHub on a schedule and republishes the snapshot
**only when `main` actually moves** — so the API always reflects the latest
commit without any manual step. It is the *only* thing that talks to GitHub,
and it does so on a timer, never at API request time.

What it does each run: `git fetch` → compare local vs remote HEAD → if changed,
`git reset --hard origin/main` → regenerate snapshot → atomically publish into
`AIR_SNAPSHOT_DIR`. A no-op run is just a cheap fetch. An flock guard prevents
overlapping runs.

### One-time setup (server)

```bash
# 1. Put a deploy checkout where the timer expects it (full clone, not shallow):
sudo git clone https://github.com/asmatkhan925/AIR_review.git \
  /var/www/scholarsrepublic/AIR_review
sudo chown -R www-data:www-data /var/www/scholarsrepublic/AIR_review
chmod +x /var/www/scholarsrepublic/AIR_review/scripts/air_sync.sh

# 2. Install the systemd timer (units are in deploy/systemd/):
sudo cp /var/www/scholarsrepublic/AIR_review/deploy/systemd/air-sync.* /etc/systemd/system/
sudo systemctl daemon-reload
sudo systemctl enable --now air-sync.timer

# 3. Verify
systemctl list-timers air-sync.timer
sudo systemctl start air-sync.service   # force a run now
journalctl -u air-sync.service -n 50
```

The timer runs every 5 minutes (`OnUnitActiveSec=5min`); edit `air-sync.timer`
to change cadence. Adjust `User`/`Group` and the `Environment=` paths in
`air-sync.service` to match your deploy user and layout.

### Cron alternative (if you don't use systemd)

```cron
*/5 * * * * AIR_REPO_DIR=/var/www/scholarsrepublic/AIR_review \
  AIR_SNAPSHOT_DIR=/var/www/scholarsrepublic/air_api_snapshot \
  /var/www/scholarsrepublic/AIR_review/scripts/air_sync.sh >> /var/log/air_sync.log 2>&1
```

### Force a rebuild manually

```bash
AIR_FORCE=1 /var/www/scholarsrepublic/AIR_review/scripts/air_sync.sh
```

### Instant "on push" refresh — GitHub webhook (recommended)

`POST /api/air/refresh` triggers `air_sync.sh` the moment you push, so the
snapshot updates in seconds instead of waiting for the next poll. It is
**HMAC-verified** against GitHub's `X-Hub-Signature-256` header and only acts on
pushes to the tracked branch. The 1-minute timer stays on as a safety net.

**Server config** — set a shared secret and (re)start the backend:
```bash
# add to the backend environment (.env or systemd unit), then restart:
AIR_WEBHOOK_SECRET=<a-long-random-string>
AIR_SYNC_SCRIPT=/var/www/scholarsrepublic/AIR_review/scripts/air_sync.sh
AIR_BRANCH=main
# sudo systemctl restart scholars-backend
```
Until `AIR_WEBHOOK_SECRET` is set the endpoint is **disabled** (returns `503`).

**GitHub config** — repo → Settings → Webhooks → Add webhook:
- Payload URL: `https://scholarsrepublic.org/api/air/refresh`
- Content type: `application/json`
- Secret: the same `AIR_WEBHOOK_SECRET`
- Events: "Just the push event"

Behaviour:
| Condition | Response |
|---|---|
| valid signature, push to `main` | `202 {"status":"triggered"}` |
| `ping` event (GitHub's test) | `200 {"status":"pong"}` |
| push to another branch | `200 {"status":"ignored"}` |
| missing/wrong signature | `401 {"error":"invalid_signature"}` |
| secret not configured | `503 {"error":"webhook_disabled"}` |

The endpoint launches `air_sync.sh` detached; the script's `flock` guard means a
webhook firing and a timer tick at the same moment can't collide.

## 8. Validation commands

```bash
curl -i https://scholarsrepublic.org/api/air/health
curl -i https://scholarsrepublic.org/api/air/latest
curl -i https://scholarsrepublic.org/api/air/manifest
curl -i "https://scholarsrepublic.org/api/air/file?path=05_synthesis_matrices/evaluation_robustness_matrix.csv"
curl -i "https://scholarsrepublic.org/api/air/file?path=05_synthesis_matrices/evidence_to_claim_matrix.csv"
curl -i "https://scholarsrepublic.org/api/air/file?path=05_synthesis_matrices/seed_paper_map.csv"
curl -i "https://scholarsrepublic.org/api/air/file?path=../../wp-config.php"   # expect 400/403
```

Expected: 200 JSON for health/latest/manifest; 200 raw for allowlisted files;
400/403 for traversal; `no-store` cache headers everywhere; `X-AIR-Commit`
equal to the local `git rev-parse HEAD` at generation time.

## 9. Troubleshooting

- **503 `snapshot_unavailable`** — the bundle hasn't been uploaded to
  `AIR_SNAPSHOT_DIR` yet, or the path/permissions are wrong. Re-run the upload.
- **Stale commit** — re-run the generator and re-upload; `X-AIR-Commit` should
  match `git rev-parse HEAD`. The snapshot is a point-in-time copy.
- **CDN / Cloudflare caching** — create a cache rule to **bypass cache** for
  `/api/air/*`. With Cloudflare: a Cache Rule → "Bypass cache" for the path.
  Origin already sends `no-store`, so `respect existing headers` also works.
- **nginx micro-cache** (if you add one later) — add
  `location /api/air/ { proxy_no_cache 1; proxy_cache_bypass 1; ... }`.
- **403 on a file you expect** — the path is not on the allowlist, or it has a
  typo (paths are exact, case-sensitive, forward-slash).

## 10. How ChatGPT should use this API instead of GitHub raw URLs

1. `GET /api/air/latest` → read `commit` and `chatgpt_verification_targets`.
2. `GET /api/air/manifest` → per-file `sha256`, `rows`, `columns`, `validations`.
3. Fetch any file via `GET /api/air/file?path=<allowlisted-path>` (raw bytes).
4. Confirm freshness with the `X-AIR-Commit` header.

**Do not** use `raw.githubusercontent.com` — it is cached/stale. This API is the
source of truth for the latest repository state.
