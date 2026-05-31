#!/usr/bin/env python3
"""Shifting-the-burden model: symptomatic relief weakens fundamental capacity."""

from pathlib import Path
import csv

ROOT = Path(__file__).resolve().parents[1]
out = ROOT / "outputs" / "tables" / "shifting_the_burden_model.csv"
out.parent.mkdir(parents=True, exist_ok=True)

symptom = 70.0
capacity = 45.0
rows = []

for t in range(30):
    symptomatic_fix = max(symptom, 0) * 0.25
    fundamental_investment = 4.0 if t >= 10 else 1.0
    capacity = capacity + fundamental_investment - 0.07 * symptomatic_fix
    symptom = symptom - 0.20 * symptomatic_fix - 0.08 * capacity + 8.0
    rows.append({
        "time": t,
        "symptom": round(symptom, 3),
        "symptomatic_fix": round(symptomatic_fix, 3),
        "fundamental_capacity": round(capacity, 3),
        "fundamental_investment": fundamental_investment,
    })

with out.open("w", newline="", encoding="utf-8") as f:
    writer = csv.DictWriter(f, fieldnames=rows[0].keys())
    writer.writeheader()
    writer.writerows(rows)

print(f"Wrote {out}")
