# Scripts

## Purpose

This folder contains lightweight helper scripts for maintaining the review-paper repository.

## Scripts

- `check_bib_duplicates.py`: identify duplicate BibTeX keys or repeated titles.
- `count_papers_by_category.py`: count papers by category from screening and quality-label logs.
- `generate_reference_summary.py`: summarize BibTeX reference coverage by year and entry type.
- `validate_search_log.py`: check missing fields in search logs.
- `export_tables.py`: convert CSV synthesis matrices into Markdown tables.

## Usage

Run scripts from the repository root:

```bash
python3 15_scripts/check_bib_duplicates.py
python3 15_scripts/validate_search_log.py
```

These scripts are intentionally simple and local. They should help catch maintenance problems without becoming a heavyweight pipeline.
