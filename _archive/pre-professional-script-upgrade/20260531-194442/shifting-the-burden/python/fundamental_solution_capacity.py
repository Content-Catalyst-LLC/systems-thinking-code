#!/usr/bin/env python3
"""Simulate fundamental capacity under relief-only and repair-oriented paths."""

from __future__ import annotations

from pathlib import Path
import csv

ARTICLE_DIR = Path(__file__).resolve().parents[1]
OUTPUT_PATH = ARTICLE_DIR / "outputs" / "tables" / "fundamental_capacity_paths.csv"


def simulate(periods: int, initial_capacity: float, repair: float, symptomatic_harm: float) -> list[float]:
    capacity = initial_capacity
    values: list[float] = []
    for _ in range(periods):
        capacity = max(0.0, capacity + repair - symptomatic_harm)
        values.append(round(capacity, 2))
    return values


def main() -> None:
    relief_only = simulate(10, 55, repair=1.0, symptomatic_harm=4.0)
    relief_plus_repair = simulate(10, 55, repair=6.0, symptomatic_harm=2.0)

    OUTPUT_PATH.parent.mkdir(parents=True, exist_ok=True)
    with OUTPUT_PATH.open("w", newline="", encoding="utf-8") as handle:
        writer = csv.writer(handle)
        writer.writerow(["period", "relief_only_capacity", "relief_plus_repair_capacity"])
        for idx, (a, b) in enumerate(zip(relief_only, relief_plus_repair)):
            writer.writerow([idx, a, b])

    print(f"Wrote {OUTPUT_PATH}")


if __name__ == "__main__":
    main()
