#!/usr/bin/env python3
"""Tragedy-of-the-commons model with optional governance after midpoint."""

from pathlib import Path
import csv

ROOT = Path(__file__).resolve().parents[1]
out = ROOT / "outputs" / "tables" / "commons_depletion_model.csv"
out.parent.mkdir(parents=True, exist_ok=True)

resource = 100.0
users = 12
rows = []

for t in range(35):
    governance_factor = 1.0 if t < 16 else 0.62
    extraction = users * 2.1 * governance_factor
    regeneration = 0.09 * resource
    resource = max(0.0, resource + regeneration - extraction)
    rows.append({"time": t, "resource_stock": round(resource, 3), "extraction": round(extraction, 3), "regeneration": round(regeneration, 3), "governance_factor": governance_factor})

with out.open("w", newline="", encoding="utf-8") as f:
    writer = csv.DictWriter(f, fieldnames=rows[0].keys())
    writer.writeheader()
    writer.writerows(rows)

print(f"Wrote {out}")
