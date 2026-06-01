"""
Scenario comparison for a simplified institutional system.

The model is intentionally simple and synthetic.
"""

from __future__ import annotations

import csv
from pathlib import Path


DATA_DIR = Path(__file__).resolve().parents[1] / "data"
SCENARIO_PATH = DATA_DIR / "synthetic_scenarios.csv"


def load_scenarios() -> list[dict[str, str]]:
    with SCENARIO_PATH.open(newline="", encoding="utf-8") as handle:
        return list(csv.DictReader(handle))


def run_scenario(scenario: dict[str, str], periods: int = 12) -> dict[str, float | str]:
    trust = 62.0
    capacity = 55.0
    demand = 70.0
    delay = 14.0
    resilience = 40.0

    resource_multiplier = float(scenario["resource_multiplier"])
    demand_multiplier = float(scenario["demand_multiplier"])
    delay_multiplier = float(scenario["delay_multiplier"])
    shock_period = int(scenario["shock_period"])
    shock_size = float(scenario["shock_size"])

    for period in range(1, periods + 1):
        current_demand = demand * demand_multiplier
        if shock_period and period >= shock_period:
            current_demand += shock_size
        capacity += (resource_multiplier * 2.0) - (current_demand / 100.0)
        delay = max(1.0, delay * delay_multiplier + (current_demand - capacity) / 80.0)
        trust += (capacity / 100.0) - (delay / 20.0)
        resilience += (capacity / 120.0) - (current_demand / 150.0)

    return {
        "scenario_id": scenario["scenario_id"],
        "scenario_name": scenario["scenario_name"],
        "final_trust": round(trust, 2),
        "final_capacity": round(capacity, 2),
        "final_delay": round(delay, 2),
        "final_resilience": round(resilience, 2),
    }


def main() -> None:
    print("scenario_id,scenario_name,final_trust,final_capacity,final_delay,final_resilience")
    for scenario in load_scenarios():
        result = run_scenario(scenario)
        print(
            f"{result['scenario_id']},{result['scenario_name']},"
            f"{result['final_trust']},{result['final_capacity']},"
            f"{result['final_delay']},{result['final_resilience']}"
        )


if __name__ == "__main__":
    main()
