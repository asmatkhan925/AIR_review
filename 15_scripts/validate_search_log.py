#!/usr/bin/env python3
"""Validate required fields in literature-search CSV logs."""

from __future__ import annotations

import argparse
import csv
from pathlib import Path


REQUIRED_COLUMNS = {
    "02_literature_search/search_log.csv": ["Date", "Database", "Query", "Number of results", "Papers selected", "Notes"],
    "02_literature_search/screening_log.csv": ["Paper title", "Year", "Venue", "Included or excluded", "Reason", "Category"],
    "02_literature_search/rejected_papers_log.csv": ["Paper title", "Reason for rejection", "Possible future use"],
}


def validate(path: Path, required: list[str]) -> list[str]:
    problems: list[str] = []
    if not path.exists():
        return [f"{path}: file missing"]
    with path.open(newline="", encoding="utf-8") as handle:
        reader = csv.DictReader(handle)
        fieldnames = reader.fieldnames or []
        missing_columns = [column for column in required if column not in fieldnames]
        if missing_columns:
            problems.append(f"{path}: missing columns {', '.join(missing_columns)}")
            return problems
        for line_number, row in enumerate(reader, start=2):
            for column in required:
                value = (row.get(column) or "").strip()
                if not value:
                    problems.append(f"{path}:{line_number}: missing {column}")
    return problems


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("files", nargs="*", help="Optional CSV files to validate")
    args = parser.parse_args()

    targets = {Path(file_name): REQUIRED_COLUMNS.get(file_name, []) for file_name in args.files} if args.files else {
        Path(file_name): columns for file_name, columns in REQUIRED_COLUMNS.items()
    }

    problems: list[str] = []
    for path, columns in targets.items():
        if not columns:
            print(f"{path}: no validation rule configured")
            continue
        problems.extend(validate(path, columns))

    if problems:
        print("Search-log validation problems:")
        for problem in problems:
            print(f"  {problem}")
        return 1

    print("Search logs passed validation.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
