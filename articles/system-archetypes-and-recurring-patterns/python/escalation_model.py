#!/usr/bin/env python3
"""Escalation model: two actors intensify based on relative comparison."""

from pathlib import Path
import csv

ROOT = Path(__file__).resolve().parents[1]
out = ROOT / "outputs" / "tables" / "escalation_model.csv"
out.parent.mkdir(parents=True, exist_ok=True)

actor_a = 40.0
actor_b = 42.0
rows = []

for t in range(30):
    gap_ab = actor_b - actor_a
    gap_ba = actor_a - actor_b
    actor_a += max(gap_ab, 0) * 0.18 + 1.2
    actor_b += max(gap_ba, 0) * 0.18 + 1.2
    rows.append({"time": t, "actor_a_action": round(actor_a, 3), "actor_b_action": round(actor_b, 3), "difference": round(actor_a - actor_b, 3)})

with out.open("w", newline="", encoding="utf-8") as f:
    writer = csv.DictWriter(f, fieldnames=rows[0].keys())
    writer.writeheader()
    writer.writerows(rows)

print(f"Wrote {out}")
