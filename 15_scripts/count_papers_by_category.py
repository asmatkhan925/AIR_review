#!/usr/bin/env python3
"""Count papers by category from repository CSV logs."""

from __future__ import annotations

import argparse
import csv
from collections import Counter
from pathlib import Path


DEFAULT_FILES = [
    "02_literature_search/screening_log.csv",
    "02_literature_search/paper_quality_labels.csv",
]


def find_category_column(fieldnames: list[str] | None) -> str | None:
    if not fieldnames:
        return None
    for candidate in ("Category", "category"):
        if candidate in fieldnames:
            return candidate
    return None


def count_file(path: Path) -> Counter[str]:
    counts: Counter[str] = Counter()
    if not path.exists():
        return counts
    with path.open(newline="", encoding="utf-8") as handle:
        reader = csv.DictReader(handle)
        column = find_category_column(reader.fieldnames)
        if not column:
            return counts
        for row in reader:
            value = (row.get(column) or "").strip()
            if value and value.upper() != "TBD":
                counts[value] += 1
    return counts


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("files", nargs="*", default=DEFAULT_FILES)
    args = parser.parse_args()

    total: Counter[str] = Counter()
    for file_name in args.files:
        total.update(count_file(Path(file_name)))

    if not total:
        print("No categorized papers found yet.")
        return 0

    for category, count in sorted(total.items()):
        print(f"{category}: {count}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
