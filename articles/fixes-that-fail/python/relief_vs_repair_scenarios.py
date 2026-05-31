#!/usr/bin/env python3
"""Compare quick-fix-only and relief-plus-repair scenarios."""
from __future__ import annotations

import csv
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / "outputs" / "tables"
OUT.mkdir(parents=True, exist_ok=True)

SCENARIOS = {
    "quick_fix_only": {"fix": 0.80, "repair": 0.05},
    "relief_plus_repair": {"fix": 0.55, "repair": 0.65},
    "prevention_first": {"fix": 0.25, "repair": 0.90},
}


def simulate(name: str, fix_policy: float, repair_policy: float, periods: int = 14) -> list[dict[str, float | str]]:
    problem = 100.0
    capacity = 1.0
    rows = []
    delayed = [0.0, 0.0, 0.0]
    for t in range(periods):
        fix = fix_policy * min(1.0, problem / 130.0)
        repair = repair_policy
        delayed_harm = delayed.pop(0) * 20.0
        capacity = max(0.1, capacity + 0.05 * repair - 0.05 * fix)
        problem = max(0.0, problem + 7.0 - 25.0 * fix - 10.0 * capacity + delayed_harm)
        delayed.append(fix)
        rows.append({"scenario": name, "period": t, "problem": round(problem, 2), "capacity": round(capacity, 3), "fix": round(fix, 3), "repair": round(repair, 3)})
    return rows


def main() -> None:
    rows = []
    for name, params in SCENARIOS.items():
        rows.extend(simulate(name, params["fix"], params["repair"]))
    path = OUT / "relief_vs_repair_scenarios.csv"
    with path.open("w", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=list(rows[0].keys()))
        writer.writeheader()
        writer.writerows(rows)
    print(f"Wrote {path}")


if __name__ == "__main__":
    main()
