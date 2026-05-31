#!/usr/bin/env python3
"""Simulate a simple delayed feedback structure that linear reasoning misses."""
import csv
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / "outputs" / "tables"
OUT.mkdir(parents=True, exist_ok=True)

state = 50.0
delay_buffer = [0.0, 0.0, 0.0]
rows = []
for t in range(1, 21):
    intervention = 6.0 if t <= 8 else 2.0
    delayed_pushback = 0.55 * delay_buffer.pop(0)
    state = state + intervention - delayed_pushback
    delay_buffer.append(intervention)
    rows.append({
        "period": t,
        "intervention": intervention,
        "delayed_pushback": round(delayed_pushback, 3),
        "system_state": round(state, 3),
    })

with (OUT / "feedback_delay_simulation.csv").open("w", newline="") as f:
    writer = csv.DictWriter(f, fieldnames=rows[0].keys())
    writer.writeheader()
    writer.writerows(rows)

print("Wrote outputs/tables/feedback_delay_simulation.csv")
