"""Demonstrate how averages can hide level-specific variation."""

from __future__ import annotations

import csv
from pathlib import Path

DATA = Path(__file__).resolve().parents[1] / "data" / "synthetic_system_entities.csv"


def load_entities() -> list[dict[str, str]]:
    with DATA.open(newline="", encoding="utf-8") as handle:
        return list(csv.DictReader(handle))


def main() -> None:
    rows = load_entities()
    capacities = [float(row["baseline_capacity"]) for row in rows]
    exposures = [float(row["risk_exposure"]) for row in rows]
    print(f"average_capacity,{sum(capacities) / len(capacities):.2f}")
    print(f"average_risk_exposure,{sum(exposures) / len(exposures):.2f}")
    print("highest_risk_entity," + max(rows, key=lambda row: float(row["risk_exposure"]))["entity_name"])
    print("lowest_capacity_entity," + min(rows, key=lambda row: float(row["baseline_capacity"]))["entity_name"])


if __name__ == "__main__":
    main()
