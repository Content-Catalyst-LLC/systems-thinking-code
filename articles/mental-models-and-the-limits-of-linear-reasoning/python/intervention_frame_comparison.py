#!/usr/bin/env python3
"""Compare intervention frames by redesign orientation."""
import csv
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "data" / "raw" / "synthetic_intervention_frames.csv"
OUT = ROOT / "outputs" / "tables"
OUT.mkdir(parents=True, exist_ok=True)

rows = []
with DATA.open(newline="") as f:
    for row in csv.DictReader(f):
        score = float(row["redesign_score"])
        row["frame_class"] = "structural redesign" if score >= 0.75 else "partial" if score >= 0.5 else "linear or pressure-based"
        rows.append(row)

rows.sort(key=lambda r: float(r["redesign_score"]), reverse=True)
with (OUT / "intervention_frame_comparison.csv").open("w", newline="") as f:
    writer = csv.DictWriter(f, fieldnames=rows[0].keys())
    writer.writeheader()
    writer.writerows(rows)

print("Wrote outputs/tables/intervention_frame_comparison.csv")
