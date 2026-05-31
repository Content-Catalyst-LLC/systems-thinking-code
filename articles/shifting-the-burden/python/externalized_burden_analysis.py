#!/usr/bin/env python3
"""Aggregate synthetic externalized burden by group."""

from __future__ import annotations

from collections import defaultdict
from pathlib import Path
import csv

ARTICLE_DIR = Path(__file__).resolve().parents[1]
DATA_PATH = ARTICLE_DIR / "data" / "synthetic_externalized_burdens.csv"
OUTPUT_PATH = ARTICLE_DIR / "outputs" / "tables" / "externalized_burden_by_group.csv"


def main() -> None:
    totals: dict[str, float] = defaultdict(float)
    counts: dict[str, int] = defaultdict(int)

    with DATA_PATH.open(newline="", encoding="utf-8") as handle:
        for row in csv.DictReader(handle):
            group = row["group"]
            totals[group] += float(row["burden_score"])
            counts[group] += 1

    rows = [
        {"group": group, "average_burden_score": round(totals[group] / counts[group], 2)}
        for group in sorted(totals)
    ]

    OUTPUT_PATH.parent.mkdir(parents=True, exist_ok=True)
    with OUTPUT_PATH.open("w", newline="", encoding="utf-8") as handle:
        writer = csv.DictWriter(handle, fieldnames=["group", "average_burden_score"])
        writer.writeheader()
        writer.writerows(rows)

    for row in rows:
        print(row)


if __name__ == "__main__":
    main()
