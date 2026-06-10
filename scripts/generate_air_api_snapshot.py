#!/usr/bin/env python3
"""
generate_air_api_snapshot.py
============================

Generate a cache-resistant API snapshot of the AIR_review repository.

This script is meant to run **inside the AIR_review git repository**. It reads
only an allowlist of safe project files, computes integrity metadata
(sizes, SHA-256 hashes, line/row/column counts), runs project invariant
validations, and writes a self-contained snapshot bundle to ``air_api_snapshot/``.

That bundle is then uploaded to the scholarsrepublic.org server, where a small
Django app serves it as a public, no-cache API. Nothing here talks to GitHub,
so the API keeps working even if raw.githubusercontent.com is stale or down.

Usage
-----
    python scripts/generate_air_api_snapshot.py
    python scripts/generate_air_api_snapshot.py --out air_api_snapshot --base-url https://scholarsrepublic.org

Exit codes
----------
    0  snapshot generated (check ``status`` field for "ok" vs "degraded")
    1  fatal error (e.g. not a git repo, repo root not found)

The script never raises on a missing allowlisted file or a failed validation;
those are reported in the manifest so the snapshot is always produced.
"""

from __future__ import annotations

import argparse
import csv
import hashlib
import io
import json
import os
import re
import shutil
import subprocess
import sys
from datetime import datetime, timezone
from pathlib import Path

# --------------------------------------------------------------------------- #
# Configuration
# --------------------------------------------------------------------------- #

REPOSITORY = "asmatkhan925/AIR_review"
PROJECT = "AIR_review"
DEFAULT_BASE_URL = "https://scholarsrepublic.org"
FROZEN_BLOCKS = ["A", "B", "C", "D", "E", "F"]

# The single source of truth for what may be exposed. Order is preserved in
# the manifest. "if present" files are allowed to be missing without error.
ALLOWLIST = [
    "README.md",
    "LATEST_REPO_STATE.md",          # if present
    "repo_manifest.json",            # if present
    "00_project_management/decision_log.md",
    "01_scope_and_planning/research_questions.md",
    "01_scope_and_planning/review_methodology.md",
    "02_literature_search/search_log.csv",
    "03_references/citation_verification_log.csv",
    "03_references/references.bib",
    "05_synthesis_matrices/seed_paper_map.csv",
    "05_synthesis_matrices/dataset_benchmark_matrix.csv",
    "05_synthesis_matrices/foundation_model_matrix.csv",
    "05_synthesis_matrices/data_centric_strategy_matrix.csv",
    "05_synthesis_matrices/adaptation_strategy_matrix.csv",
    "05_synthesis_matrices/pseudo_labeling_kd_matrix.csv",
    "05_synthesis_matrices/evaluation_robustness_matrix.csv",
    "05_synthesis_matrices/evidence_to_claim_matrix.csv",
    "06_review_outline/section_argument_map.md",
    "07_draft_sections/01_introduction.md",
    "12_manuscript/main_manuscript.md",
]

# Key files surfaced in /latest for quick assistant access.
KEY_FILES = {
    "readme": "README.md",
    "decision_log": "00_project_management/decision_log.md",
    "seed_paper_map": "05_synthesis_matrices/seed_paper_map.csv",
    "evaluation_robustness_matrix": "05_synthesis_matrices/evaluation_robustness_matrix.csv",
    "evidence_to_claim_matrix": "05_synthesis_matrices/evidence_to_claim_matrix.csv",
    "references_bib": "03_references/references.bib",
}

SEED_MAP = "05_synthesis_matrices/seed_paper_map.csv"
EVIDENCE_MATRIX = "05_synthesis_matrices/evidence_to_claim_matrix.csv"
EVAL_ROBUSTNESS = "05_synthesis_matrices/evaluation_robustness_matrix.csv"
CITATION_LOG = "03_references/citation_verification_log.csv"
REFERENCES_BIB = "03_references/references.bib"

CF_CLAIMS = [f"C-F{i}" for i in range(1, 9)]  # C-F1 .. C-F8


# --------------------------------------------------------------------------- #
# Git helpers
# --------------------------------------------------------------------------- #

