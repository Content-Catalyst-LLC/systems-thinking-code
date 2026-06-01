"""
Counterfactual scenario analysis for systems causality.
"""

from __future__ import annotations

import csv
from pathlib import Path

DATA_PATH = Path(__file__).resolve().parents[1] / "data" / "synthetic_counterfactuals.csv"


def load_counterfactuals() -> list[dict[str, str]]:
    with DATA_PATH.open(newline="", encoding="utf-8") as handle:
        return list(csv.DictReader(handle))


def run_counterfactual(row: dict[str, str], periods: int = 12) -> dict[str, float | str]:
    trust = 64.0
    capacity = 58.0
    demand = 70.0
    backlog = 100.0 - float(row["backlog_reduction"])

    resource_multiplier = float(row["resource_multiplier"])
    demand_multiplier = float(row["demand_multiplier"])
    delay_multiplier = float(row["delay_multiplier"])
    threshold = float(row["threshold_level"])

    for _ in range(periods):
        demand_now = demand * demand_multiplier
        capacity += 1.8 * resource_multiplier - (backlog / 200.0)
        delay = max(1.0, (demand_now / max(capacity, 1.0)) * 10.0 * delay_multiplier)
        backlog += demand_now * 0.15 - capacity * 0.10
        trust += (capacity / 140.0) - (delay / 18.0)

    threshold_crossed = 1 if backlog > threshold else 0

    return {
        "counterfactual_id": row["counterfactual_id"],
        "name": row["name"],
        "final_trust": round(trust, 2),
        "final_capacity": round(capacity, 2),
        "final_backlog": round(backlog, 2),
        "threshold_crossed": threshold_crossed,
    }


def main() -> None:
    print("counterfactual_id,name,final_trust,final_capacity,final_backlog,threshold_crossed")
    for row in load_counterfactuals():
        result = run_counterfactual(row)
        print(
            f"{result['counterfactual_id']},{result['name']},"
            f"{result['final_trust']},{result['final_capacity']},"
            f"{result['final_backlog']},{result['threshold_crossed']}"
        )


if __name__ == "__main__":
    main()
