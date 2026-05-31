#!/usr/bin/env python3
"""Compare relief-only, delayed-repair, and relief-plus-repair paths."""

from __future__ import annotations

from pathlib import Path
import csv

ARTICLE_DIR = Path(__file__).resolve().parents[1]
OUTPUT_PATH = ARTICLE_DIR / "outputs" / "tables" / "relief_plus_repair_scenarios.csv"


def simulate(name: str, repair_schedule: list[float], relief_schedule: list[float]) -> list[dict[str, float | str]]:
    pressure = 80.0
    capacity = 55.0
    dependency = 0.3
    rows: list[dict[str, float | str]] = []

    for period, (repair, relief) in enumerate(zip(repair_schedule, relief_schedule)):
        capacity = max(0.0, capacity + 0.7 * repair - 0.25 * relief)
        dependency = max(0.0, dependency + 0.015 * relief - 0.012 * repair)
        pressure = max(0.0, pressure + 4.0 - 0.4 * relief - 0.25 * capacity)
        rows.append(
            {
                "scenario": name,
                "period": period,
                "problem_pressure": round(pressure, 2),
                "capacity": round(capacity, 2),
                "dependency": round(dependency, 3),
            }
        )

    return rows


def main() -> None:
    periods = 12
    scenarios = []
    scenarios.extend(simulate("relief_only", [4] * periods, [42] * periods))
    scenarios.extend(simulate("delayed_repair", [4] * 5 + [18] * 7, [38] * periods))
    scenarios.extend(simulate("relief_plus_repair", [20] * periods, [30, 28, 26, 24, 22, 20, 18, 16, 14, 12, 10, 8]))

    OUTPUT_PATH.parent.mkdir(parents=True, exist_ok=True)
    with OUTPUT_PATH.open("w", newline="", encoding="utf-8") as handle:
        writer = csv.DictWriter(handle, fieldnames=list(scenarios[0].keys()))
        writer.writeheader()
        writer.writerows(scenarios)

    print(f"Wrote {len(scenarios)} scenario rows to {OUTPUT_PATH}")


if __name__ == "__main__":
    main()
