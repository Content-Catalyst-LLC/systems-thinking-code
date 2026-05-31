#!/usr/bin/env python3
"""Rank synthetic mental models by systems quality and ethical boundary awareness."""
import csv
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "data" / "raw" / "synthetic_mental_models.csv"
OUT = ROOT / "outputs" / "tables"
OUT.mkdir(parents=True, exist_ok=True)

rows = []
with DATA.open(newline="") as f:
    for row in csv.DictReader(f):
        linear = float(row["linear_score"])
        feedback = float(row["feedback_score"])
        boundary = float(row["boundary_score"])
        power = float(row["power_awareness_score"])
        systemic_quality = (feedback + boundary + power + (1 - linear)) / 4
        row["systemic_quality_index"] = round(systemic_quality, 3)
        row["risk_label"] = "high linear-risk" if linear > 0.75 and boundary < 0.5 else "systemic or mixed"
        rows.append(row)

rows.sort(key=lambda r: float(r["systemic_quality_index"]), reverse=True)
with (OUT / "mental_model_comparison.csv").open("w", newline="") as f:
    writer = csv.DictWriter(f, fieldnames=rows[0].keys())
    writer.writeheader()
    writer.writerows(rows)

print("Wrote outputs/tables/mental_model_comparison.csv")
