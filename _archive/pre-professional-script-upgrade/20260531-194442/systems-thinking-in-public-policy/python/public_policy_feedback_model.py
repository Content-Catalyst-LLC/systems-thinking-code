"""Professional synthetic policy scenario model.

Models public-policy outcomes as a dynamic interaction among policy effort,
administrative burden, implementation capacity, public trust, enforcement,
feedback closure, and distributional gaps.
"""
from __future__ import annotations

from dataclasses import dataclass
from _policy_utils import DATA, OUT_TABLES, clamp, ensure_outputs, read_csv_dict, to_float, write_csv_dict

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


def load_scenarios() -> list[PolicyScenario]:
    rows = read_csv_dict(
        DATA / "synthetic_policy_scenarios.csv",
        ["scenario", "initial_outcome", "initial_trust", "initial_capacity", "policy_effort", "burden_level", "capacity_investment", "feedback_closure", "enforcement_intensity", "distribution_gap"],
    )
    return [
        PolicyScenario(
            name=row["scenario"],
            initial_outcome=to_float(row, "initial_outcome"),
            initial_trust=to_float(row, "initial_trust"),
            initial_capacity=to_float(row, "initial_capacity"),
            policy_effort=to_float(row, "policy_effort"),
            burden_level=to_float(row, "burden_level"),
            capacity_investment=to_float(row, "capacity_investment"),
            feedback_closure=to_float(row, "feedback_closure"),
            enforcement_intensity=to_float(row, "enforcement_intensity"),
            distribution_gap=to_float(row, "distribution_gap"),
        )
        for row in rows
    ]


def diagnostic_label(outcome: float, trust: float, distribution_gap: float) -> str:
    if outcome >= 80 and trust >= 70 and distribution_gap <= 20:
        return "strong public-value trajectory"
    if outcome >= 65 and trust >= 55:
        return "improving but monitor burden and equity"
    if outcome >= 50 and trust < 55:
        return "technical improvement with legitimacy risk"
    return "weak or fragile trajectory"


def run_policy_scenario(scenario: PolicyScenario, years: int = 20) -> list[dict]:
    outcome = scenario.initial_outcome
    trust = scenario.initial_trust
    capacity = scenario.initial_capacity
    rows: list[dict] = []

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
    ensure_outputs()
    scenario_results: list[dict] = []
    for scenario in load_scenarios():
        scenario_results.extend(run_policy_scenario(scenario))

    write_csv_dict(OUT_TABLES / "public_policy_scenario_results.csv", scenario_results)

    summary_rows: list[dict] = []
    for scenario_name in sorted({row["scenario"] for row in scenario_results}):
        rows = [row for row in scenario_results if row["scenario"] == scenario_name]
        last = rows[-1]
        avg_burden = sum(float(row["administrative_burden"]) for row in rows) / len(rows)
        avg_closure = sum(float(row["feedback_closure"]) for row in rows) / len(rows)
        avg_gap = sum(float(row["distribution_gap"]) for row in rows) / len(rows)
        summary_rows.append({
            "scenario": scenario_name,
            "final_outcome": last["policy_outcome"],
            "final_trust": last["public_trust"],
            "final_capacity": last["implementation_capacity"],
            "average_burden": round(avg_burden, 2),
            "average_feedback_closure": round(avg_closure, 2),
            "average_distribution_gap": round(avg_gap, 2),
            "diagnostic": diagnostic_label(float(last["policy_outcome"]), float(last["public_trust"]), avg_gap),
        })

    write_csv_dict(OUT_TABLES / "public_policy_scenario_summary.csv", summary_rows)
    print(f"Wrote {OUT_TABLES / 'public_policy_scenario_results.csv'}")
    print(f"Wrote {OUT_TABLES / 'public_policy_scenario_summary.csv'}")

if __name__ == "__main__":
    main()
