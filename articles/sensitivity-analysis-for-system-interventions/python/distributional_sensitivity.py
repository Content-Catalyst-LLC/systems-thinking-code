#!/usr/bin/env python3
"""Distributional sensitivity example for low-buffer groups."""
from pathlib import Path
import csv

ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "data"
OUT = ROOT / "outputs" / "tables"
OUT.mkdir(parents=True, exist_ok=True)

def main() -> None:
    rows = []
    with (DATA / "synthetic_distributional_outputs.csv").open(newline="", encoding="utf-8") as f:
        for row in csv.DictReader(f):
            resilience = float(row["resilience"])
            burden = float(row["burden"])
            exposure = float(row["cost_exposure"])
            sensitivity_flag = "high" if resilience < 0.50 or burden > 0.65 or exposure > 140 else "moderate" if burden > 0.45 else "lower"
            rows.append({**row, "sensitivity_flag": sensitivity_flag})
    with (OUT / "distributional_sensitivity_flags.csv").open("w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=list(rows[0].keys()))
        writer.writeheader()
        writer.writerows(rows)
    print(f"Wrote {OUT / 'distributional_sensitivity_flags.csv'}")

if __name__ == "__main__":
    main()
