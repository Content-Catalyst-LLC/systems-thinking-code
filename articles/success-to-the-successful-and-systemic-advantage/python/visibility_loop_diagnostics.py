#!/usr/bin/env python3
"""Estimate how visibility loops can amplify already-visible actors."""
from __future__ import annotations
import csv
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
RAW = ROOT / "data" / "raw"
OUT = ROOT / "outputs" / "tables"
OUT.mkdir(parents=True, exist_ok=True)

rows = []
with (RAW / "synthetic_initial_conditions.csv").open(newline="") as f:
    for row in csv.DictReader(f):
        visibility = float(row["starting_visibility"])
        credibility = float(row["starting_credibility"])
        opportunity = float(row["starting_opportunity"])
        amplification = 0.50 * visibility + 0.30 * credibility + 0.20 * opportunity
        rows.append({
            "actor_id": row["actor_id"],
            "visibility_loop_score": round(amplification, 2),
            "interpretation": "high amplification risk" if amplification >= 75 else "capacity-building needed" if amplification < 45 else "moderate amplification",
        })

with (OUT / "visibility_loop_diagnostics.csv").open("w", newline="") as f:
    writer = csv.DictWriter(f, fieldnames=list(rows[0].keys()))
    writer.writeheader()
    writer.writerows(rows)

print(f"Wrote {OUT / 'visibility_loop_diagnostics.csv'}")
