#!/usr/bin/env python3
"""Check references.bib for duplicate keys and repeated titles."""

from __future__ import annotations

import argparse
import re
from collections import defaultdict
from pathlib import Path


ENTRY_RE = re.compile(r"@\w+\s*\{\s*([^,\s]+)", re.IGNORECASE)
TITLE_RE = re.compile(r"\btitle\s*=\s*[\{\"](.+?)[\}\"]\s*,", re.IGNORECASE | re.DOTALL)


def normalize_title(title: str) -> str:
    title = re.sub(r"[{}]", "", title)
    title = re.sub(r"\s+", " ", title)
    return title.strip().lower()


def strip_comment_lines(text: str) -> str:
    return "\n".join(line for line in text.splitlines() if not line.lstrip().startswith("%"))


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("bib", nargs="?", default="03_references/references.bib")
    args = parser.parse_args()

    path = Path(args.bib)
    text = strip_comment_lines(path.read_text(encoding="utf-8"))

    keys = ENTRY_RE.findall(text)
    titles = [normalize_title(match) for match in TITLE_RE.findall(text)]

    duplicate_keys = {key: count for key, count in defaultdict(int, ((k, keys.count(k)) for k in set(keys))).items() if count > 1}

    title_counts: dict[str, int] = defaultdict(int)
    for title in titles:
        title_counts[title] += 1
    duplicate_titles = {title: count for title, count in title_counts.items() if count > 1 and title}

    if not duplicate_keys and not duplicate_titles:
        print(f"No duplicate BibTeX keys or titles found in {path}.")
        return 0

    if duplicate_keys:
        print("Duplicate keys:")
        for key, count in sorted(duplicate_keys.items()):
            print(f"  {key}: {count}")

    if duplicate_titles:
        print("Duplicate titles:")
        for title, count in sorted(duplicate_titles.items()):
            print(f"  {title}: {count}")

    return 1


if __name__ == "__main__":
    raise SystemExit(main())
