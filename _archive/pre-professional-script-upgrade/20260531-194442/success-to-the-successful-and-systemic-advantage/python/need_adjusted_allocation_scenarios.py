#!/usr/bin/env python3
"""Create summary measures for need-adjusted allocation scenarios."""
from __future__ import annotations
import csv
from pathlib import Path
from statistics import mean

ROOT = Path(__file__).resolve().parents[1]
RAW = ROOT / "data" / "raw"
OUT = ROOT / "outputs" / "tables"
OUT.mkdir(parents=True, exist_ok=True)

actors = []
with (RAW / "synthetic_actors.csv").open(newline="") as f:
    actors = list(csv.DictReader(f))

scenario_rows = []
weights = {
    "performance_only": (0.85, 0.05, 0.05),
    "need_adjusted": (0.45, 0.30, 0.20),
    "capacity_building": (0.30, 0.35, 0.25),
}
for scenario, (pw, nw, iw) in weights.items():
    awards = []
    for a in actors:
        performance = float(a["initial_advantage"])
        need = float(a["need_score"])
        improvement = 100.0 - float(a["initial_capacity"])
        score = pw * performance + nw * need + iw * improvement
        awards.append((a["actor_group"], score))
    high = [score for group, score in awards if group == "high_advantage"]
    low = [score for group, score in awards if group == "low_advantage"]
    scenario_rows.append({
        "scenario": scenario,
        "high_advantage_mean_allocation_score": round(mean(high), 2),
        "low_advantage_mean_allocation_score": round(mean(low), 2),
        "allocation_gap": round(mean(high) - mean(low), 2),
    })

with (OUT / "need_adjusted_scenario_summary.csv").open("w", newline="") as f:
    writer = csv.DictWriter(f, fieldnames=list(scenario_rows[0].keys()))
    writer.writeheader()
    writer.writerows(scenario_rows)

print(f"Wrote {OUT / 'need_adjusted_scenario_summary.csv'}")
