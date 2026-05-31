#!/usr/bin/env python3
"""Create a simple sensitivity score for assumptions that should be tested first."""
import csv
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "data" / "raw" / "synthetic_assumptions.csv"
OUT = ROOT / "outputs" / "tables"
OUT.mkdir(parents=True, exist_ok=True)

priority_weight = {"high": 1.0, "medium": 0.65, "low": 0.35}
rows = []
with DATA.open(newline="") as f:
    for row in csv.DictReader(f):
        confidence = float(row["confidence"])
        weight = priority_weight.get(row["revision_priority"], 0.5)
        row["test_urgency_score"] = round(confidence * weight, 3)
        rows.append(row)

rows.sort(key=lambda r: float(r["test_urgency_score"]), reverse=True)
with (OUT / "assumption_sensitivity_analysis.csv").open("w", newline="") as f:
    writer = csv.DictWriter(f, fieldnames=rows[0].keys())
    writer.writeheader()
    writer.writerows(rows)

print("Wrote outputs/tables/assumption_sensitivity_analysis.csv")
