#!/usr/bin/env python3
"""Simulate dependency growth from repeated symptomatic relief."""

from __future__ import annotations

from pathlib import Path
import csv

ARTICLE_DIR = Path(__file__).resolve().parents[1]
OUTPUT_PATH = ARTICLE_DIR / "outputs" / "tables" / "dependency_loop_simulation.csv"


def main() -> None:
    dependency = 0.25
    rows: list[dict[str, float]] = []

    for period in range(12):
        symptomatic_reliance = 20 + period * 3
        repair_investment = 6 + max(0, period - 5) * 4
        dependency = max(0.0, dependency + 0.012 * symptomatic_reliance - 0.018 * repair_investment)
        rows.append(
            {
                "period": period,
                "symptomatic_reliance": symptomatic_reliance,
                "repair_investment": repair_investment,
                "dependency": round(dependency, 3),
            }
        )

    OUTPUT_PATH.parent.mkdir(parents=True, exist_ok=True)
    with OUTPUT_PATH.open("w", newline="", encoding="utf-8") as handle:
        writer = csv.DictWriter(handle, fieldnames=list(rows[0].keys()))
        writer.writeheader()
        writer.writerows(rows)

    print("Dependency loop simulation")
    for row in rows:
        print(row)


if __name__ == "__main__":
    main()
