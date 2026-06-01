"""Simple comparison of early and late policy timing scenarios."""

from __future__ import annotations

import csv
from pathlib import Path

SCENARIOS = Path(__file__).resolve().parents[1] / "data" / "synthetic_scenarios.csv"


def run_scenario(row: dict[str, str], periods: int = 14) -> dict[str, float | str]:
    risk = 42.0
    capacity = 58.0
    delay_multiplier = float(row["delay_multiplier"])
    capacity_investment = float(row["capacity_investment"])
    shock_period = int(row["shock_period"])
    shock_size = float(row["shock_size"])

    for period in range(1, periods + 1):
        if shock_period and period >= shock_period:
            risk += shock_size / 10
        capacity += capacity_investment / periods
        risk += 2.5 * delay_multiplier - capacity / 45
        risk = max(0, risk)

    return {
        "scenario_id": row["scenario_id"],
        "scenario_name": row["scenario_name"],
        "final_risk": round(risk, 2),
        "final_capacity": round(capacity, 2),
    }


def main() -> None:
    with SCENARIOS.open(newline="", encoding="utf-8") as handle:
        scenarios = list(csv.DictReader(handle))

    print("scenario_id,scenario_name,final_risk,final_capacity")
    for scenario in scenarios:
        result = run_scenario(scenario)
        print(f"{result['scenario_id']},{result['scenario_name']},{result['final_risk']},{result['final_capacity']}")


if __name__ == "__main__":
    main()
