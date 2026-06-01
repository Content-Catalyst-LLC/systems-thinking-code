#!/usr/bin/env python3
"""Report signed links that include delay annotations."""
from __future__ import annotations

import csv
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
EDGES = ROOT / "data" / "synthetic_signed_edges.csv"


def main() -> None:
    with EDGES.open(newline="", encoding="utf-8") as handle:
        for row in csv.DictReader(handle):
            if row["delay"] != "none":
                print(f"{row['source_variable']} --{row['sign']} ({row['delay']})--> {row['target_variable']}")


if __name__ == "__main__":
    main()
