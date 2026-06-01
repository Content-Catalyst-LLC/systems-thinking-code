"""Compare early and late intervention scenarios."""
from __future__ import annotations

from pathlib import Path
import csv

ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "data" / "processed"
OUT = ROOT / "outputs" / "tables"


def main() -> None:
    OUT.mkdir(parents=True, exist_ok=True)
    target = {"S001", "S002", "S004"}
    with (DATA / "outcomes.csv").open(newline="") as src, (OUT / "early_late_intervention_comparison.csv").open("w", newline="") as dst:
        reader = csv.DictReader(src)
        writer = csv.DictWriter(dst, fieldnames=reader.fieldnames)
        writer.writeheader()
        for row in reader:
            if row["scenario_id"] in target:
                writer.writerow(row)


if __name__ == "__main__":
    main()
