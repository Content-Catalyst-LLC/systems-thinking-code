#!/usr/bin/env python3
"""Distributional summary of systemic advantage gaps."""
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

by_group = {}
for row in actors:
    by_group.setdefault(row["actor_group"], []).append(row)

rows = []
for group, items in by_group.items():
    rows.append({
        "actor_group": group,
        "mean_initial_advantage": round(mean(float(x["initial_advantage"]) for x in items), 2),
        "mean_initial_capacity": round(mean(float(x["initial_capacity"]) for x in items), 2),
        "mean_need_score": round(mean(float(x["need_score"]) for x in items), 2),
        "mean_network_connections": round(mean(float(x["network_connections"]) for x in items), 2),
    })

with (OUT / "distributional_advantage_summary.csv").open("w", newline="") as f:
    writer = csv.DictWriter(f, fieldnames=list(rows[0].keys()))
    writer.writeheader()
    writer.writerows(rows)

print(f"Wrote {OUT / 'distributional_advantage_summary.csv'}")
