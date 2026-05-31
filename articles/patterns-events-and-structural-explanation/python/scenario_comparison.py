"""
Scenario comparison for event-pattern-structure dynamics.
"""

from __future__ import annotations

import csv
from pathlib import Path

SCENARIO_PATH = Path(__file__).resolve().parents[1] / "data" / "synthetic_scenarios.csv"


def load_scenarios() -> list[dict[str, str]]:
    with SCENARIO_PATH.open(newline="", encoding="utf-8") as handle:
        return list(csv.DictReader(handle))


def run_scenario(scenario: dict[str, str], periods: int = 12) -> dict[str, float | str]:
    trust = 62.0
    capacity = 55.0
    backlog = 120.0
    structural_risk = 52.0

    capacity_multiplier = float(scenario["capacity_multiplier"])
    backlog_multiplier = float(scenario["backlog_multiplier"])
    trust_repair_rate = float(scenario["trust_repair_rate"])
    shock_period = int(scenario["shock_period"])
    shock_size = float(scenario["shock_size"])

    for period in range(1, periods + 1):
        shock = shock_size if shock_period and period >= shock_period else 0.0
        capacity += (2.0 * capacity_multiplier) - (backlog / 150.0)
        backlog += (5.0 * backlog_multiplier) + shock / 10.0 - (capacity / 20.0)
        structural_risk += (backlog / 200.0) - (capacity / 120.0)
        trust += trust_repair_rate - (structural_risk / 120.0)

    return {
        "scenario_id": scenario["scenario_id"],
        "scenario_name": scenario["scenario_name"],
        "final_trust": round(trust, 2),
        "final_capacity": round(capacity, 2),
        "final_backlog": round(backlog, 2),
        "final_structural_risk": round(structural_risk, 2),
    }


def main() -> None:
    print("scenario_id,scenario_name,final_trust,final_capacity,final_backlog,final_structural_risk")
    for scenario in load_scenarios():
        row = run_scenario(scenario)
        print(
            f"{row['scenario_id']},{row['scenario_name']},{row['final_trust']},"
            f"{row['final_capacity']},{row['final_backlog']},{row['final_structural_risk']}"
        )


if __name__ == "__main__":
    main()
