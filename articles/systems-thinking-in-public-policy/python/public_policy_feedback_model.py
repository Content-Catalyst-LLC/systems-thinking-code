"""Python Workflow: Policy Feedback, Administrative Burden, and Scenario Modeling."""
from __future__ import annotations
from dataclasses import dataclass
from pathlib import Path
import csv

ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "data"
OUT = ROOT / "outputs" / "tables"
OUT.mkdir(parents=True, exist_ok=True)

@dataclass
class PolicyScenario:
    name: str
    initial_outcome: float
    initial_trust: float
    initial_capacity: float
    policy_effort: float
    burden_level: float
    capacity_investment: float
    feedback_closure: float
    enforcement_intensity: float
    distribution_gap: float


def clamp(value: float, low: float = 0.0, high: float = 100.0) -> float:
    return max(low, min(high, value))


def load_scenarios() -> list[PolicyScenario]:
    scenarios: list[PolicyScenario] = []
    with (DATA / "synthetic_policy_scenarios.csv").open(newline="", encoding="utf-8") as handle:
        for row in csv.DictReader(handle):
            scenarios.append(PolicyScenario(
                name=row["scenario"],
                initial_outcome=float(row["initial_outcome"]),
                initial_trust=float(row["initial_trust"]),
                initial_capacity=float(row["initial_capacity"]),
                policy_effort=float(row["policy_effort"]),
                burden_level=float(row["burden_level"]),
                capacity_investment=float(row["capacity_investment"]),
                feedback_closure=float(row["feedback_closure"]),
                enforcement_intensity=float(row["enforcement_intensity"]),
                distribution_gap=float(row["distribution_gap"]),
            ))
    return scenarios


def run_policy_scenario(scenario: PolicyScenario, years: int = 20) -> list[dict[str, float | int | str]]:
    outcome = scenario.initial_outcome
    trust = scenario.initial_trust
    capacity = scenario.initial_capacity
    rows: list[dict[str, float | int | str]] = []

    for year in range(years + 1):
        access_penalty = scenario.burden_level * 0.22
        capacity = clamp(capacity + scenario.capacity_investment - (scenario.burden_level * 0.04))
        learning_gain = scenario.feedback_closure * 4.0
        enforcement_gain = scenario.enforcement_intensity * 1.3
        enforcement_trust_cost = scenario.enforcement_intensity * scenario.burden_level * 0.03
        equity_penalty = scenario.distribution_gap * 0.18

        outcome_change = (
            scenario.policy_effort * 0.35
            + capacity * 0.06
            + learning_gain
            + enforcement_gain
            - access_penalty
            - equity_penalty
        ) / 6.0

        trust_change = (
            scenario.feedback_closure * 1.8
            + capacity * 0.015
            - scenario.burden_level * 0.10
            - enforcement_trust_cost / 20.0
            - scenario.distribution_gap * 0.04
        ) / 2.0

        outcome = clamp(outcome + outcome_change)
        trust = clamp(trust + trust_change)

        rows.append({
            "year": year,
            "scenario": scenario.name,
            "policy_outcome": round(outcome, 2),
            "public_trust": round(trust, 2),
            "implementation_capacity": round(capacity, 2),
            "administrative_burden": round(scenario.burden_level, 2),
            "feedback_closure": round(scenario.feedback_closure, 2),
            "distribution_gap": round(scenario.distribution_gap, 2),
            "enforcement_intensity": round(scenario.enforcement_intensity, 2),
        })
    return rows


def main() -> None:
    rows: list[dict[str, float | int | str]] = []
    for scenario in load_scenarios():
        rows.extend(run_policy_scenario(scenario))

    result_fields = [
        "year", "scenario", "policy_outcome", "public_trust", "implementation_capacity",
        "administrative_burden", "feedback_closure", "distribution_gap", "enforcement_intensity"
    ]
    with (OUT / "public_policy_scenario_results.csv").open("w", newline="", encoding="utf-8") as handle:
        writer = csv.DictWriter(handle, fieldnames=result_fields)
        writer.writeheader()
        writer.writerows(rows)

    summary_rows = []
    for scenario in sorted({str(row["scenario"]) for row in rows}):
        scenario_rows = [row for row in rows if row["scenario"] == scenario]
        last = scenario_rows[-1]
        summary_rows.append({
            "scenario": scenario,
            "final_outcome": last["policy_outcome"],
            "final_trust": last["public_trust"],
            "final_capacity": last["implementation_capacity"],
            "average_burden": round(sum(float(r["administrative_burden"]) for r in scenario_rows) / len(scenario_rows), 2),
            "average_feedback_closure": round(sum(float(r["feedback_closure"]) for r in scenario_rows) / len(scenario_rows), 2),
            "average_distribution_gap": round(sum(float(r["distribution_gap"]) for r in scenario_rows) / len(scenario_rows), 2),
        })

    with (OUT / "public_policy_scenario_summary.csv").open("w", newline="", encoding="utf-8") as handle:
        writer = csv.DictWriter(handle, fieldnames=list(summary_rows[0].keys()))
        writer.writeheader()
        writer.writerows(summary_rows)

    print(f"Wrote {OUT / 'public_policy_scenario_results.csv'}")
    print(f"Wrote {OUT / 'public_policy_scenario_summary.csv'}")


if __name__ == "__main__":
    main()
