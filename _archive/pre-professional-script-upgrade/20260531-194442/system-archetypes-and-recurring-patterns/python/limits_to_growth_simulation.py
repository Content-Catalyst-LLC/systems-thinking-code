#!/usr/bin/env python3
"""Simple limits-to-growth simulation using logistic recurrence."""

from pathlib import Path
import csv

ROOT = Path(__file__).resolve().parents[1]
out = ROOT / "outputs" / "tables" / "limits_to_growth_simulation.csv"
out.parent.mkdir(parents=True, exist_ok=True)

capacity_limit = 100.0
growth_rate = 0.32
state = 8.0

rows = []
for t in range(31):
    rows.append({"time": t, "system_size": round(state, 4), "capacity_limit": capacity_limit})
    state = state + growth_rate * state * (1 - state / capacity_limit)

with out.open("w", newline="", encoding="utf-8") as f:
    writer = csv.DictWriter(f, fieldnames=rows[0].keys())
    writer.writeheader()
    writer.writerows(rows)

print(f"Wrote {out}")
