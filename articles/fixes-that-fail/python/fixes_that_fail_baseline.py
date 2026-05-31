#!/usr/bin/env python3
"""Baseline fixes-that-fail simulation with synthetic data."""
from __future__ import annotations

import csv
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "data"
OUT = ROOT / "outputs" / "tables"
OUT.mkdir(parents=True, exist_ok=True)


def simulate(periods: int = 12, initial_problem: float = 100.0, fix_intensity: float = 0.55, delay: int = 2) -> list[dict[str, float]]:
    problem = initial_problem
    past_fixes = [0.0] * (periods + delay + 1)
    rows: list[dict[str, float]] = []
    for t in range(periods):
        fix = fix_intensity * max(problem / 100.0, 0.0)
        immediate_relief = 24.0 * fix
        delayed_harm = 18.0 * past_fixes[t]
        underlying_demand = 7.5
        problem = max(0.0, problem + underlying_demand - immediate_relief + delayed_harm)
        past_fixes[t + delay] += fix
        rows.append({
            "period": t,
            "problem": round(problem, 3),
            "fix": round(fix, 3),
            "immediate_relief": round(immediate_relief, 3),
            "delayed_harm": round(delayed_harm, 3),
        })
    return rows


def main() -> None:
    rows = simulate()
    path = OUT / "fixes_that_fail_baseline.csv"
    with path.open("w", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=list(rows[0].keys()))
        writer.writeheader()
        writer.writerows(rows)
    print(f"Wrote {path}")


if __name__ == "__main__":
    main()
