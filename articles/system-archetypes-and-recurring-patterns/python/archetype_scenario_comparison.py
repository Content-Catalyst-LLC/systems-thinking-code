#!/usr/bin/env python3
"""Compare synthetic model runs across scenario IDs."""

from pathlib import Path
import csv
from collections import defaultdict

ROOT = Path(__file__).resolve().parents[1]
runs_path = ROOT / "data" / "synthetic_model_runs.csv"
out = ROOT / "outputs" / "tables" / "scenario_comparison_summary.csv"
out.parent.mkdir(parents=True, exist_ok=True)

by_scenario = defaultdict(list)
with runs_path.open(newline="", encoding="utf-8") as f:
    for row in csv.DictReader(f):
        by_scenario[row["scenario_id"]].append(row)

summary = []
for scenario_id, rows in sorted(by_scenario.items()):
    first = rows[0]
    last = rows[-1]
    summary.append({
        "scenario_id": scenario_id,
        "initial_problem": first["problem_level"],
        "final_problem": last["problem_level"],
        "initial_capacity": first["capacity"],
        "final_capacity": last["capacity"],
        "initial_trust": first["trust"],
        "final_trust": last["trust"],
    })

with out.open("w", newline="", encoding="utf-8") as f:
    writer = csv.DictWriter(f, fieldnames=summary[0].keys())
    writer.writeheader()
    writer.writerows(summary)

print(f"Wrote {out}")
