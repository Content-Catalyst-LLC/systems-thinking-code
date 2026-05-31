#!/usr/bin/env python3
"""Simulate success-to-the-successful cumulative advantage dynamics."""
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
        actors.append({
            "actor_id": row["actor_id"],
            "group": row["actor_group"],
            "advantage": float(row["initial_advantage"]),
            "need": float(row["need_score"]),
        })

def run(periods: int = 12, total_resources: float = 1_200_000, feedback: float = 0.62):
    rows = []
    for t in range(periods + 1):
        total_advantage = sum(max(a["advantage"], 1) for a in actors)
        for a in actors:
            share = max(a["advantage"], 1) / total_advantage
            resources = share * total_resources
            rows.append({
                "period": t,
                "actor_id": a["actor_id"],
                "actor_group": a["group"],
                "advantage_index": round(a["advantage"], 3),
                "resource_share": round(share, 5),
                "resource_award": round(resources, 2),
            })
        for a in actors:
            share = max(a["advantage"], 1) / total_advantage
            a["advantage"] += feedback * share * 10
    return rows

rows = run()
with (OUT / "cumulative_advantage_outputs.csv").open("w", newline="") as f:
    writer = csv.DictWriter(f, fieldnames=list(rows[0].keys()))
    writer.writeheader()
    writer.writerows(rows)

print(f"Wrote {OUT / 'cumulative_advantage_outputs.csv'}")
