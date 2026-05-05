#!/usr/bin/env python3
"""Summarize BibTeX references by entry type and year."""

from __future__ import annotations

import argparse
import re
from collections import Counter
from pathlib import Path


ENTRY_TYPE_RE = re.compile(r"@(\w+)\s*\{", re.IGNORECASE)
YEAR_RE = re.compile(r"\byear\s*=\s*[\{\"]?(\d{4})", re.IGNORECASE)


def strip_comment_lines(text: str) -> str:
    return "\n".join(line for line in text.splitlines() if not line.lstrip().startswith("%"))


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("bib", nargs="?", default="03_references/references.bib")
    args = parser.parse_args()

    text = strip_comment_lines(Path(args.bib).read_text(encoding="utf-8"))
    entry_types = Counter(match.lower() for match in ENTRY_TYPE_RE.findall(text))
    years = Counter(YEAR_RE.findall(text))

    print("Entry types:")
    if entry_types:
        for entry_type, count in sorted(entry_types.items()):
            print(f"  {entry_type}: {count}")
    else:
        print("  No BibTeX entries found.")

    print("\nYears:")
    if years:
        for year, count in sorted(years.items()):
            print(f"  {year}: {count}")
    else:
        print("  No years found.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
