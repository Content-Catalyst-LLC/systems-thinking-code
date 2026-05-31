#!/usr/bin/env python3
"""Summarize loop counts by polarity."""
from __future__ import annotations

import csv
from collections import Counter
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
LOOPS = ROOT / "data" / "synthetic_feedback_loops.csv"


def main() -> None:
    with LOOPS.open(newline="", encoding="utf-8") as handle:
        counts = Counter(row["loop_polarity"] for row in csv.DictReader(handle))
    for polarity, count in sorted(counts.items()):
        print(f"{polarity}: {count}")


if __name__ == "__main__":
    main()
