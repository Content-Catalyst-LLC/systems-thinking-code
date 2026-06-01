#!/usr/bin/env python3
"""Fixes-that-fail model: quick relief with delayed consequence."""

from collections import deque
from pathlib import Path
import csv

ROOT = Path(__file__).resolve().parents[1]
out = ROOT / "outputs" / "tables" / "fixes_that_fail_model.csv"
out.parent.mkdir(parents=True, exist_ok=True)

problem = 60.0
fix_history = deque([0.0, 0.0, 0.0], maxlen=3)
rows = []

for t in range(25):
    fix = 0.35 * problem
    delayed_fix = fix_history[0]
    problem = problem - 0.25 * fix + 0.18 * delayed_fix + 4.0
    fix_history.append(fix)
    rows.append({"time": t, "problem_level": round(problem, 3), "quick_fix": round(fix, 3), "delayed_consequence_source": round(delayed_fix, 3)})

with out.open("w", newline="", encoding="utf-8") as f:
    writer = csv.DictWriter(f, fieldnames=rows[0].keys())
    writer.writeheader()
    writer.writerows(rows)

print(f"Wrote {out}")
