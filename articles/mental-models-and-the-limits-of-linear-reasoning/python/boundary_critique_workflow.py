#!/usr/bin/env python3
"""Summarize boundary exclusions and ethical risk in synthetic mental models."""
import csv
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "data" / "raw" / "synthetic_boundaries.csv"
OUT = ROOT / "outputs" / "tables"
OUT.mkdir(parents=True, exist_ok=True)

rows = []
with DATA.open(newline="") as f:
    for row in csv.DictReader(f):
        risk = float(row["ethical_risk_score"])
        row["boundary_review_level"] = "urgent" if risk >= 0.75 else "review" if risk >= 0.5 else "monitor"
        rows.append(row)

with (OUT / "boundary_critique_workflow.csv").open("w", newline="") as f:
    writer = csv.DictWriter(f, fieldnames=rows[0].keys())
    writer.writeheader()
    writer.writerows(rows)

print("Wrote outputs/tables/boundary_critique_workflow.csv")
