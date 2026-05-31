"""
Cross-scale scenario analysis.

Compares scenarios that use different boundary and frame assumptions.
"""

from __future__ import annotations

import csv
from pathlib import Path


DATA_DIR = Path(__file__).resolve().parents[1] / "data"
SCENARIOS_PATH = DATA_DIR / "synthetic_scenarios.csv"
INDICATORS_PATH = DATA_DIR / "synthetic_indicators.csv"


def load_by_key(path: Path, key: str) -> dict[str, dict[str, str]]:
    with path.open(newline="", encoding="utf-8") as handle:
        return {row[key]: row for row in csv.DictReader(handle)}


def main() -> None:
    indicators = load_by_key(INDICATORS_PATH, "boundary_id")

    print("scenario_id,scenario_name,boundary_id,adjusted_score")
    with SCENARIOS_PATH.open(newline="", encoding="utf-8") as handle:
        for scenario in csv.DictReader(handle):
            boundary = indicators[scenario["boundary_id"]]
            measured_value = float(boundary["measured_value"])
            internal_cost = float(boundary["internal_cost"])
            external_cost = float(boundary["external_cost"])
            stakeholder_ratio = float(boundary["stakeholder_inclusion_ratio"])
            resilience = float(boundary["resilience_score"])

            adjusted_score = (
                measured_value
                - internal_cost * float(scenario["internal_cost_weight"])
                - external_cost * float(scenario["external_cost_weight"])
                + stakeholder_ratio * 50000 * float(scenario["stakeholder_weight"])
                + resilience * 500
            )

            print(
                f"{scenario['scenario_id']},{scenario['scenario_name']},"
                f"{scenario['boundary_id']},{round(adjusted_score, 2)}"
            )


if __name__ == "__main__":
    main()
