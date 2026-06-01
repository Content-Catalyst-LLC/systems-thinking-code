#!/usr/bin/env python3
"""Simple path-dependence model: early investment changes future feasible states."""
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / "outputs" / "tables"
OUT.mkdir(parents=True, exist_ok=True)

rows = []
paths = {
    "early_advantage_path": {"capacity": 80.0, "investment": 12.0},
    "underinvestment_path": {"capacity": 30.0, "investment": 4.0},
    "repair_path": {"capacity": 30.0, "investment": 14.0},
}
for name, state in paths.items():
    capacity = state["capacity"]
    investment = state["investment"]
    for t in range(13):
        rows.append((name, t, round(capacity, 2)))
        capacity = capacity + investment * 0.55 + capacity * 0.025

with (OUT / "path_dependence_outputs.csv").open("w") as f:
    f.write("scenario,period,capacity_index\n")
    for row in rows:
        f.write(f"{row[0]},{row[1]},{row[2]}\n")

print(f"Wrote {OUT / 'path_dependence_outputs.csv'}")
