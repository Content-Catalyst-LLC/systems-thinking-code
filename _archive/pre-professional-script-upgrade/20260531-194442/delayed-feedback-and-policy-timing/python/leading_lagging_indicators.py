"""Create a simple leading/lagging indicator comparison."""
from __future__ import annotations

from pathlib import Path
import csv

ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "data" / "processed"
OUT = ROOT / "outputs" / "tables"


def main() -> None:
    OUT.mkdir(parents=True, exist_ok=True)
    with (DATA / "indicators.csv").open(newline="") as src, (OUT / "indicator_gap_summary.csv").open("w", newline="") as dst:
        reader = csv.DictReader(src)
        writer = csv.writer(dst)
        writer.writerow(["month", "domain", "leading_indicator", "lagging_indicator", "leading_lagging_gap"])
        for row in reader:
            gap = float(row["leading_indicator"]) - float(row["lagging_indicator"])
            writer.writerow([row["month"], row["domain"], row["leading_indicator"], row["lagging_indicator"], round(gap, 3)])


if __name__ == "__main__":
    main()
