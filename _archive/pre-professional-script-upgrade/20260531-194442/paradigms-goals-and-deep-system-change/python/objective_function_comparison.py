#!/usr/bin/env python3
"""Compare narrow and broader objective functions using synthetic scenario data."""

from __future__ import annotations

from pathlib import Path
import csv

ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "data" / "synthetic_scenario_outputs.csv"
OUT = ROOT / "outputs" / "tables" / "objective_function_comparison.csv"
OUT.parent.mkdir(parents=True, exist_ok=True)

OBJECTIVES = {
    "narrow_throughput": {"throughput": 1.0, "access": 0.1, "dignity": 0.05, "resilience": 0.05, "burden": -0.1, "harm": -0.1},
    "access_dignity": {"throughput": 0.45, "access": 0.9, "dignity": 0.85, "resilience": 0.6, "burden": -0.8, "harm": -0.9},
    "resilience_repair": {"throughput": 0.35, "access": 0.65, "dignity": 0.7, "resilience": 0.95, "burden": -0.85, "harm": -0.95},
}


def weighted_score(row: dict[str, str], weights: dict[str, float]) -> float:
    return round(sum(float(row[key]) * weight for key, weight in weights.items()), 3)


def main() -> None:
    with DATA.open(newline="", encoding="utf-8") as handle:
        rows = list(csv.DictReader(handle))

    output_rows: list[dict[str, object]] = []
    for row in rows:
        for objective_name, weights in OBJECTIVES.items():
            output_rows.append({
                "scenario_id": row["scenario_id"],
                "scenario_name": row["scenario_name"],
                "year": row["year"],
                "objective": objective_name,
                "objective_score": weighted_score(row, weights),
            })

    with OUT.open("w", newline="", encoding="utf-8") as handle:
        writer = csv.DictWriter(handle, fieldnames=list(output_rows[0].keys()))
        writer.writeheader()
        writer.writerows(output_rows)
    print(f"Wrote {OUT}")


if __name__ == "__main__":
    main()
