#!/usr/bin/env python3
"""Compare short-term relief with delayed unintended consequences."""
from __future__ import annotations

import csv
from collections import deque
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / "outputs" / "tables"
OUT.mkdir(parents=True, exist_ok=True)


def run(delay: int = 3, periods: int = 16) -> list[dict[str, float]]:
    problem = 100.0
    capacity = 1.0
    delayed_fixes: deque[float] = deque([0.0] * delay, maxlen=delay)
    rows = []
    for t in range(periods):
        fix = min(1.0, problem / 160.0)
        consequence = delayed_fixes[0] * 22.0
        capacity = max(0.15, capacity - 0.045 * fix + 0.012)
        problem = max(0.0, problem + 8.0 - 30.0 * fix + consequence + (1.0 - capacity) * 12.0)
        delayed_fixes.append(fix)
        rows.append({"period": t, "problem": round(problem, 2), "capacity": round(capacity, 3), "fix": round(fix, 3), "delayed_consequence": round(consequence, 2)})
    return rows


def main() -> None:
    rows = run()
    path = OUT / "delayed_consequence_simulation.csv"
    with path.open("w", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=list(rows[0].keys()))
        writer.writeheader()
        writer.writerows(rows)
    print(f"Wrote {path}")


if __name__ == "__main__":
    main()
