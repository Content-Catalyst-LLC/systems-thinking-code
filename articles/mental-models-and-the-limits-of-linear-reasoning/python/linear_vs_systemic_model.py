#!/usr/bin/env python3
"""Compare linear-pressure reasoning with feedback-aware systems reasoning."""
import csv
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / "outputs" / "tables"
OUT.mkdir(parents=True, exist_ok=True)

rows = []
for t in range(1, 13):
    linear_output = 100 + 5 * t
    fatigue = max(0, (t - 3) * 4)
    rework = fatigue * 0.65
    systemic_output = 100 + 4 * t - rework
    rows.append({
        "period": t,
        "linear_expected_output": round(linear_output, 2),
        "fatigue_stock": round(fatigue, 2),
        "rework_flow": round(rework, 2),
        "feedback_aware_output": round(systemic_output, 2),
    })

with (OUT / "linear_vs_systemic_model.csv").open("w", newline="") as f:
    writer = csv.DictWriter(f, fieldnames=rows[0].keys())
    writer.writeheader()
    writer.writerows(rows)

print("Wrote outputs/tables/linear_vs_systemic_model.csv")