def _git(args, repo_root):
    try:
        out = subprocess.run(
            ["git", *args],
            cwd=str(repo_root),
            check=True,
            capture_output=True,
            text=True,
        )
        return out.stdout.strip()
    except (subprocess.CalledProcessError, FileNotFoundError):
        return ""


def find_repo_root(start: Path) -> Path:
    root = _git(["rev-parse", "--show-toplevel"], start)
    if root:
        return Path(root)
    # Fall back to walking up looking for a .git directory.
    cur = start.resolve()
    for parent in [cur, *cur.parents]:
        if (parent / ".git").exists():
            return parent
    return start.resolve()


# --------------------------------------------------------------------------- #
# File metrics
# --------------------------------------------------------------------------- #

def sha256_of(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()


def count_lines(data: bytes) -> int:
    if not data:
        return 0
    text = data.decode("utf-8", errors="replace")
    # Count logical lines: number of '\n' plus 1 if no trailing newline.
    n = text.count("\n")
    if not text.endswith("\n"):
        n += 1
    return n


def csv_stats(data: bytes):
    """Return (rows, columns, width_ok) for CSV bytes.

    rows  = data rows excluding header
    columns = number of columns in the header
    width_ok = every data row has the same column count as the header
    """
    text = data.decode("utf-8-sig", errors="replace")
    reader = csv.reader(io.StringIO(text))
    rows = list(reader)
    if not rows:
        return 0, 0, True
    header = rows[0]
    columns = len(header)
    data_rows = rows[1:]
    width_ok = all(len(r) == columns for r in data_rows)
    return len(data_rows), columns, width_ok


def load_csv_dicts(repo_root: Path, rel: str):
    path = repo_root / rel
    if not path.exists():
        return None
    text = path.read_bytes().decode("utf-8-sig", errors="replace")
    return list(csv.DictReader(io.StringIO(text)))


def read_text(repo_root: Path, rel: str):
    path = repo_root / rel
    if not path.exists():
        return None
    return path.read_bytes().decode("utf-8", errors="replace")


# --------------------------------------------------------------------------- #
# Validations
# --------------------------------------------------------------------------- #

def _find_col(fieldnames, *candidates):
    """Return the first matching column name (case-insensitive) or None."""
    if not fieldnames:
        return None
    lower = {f.lower().strip(): f for f in fieldnames}
    for cand in candidates:
        if cand.lower() in lower:
            return lower[cand.lower()]
    # loose contains match
    for cand in candidates:
        for key, original in lower.items():
            if cand.lower() in key:
                return original
    return None


def no_duplicates_in_column(repo_root, rel, *col_candidates):
    rows = load_csv_dicts(repo_root, rel)
    if rows is None:
        return False, f"{rel} not found"
    if not rows:
        return True, "empty"
    col = _find_col(rows[0].keys(), *col_candidates)
    if not col:
        return False, f"column {col_candidates} not found in {rel}"
    seen, dups = set(), set()
    for r in rows:
        val = (r.get(col) or "").strip()
        if not val:
            continue
        if val in seen:
            dups.add(val)
        seen.add(val)
    return (len(dups) == 0), (f"duplicates: {sorted(dups)}" if dups else "ok")


def no_duplicate_bibtex_keys(repo_root):
    text = read_text(repo_root, REFERENCES_BIB)
    if text is None:
        return False, f"{REFERENCES_BIB} not found"
    keys = []
    for m in re.finditer(r"@(\w+)\s*\{\s*([^,\s}]+)\s*,", text):
        entry_type = m.group(1).lower()
        if entry_type in {"comment", "string", "preamble"}:
            continue
        keys.append(m.group(2).strip())
    seen, dups = set(), set()
    for k in keys:
        if k in seen:
            dups.add(k)
        seen.add(k)
    return (len(dups) == 0), (f"duplicates: {sorted(dups)}" if dups else f"{len(keys)} keys, ok")


def _row_for_id(repo_root, rel, paper_id):
    """Return the dict row whose any cell equals paper_id (case-insensitive)."""
    rows = load_csv_dicts(repo_root, rel)
    if not rows:
        return None
    for r in rows:
        for v in r.values():
            if v and v.strip().upper() == paper_id.upper():
                return r
    return None


def _row_text(row):
    return " | ".join((v or "") for v in row.values())


def check_id_status(repo_root, paper_id, required_any=None, required_all=None,
                    files=(SEED_MAP, EVAL_ROBUSTNESS)):
    """Verify the row for paper_id contains the expected status tokens.

    required_any : at least one of these substrings must be present
    required_all : all of these substrings must be present
    Searches each file in `files`; passes if any file's matching row satisfies.
    """
    found_any_row = False
    for rel in files:
        row = _row_for_id(repo_root, rel, paper_id)
        if row is None:
            continue
        found_any_row = True
        blob = _row_text(row).lower()
        ok = True
        if required_all:
            ok = ok and all(tok.lower() in blob for tok in required_all)
        if required_any:
            ok = ok and any(tok.lower() in blob for tok in required_any)
        if ok:
            return True, f"{paper_id} satisfied in {rel}"
    if not found_any_row:
        return False, f"{paper_id} row not found in {files}"
    return False, f"{paper_id} found but status tokens missing"


def check_tokens_present(repo_root, rel, tokens):
    text = read_text(repo_root, rel)
    if text is None:
        return False, f"{rel} not found", []
    missing = [t for t in tokens if t not in text]
    return (len(missing) == 0), ("ok" if not missing else f"missing: {missing}"), missing


def run_validations(repo_root):
    details = {}

    ok, note = no_duplicates_in_column(repo_root, SEED_MAP, "PaperID", "Paper_ID", "ID")
    details["no_duplicate_paper_ids"] = {"ok": ok, "note": note}

    ok, note = no_duplicates_in_column(repo_root, EVIDENCE_MATRIX, "ClaimID", "Claim_ID", "Claim")
    details["no_duplicate_claim_ids"] = {"ok": ok, "note": note}

    ok, note = no_duplicates_in_column(repo_root, CITATION_LOG, "CitationKey", "Citation_Key", "Key", "BibKey")
    details["no_duplicate_citation_keys"] = {"ok": ok, "note": note}

    ok, note = no_duplicate_bibtex_keys(repo_root)
    details["no_duplicate_bibtex_keys"] = {"ok": ok, "note": note}

    ok, note = check_id_status(repo_root, "BF24", required_any=["Watchlist-ArXiv", "Watchlist-current", "Watchlist"])
    details["bf24_watchlist_only"] = {"ok": ok, "note": note}

    ok, note = check_id_status(repo_root, "BF25", required_any=["efficiency", "compute", "generalization"])
    details["bf25_efficiency_only"] = {"ok": ok, "note": note}

    ok, note = check_id_status(repo_root, "BF16", required_all=["Verified-secondary-source"],
                               required_any=["High-value-citable", "High value citable", "High-value"])
    details["bf16_secondary_verified"] = {"ok": ok, "note": note}

    ok, note = check_id_status(repo_root, "BF18", required_any=["Verified-primary-source"])
    details["bf18_primary_verified"] = {"ok": ok, "note": note}

    sub = {}
    all_bg = True
    for pid in ("BF13", "BF14", "BF15"):
        o, n = check_id_status(repo_root, pid, required_any=["Background-support", "Background support"])
        sub[pid] = {"ok": o, "note": n}
        all_bg = all_bg and o
    details["bf13_15_background_support"] = {"ok": all_bg, "note": sub}

    ok, note, missing = check_tokens_present(repo_root, EVIDENCE_MATRIX, CF_CLAIMS)
    details["cf_claims_present"] = {"ok": ok, "note": note, "missing": missing}

    # Compact boolean summary (matches the spec's manifest shape).
    summary = {k: bool(v["ok"]) for k, v in details.items()}
    return summary, details


# --------------------------------------------------------------------------- #
# Snapshot build
# --------------------------------------------------------------------------- #

def build_file_entries(repo_root: Path, base_url: str):
    entries = {}
    for rel in ALLOWLIST:
        src = repo_root / rel
        api_url = f"{base_url}/api/air/file?path={rel}"
        if not src.exists() or not src.is_file():
            entries[rel] = {"exists": False, "api_url": api_url}
            continue
        data = src.read_bytes()
        entry = {
            "exists": True,
            "bytes": len(data),
            "sha256": sha256_of(data),
            "lines": count_lines(data),
            "api_url": api_url,
        }
        if rel.lower().endswith(".csv"):
            rows, cols, width_ok = csv_stats(data)
            entry.update({"rows": rows, "columns": cols, "csv_width_ok": width_ok})
        entries[rel] = entry
    return entries


def mirror_files(repo_root: Path, out_dir: Path):
    """Copy allowlisted files into out_dir/files/<relative path>."""
    files_root = out_dir / "files"
    if files_root.exists():
        shutil.rmtree(files_root)
    files_root.mkdir(parents=True, exist_ok=True)
    for rel in ALLOWLIST:
        src = repo_root / rel
        if not src.exists() or not src.is_file():
            continue
        dst = files_root / rel
        dst.parent.mkdir(parents=True, exist_ok=True)
        shutil.copy2(src, dst)


def main(argv=None):
    parser = argparse.ArgumentParser(description="Generate AIR_review API snapshot.")
    parser.add_argument("--out", default="air_api_snapshot", help="Output snapshot directory.")
    parser.add_argument("--base-url", default=DEFAULT_BASE_URL, help="Public base URL for api_url fields.")
    parser.add_argument("--repo-root", default=None, help="Override repo root (default: auto-detect via git).")
    args = parser.parse_args(argv)

    base_url = args.base_url.rstrip("/")
    start = Path(args.repo_root) if args.repo_root else Path.cwd()
    repo_root = find_repo_root(start)

    commit = _git(["rev-parse", "HEAD"], repo_root) or "unknown"
    branch = _git(["branch", "--show-current"], repo_root) or "unknown"
    generated_at = datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")

    print(f"[air-snapshot] repo_root = {repo_root}")
    print(f"[air-snapshot] commit    = {commit}")
    print(f"[air-snapshot] branch    = {branch}")

    files = build_file_entries(repo_root, base_url)
    validations, validation_details = run_validations(repo_root)

    missing = [rel for rel, e in files.items()
               if not e["exists"] and rel not in ("LATEST_REPO_STATE.md", "repo_manifest.json")]
    all_valid = all(validations.values())
    status = "ok" if (not missing and all_valid) else "degraded"

    manifest = {
        "project": PROJECT,
        "repository": REPOSITORY,
        "branch": branch,
        "commit": commit,
        "generated_at_utc": generated_at,
        "frozen_blocks": FROZEN_BLOCKS,
        "status": status,
        "files": files,
        "validations": validations,
        "validation_details": validation_details,
        "missing_files": missing,
    }

    latest = {
        "project": PROJECT,
        "repository": REPOSITORY,
        "commit": commit,
        "branch": branch,
        "generated_at_utc": generated_at,
        "frozen_blocks": FROZEN_BLOCKS,
        "status": status,
        "manifest_url": f"{base_url}/api/air/manifest",
        "key_files": {
            name: f"{base_url}/api/air/file?path={rel}"
            for name, rel in KEY_FILES.items()
        },
        "validations": validations,
        "chatgpt_verification_targets": {
            "must_find_in_seed_map": ["BF24", "BF25"],
            "must_find_in_evidence_to_claim_matrix": ["C-F1", "C-F8"],
            "must_find_in_evaluation_robustness_matrix": ["BF24", "BF25"],
            "current_commit": commit,
        },
    }

    health = {
        "status": "ok",
        "service": "AIR_review public snapshot API",
        "commit": commit,
        "generated_at_utc": generated_at,
    }

    out_dir = (repo_root / args.out) if not os.path.isabs(args.out) else Path(args.out)
    out_dir.mkdir(parents=True, exist_ok=True)

    (out_dir / "manifest.json").write_text(json.dumps(manifest, indent=2), encoding="utf-8")
    (out_dir / "latest.json").write_text(json.dumps(latest, indent=2), encoding="utf-8")
    (out_dir / "health.json").write_text(json.dumps(health, indent=2), encoding="utf-8")
    mirror_files(repo_root, out_dir)

    print(f"[air-snapshot] wrote snapshot to {out_dir}")
    print(f"[air-snapshot] status = {status}")
    if missing:
        print(f"[air-snapshot] WARNING missing allowlisted files: {missing}")
    failed = [k for k, v in validations.items() if not v]
    if failed:
        print(f"[air-snapshot] WARNING failed validations: {failed}")
    else:
        print("[air-snapshot] all validations passed")

    return 0


if __name__ == "__main__":
    sys.exit(main())
