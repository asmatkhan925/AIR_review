#!/usr/bin/env python3
"""Convert CSV synthesis matrices into Markdown tables."""

from __future__ import annotations

import argparse
import csv
from pathlib import Path


def csv_to_markdown(path: Path) -> str:
    with path.open(newline="", encoding="utf-8") as handle:
        rows = list(csv.reader(handle))
    if not rows:
        return ""
    header = rows[0]
    separator = ["---"] * len(header)
    lines = [
        "| " + " | ".join(header) + " |",
        "| " + " | ".join(separator) + " |",
    ]
    for row in rows[1:]:
        padded = row + [""] * (len(header) - len(row))
        lines.append("| " + " | ".join(cell.replace("\n", " ") for cell in padded[: len(header)]) + " |")
    return "\n".join(lines) + "\n"


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("csv_files", nargs="*", default=sorted(str(path) for path in Path("05_synthesis_matrices").glob("*.csv")))
    parser.add_argument("--out-dir", default="08_tables/generated")
    args = parser.parse_args()

    out_dir = Path(args.out_dir)
    out_dir.mkdir(parents=True, exist_ok=True)

    for csv_file in args.csv_files:
        source = Path(csv_file)
        markdown = csv_to_markdown(source)
        target = out_dir / f"{source.stem}.md"
        target.write_text(f"# {source.stem.replace('_', ' ').title()}\n\n{markdown}", encoding="utf-8")
        print(f"Wrote {target}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
