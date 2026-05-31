#!/usr/bin/env python3
"""Link causal-loop reasoning to behavior-over-time trends."""
from __future__ import annotations

import csv
from pathlib import Path

BASE = Path(__file__).resolve().parents[1]
DATA = BASE / "data"


def trend(values: list[float]) -> str:
    change = values[-1] - values[0]
    if change > 5:
        return "increasing"
    if change < -5:
        return "decreasing"
    return "roughly stable"


def main() -> None:
    with (DATA / "synthetic_behavior_over_time.csv").open(newline="", encoding="utf-8") as f:
        rows = list(csv.DictReader(f))
    fields = [field for field in rows[0].keys() if field != "time_step"]
    for field in fields:
        values = [float(row[field]) for row in rows]
        print(f"{field}: {trend(values)} ({values[0]} -> {values[-1]})")


if __name__ == "__main__":
    main()
