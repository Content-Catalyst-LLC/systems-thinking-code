"""Compare actual and perceived system state using synthetic indicators."""

from __future__ import annotations

import csv
from pathlib import Path

DATA = Path(__file__).resolve().parents[1] / "data" / "synthetic_indicators.csv"


def main() -> None:
    with DATA.open(newline="", encoding="utf-8") as handle:
        rows = list(csv.DictReader(handle))

    print("period,actual_risk,perceived_risk,misperception_gap")
    for row in rows:
        actual = float(row["actual_risk"])
        perceived = float(row["perceived_risk"])
        gap = actual - perceived
        print(f"{row['period']},{actual:.1f},{perceived:.1f},{gap:.1f}")


if __name__ == "__main__":
    main()
