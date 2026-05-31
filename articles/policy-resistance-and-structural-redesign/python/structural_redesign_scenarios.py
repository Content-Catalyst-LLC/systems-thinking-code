#!/usr/bin/env python3
"""Compare pressure-only interventions with structural-redesign scenarios."""
from __future__ import annotations
import csv
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / "outputs" / "tables"
OUT.mkdir(parents=True, exist_ok=True)

scenarios = [
    {"scenario": "pressure_only", "direct_effect": 18, "offset": 14, "burden": 16, "capacity_gain": 1},
    {"scenario": "pressure_plus_monitoring", "direct_effect": 17, "offset": 10, "burden": 10, "capacity_gain": 3},
    {"scenario": "structural_redesign", "direct_effect": 13, "offset": 4, "burden": 4, "capacity_gain": 10},
    {"scenario": "participatory_redesign", "direct_effect": 12, "offset": 3, "burden": 2, "capacity_gain": 12},
]

rows = []
for item in scenarios:
    net_effect = item["direct_effect"] - item["offset"] - 0.35 * item["burden"] + 0.6 * item["capacity_gain"]
    rows.append({**item, "burden_adjusted_value": round(net_effect, 2)})

with (OUT / "structural_redesign_scenarios.csv").open("w", newline="") as f:
    writer = csv.DictWriter(f, fieldnames=list(rows[0].keys()))
    writer.writeheader()
    writer.writerows(rows)

print("Wrote outputs/tables/structural_redesign_scenarios.csv")
