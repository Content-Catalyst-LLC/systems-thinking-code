#!/usr/bin/env python3
"""Compare performance-only allocation with need-adjusted resource allocation."""
from __future__ import annotations
import csv
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
RAW = ROOT / "data" / "raw"
OUT = ROOT / "outputs" / "tables"
OUT.mkdir(parents=True, exist_ok=True)

actors = []
with (RAW / "synthetic_actors.csv").open(newline="") as f:
    for row in csv.DictReader(f):
        actors.append(row)

scenarios = []
with (RAW / "synthetic_intervention_scenarios.csv").open(newline="") as f:
    for row in csv.DictReader(f):
        scenarios.append(row)

rows = []
for s in scenarios:
    p_w = float(s["performance_weight"])
    n_w = float(s["need_weight"])
    i_w = float(s["improvement_weight"])
    scores = []
    for a in actors:
        performance = float(a["initial_advantage"])
        need = float(a["need_score"])
        improvement_potential = max(0.0, 100.0 - float(a["initial_capacity"]))
        score = p_w * performance + n_w * need + i_w * improvement_potential
        scores.append((a, score))
    total_score = sum(score for _, score in scores)
    for a, score in scores:
        rows.append({
            "scenario": s["scenario"],
            "actor_id": a["actor_id"],
            "actor_group": a["actor_group"],
            "allocation_score": round(score, 3),
            "resource_share": round(score / total_score, 5),
        })

with (OUT / "allocation_rule_comparison.csv").open("w", newline="") as f:
    writer = csv.DictWriter(f, fieldnames=list(rows[0].keys()))
    writer.writeheader()
    writer.writerows(rows)

print(f"Wrote {OUT / 'allocation_rule_comparison.csv'}")
