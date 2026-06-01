#!/usr/bin/env python3
"""Eroding-goals model: pressure is reduced by lowering the goal."""

from pathlib import Path
import csv

ROOT = Path(__file__).resolve().parents[1]
out = ROOT / "outputs" / "tables" / "eroding_goals_simulation.csv"
out.parent.mkdir(parents=True, exist_ok=True)

goal = 90.0
actual = 70.0
rows = []

for t in range(25):
    gap = goal - actual
    goal = goal - 0.08 * gap
    actual = actual + 0.03 * gap - 1.0
    rows.append({"time": t, "goal": round(goal, 3), "actual_performance": round(actual, 3), "gap": round(goal - actual, 3)})

with out.open("w", newline="", encoding="utf-8") as f:
    writer = csv.DictWriter(f, fieldnames=rows[0].keys())
    writer.writeheader()
    writer.writerows(rows)

print(f"Wrote {out}")
