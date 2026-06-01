#!/usr/bin/env python3
"""Simple validation checks for signed causal-edge tables."""
from __future__ import annotations

import csv
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
EDGES = ROOT / "data" / "synthetic_signed_edges.csv"
VALID_SIGNS = {"+", "-"}
VALID_DELAYS = {"none", "short", "medium", "long"}


def main() -> None:
    errors: list[str] = []
    with EDGES.open(newline="", encoding="utf-8") as handle:
        for row_number, row in enumerate(csv.DictReader(handle), start=2):
            if row["sign"] not in VALID_SIGNS:
                errors.append(f"Row {row_number}: invalid sign {row['sign']!r}")
            if row["delay"] not in VALID_DELAYS:
                errors.append(f"Row {row_number}: invalid delay {row['delay']!r}")
            if not row["mechanism"].strip():
                errors.append(f"Row {row_number}: missing mechanism")
    if errors:
        print("Validation errors:")
        for error in errors:
            print(f"- {error}")
        raise SystemExit(1)
    print("Signed causal-edge table passed validation.")


if __name__ == "__main__":
    main()
