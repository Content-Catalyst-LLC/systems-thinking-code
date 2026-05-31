"""Scenario comparison for a synthetic system dynamics model."""

from __future__ import annotations

import csv
from pathlib import Path

from system_dynamics_baseline_model import Parameters, simulate


def load_scenarios(path: Path) -> list[dict[str, str]]:
    with path.open() as f:
        return list(csv.DictReader(f))


def run_scenario(row: dict[str, str]) -> list[dict[str, float | str]]:
    params = Parameters(
        demand_growth_rate=float(row["demand_growth_rate"]),
        hiring_rate=1.8 + float(row["capacity_investment_rate"]) * 20,
        turnover_rate=max(0.4, 1.0 - float(row["policy_strength"]) * 0.25),
    )
    results = simulate(params)
    for item in results:
        item["scenario_id"] = row["scenario_id"]
        item["scenario_name"] = row["scenario_name"]
    return results


if __name__ == "__main__":
    article_dir = Path(__file__).resolve().parents[1]
    scenarios = load_scenarios(article_dir / "data" / "synthetic_scenarios.csv")
    output = article_dir / "outputs" / "tables" / "scenario_comparison_python.csv"
    output.parent.mkdir(parents=True, exist_ok=True)
    rows = [item for scenario in scenarios for item in run_scenario(scenario)]
    with output.open("w", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=list(rows[0].keys()))
        writer.writeheader()
        writer.writerows(rows)
    print(f"Wrote {output}")
