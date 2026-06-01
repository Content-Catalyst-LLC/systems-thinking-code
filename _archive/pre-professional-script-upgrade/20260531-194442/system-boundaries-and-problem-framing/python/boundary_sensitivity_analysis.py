"""
Boundary sensitivity analysis for "System Boundaries and Problem Framing".

This script compares how net assessment changes under different system boundaries.
It uses synthetic data and the Python standard library only.
"""

from __future__ import annotations

import csv
from pathlib import Path


DATA_PATH = Path(__file__).resolve().parents[1] / "data" / "synthetic_indicators.csv"


def load_rows(path: Path = DATA_PATH) -> list[dict[str, str]]:
    with path.open(newline="", encoding="utf-8") as handle:
        return list(csv.DictReader(handle))


def calculate_net_value(row: dict[str, str], external_cost_weight: float = 1.0) -> float:
    measured_value = float(row["measured_value"])
    internal_cost = float(row["internal_cost"])
    external_cost = float(row["external_cost"])
    return measured_value - internal_cost - (external_cost_weight * external_cost)


def main() -> None:
    print("boundary_id,net_value_external_weight_0_25,net_value_external_weight_1_00")
    for row in load_rows():
        narrow_score = calculate_net_value(row, external_cost_weight=0.25)
        broad_score = calculate_net_value(row, external_cost_weight=1.00)
        print(f"{row['boundary_id']},{round(narrow_score, 2)},{round(broad_score, 2)}")


if __name__ == "__main__":
    main()
