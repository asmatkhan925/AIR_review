# ChatGPT Handoff Packages

This repository can generate a self-contained ZIP for continuing AIR review work in ChatGPT without relying on GitHub browsing, raw GitHub URLs, or website APIs.

## Basic Usage

Run from the repository root:

```bash
python scripts/prepare_chatgpt_handoff.py --query "next task or question here" --zip
```

The script creates `_chatgpt_handoff/AIR_review_handoff_<shortcommit>_<timestamp>.zip`.

## Supported Modes

```bash
python scripts/prepare_chatgpt_handoff.py --query "..." --full --zip
python scripts/prepare_chatgpt_handoff.py --query "..." --since HEAD~1 --zip
python scripts/prepare_chatgpt_handoff.py --query "..." --changed-only --zip
python scripts/prepare_chatgpt_handoff.py --validate-only
```

## What The ZIP Contains

Each ZIP includes:

- `CHATGPT_HANDOFF.md`
- `AIR_REVIEW_SNAPSHOT_MANIFEST.json`
- `VALIDATION_REPORT.md`
- `USER_QUERY.txt`
- Always-required project control files
- Query-relevant files selected by keyword matching
- Changed text-like files since the selected baseline

The manifest records commit, branch, dirty status, selected files, changed files, SHA-256 hashes, CSV metadata, validation results, and a recommended reading order for ChatGPT.

## Validation

The script validates included CSV files with Python's `csv` module and reports:

- row count and column count
- headers
- SHA-256 hash
- duplicate IDs for known ID columns
- empty obvious ID fields
- row-width errors

It also checks the current AIR review targets:

- `seed_paper_map.csv` contains `BF24` and `BF25`
- `evaluation_robustness_matrix.csv` contains `BF24` and `BF25`
- `evidence_to_claim_matrix.csv` contains `C-F1` through `C-F8`
- `references.bib` is present and non-empty
- `citation_verification_log.csv` is present if available

## Safety Rules

The handoff excludes `.git/`, virtual environments, caches, `node_modules/`, PDFs, audio/video/data binaries, private `.env` files, and other non-text artifacts. It includes only safe text-like files such as `.md`, `.csv`, `.bib`, `.txt`, `.json`, `.cff`, `.tex`, `.yml`, `.yaml`, and `.py`.

Generated files are local artifacts:

- `_chatgpt_handoff/`
- `.air_handoff_state.json`

These are ignored by Git.
