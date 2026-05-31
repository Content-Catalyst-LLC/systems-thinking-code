"""Scenario comparison for reinforcing and balancing dynamics."""

from __future__ import annotations

import csv
from pathlib import Path

DATA = Path(__file__).resolve().parents[1] / "data" / "synthetic_scenarios.csv"


def run_scenario(row: dict[str, str], periods: int = 20) -> float:
    value = 10.0
    rate = float(row["growth_rate"])
    correction = float(row["correction_strength"])
    capacity = float(row["carrying_capacity"])
    for _ in range(periods):
        reinforcing = rate * value
        balancing = correction * (value / capacity) * value
        value = value + reinforcing - balancing
    return round(value, 4)


def main() -> None:
    with DATA.open(newline="", encoding="utf-8") as handle:
        rows = list(csv.DictReader(handle))
    print("scenario_id,scenario_name,final_value")
    for row in rows:
        print(f"{row['scenario_id']},{row['scenario_name']},{run_scenario(row)}")


if __name__ == "__main__":
    main()
