"""AI and technology systems scenario model.

Standard-library workflow for modeling feedback loops, group-level harm,
model drift, automation burden, human review, governance readiness,
contestability, and public trust.
"""

from __future__ import annotations

from dataclasses import dataclass
from pathlib import Path
import csv
from statistics import mean

ROOT = Path(__file__).resolve().parents[1]
TABLES = ROOT / "outputs" / "tables"


@dataclass(frozen=True)
class AIScenario:
    name: str
    periods: int
    base_accuracy: float
    group_gap: float
    feedback_strength: float
    drift_rate: float
    automation_level: float
    human_review_capacity: float
    appeal_access: float
    monitoring_strength: float
    remedy_strength: float
    vulnerability_weight: float


def clamp(value: float, low: float = 0.0, high: float = 100.0) -> float:
    return max(low, min(high, value))


def run_scenario(scenario: AIScenario) -> list[dict[str, object]]:
    drift = 0.0
    feedback_bias = scenario.group_gap
    documentation_quality = 45.0 + scenario.monitoring_strength * 25.0
    rows: list[dict[str, object]] = []

    for period in range(scenario.periods + 1):
        drift = clamp(drift + scenario.drift_rate * (1.0 - scenario.monitoring_strength * 0.35))
        feedback_bias = clamp(
            feedback_bias
            + scenario.feedback_strength * scenario.automation_level * 2.0
            - scenario.monitoring_strength * 0.70
            - scenario.remedy_strength * 0.55
        )

        base_error = clamp(100.0 - scenario.base_accuracy + drift * 0.18)
        group_a_error = clamp(base_error)
        group_b_error = clamp(base_error + feedback_bias * 0.35 + scenario.vulnerability_weight * 0.10)
        false_positive_gap = clamp(group_b_error - group_a_error)
        false_negative_gap = clamp(feedback_bias * 0.25 + drift * 0.08)

        automation_burden = clamp(
            scenario.automation_level * 55.0
            - scenario.human_review_capacity * 18.0
            - scenario.appeal_access * 16.0
            + drift * 0.10
        )
        human_review_backlog = clamp(
            scenario.automation_level * 45.0
            + group_b_error * 0.25
            - scenario.human_review_capacity * 38.0
        )
        contestability_index = clamp(
            scenario.appeal_access * 45.0
            + scenario.human_review_capacity * 30.0
            + scenario.remedy_strength * 25.0
            - automation_burden * 0.20
        )
        governance_readiness = clamp(
            documentation_quality * 0.22
            + scenario.monitoring_strength * 28.0
            + scenario.remedy_strength * 24.0
            + scenario.appeal_access * 18.0
            + scenario.human_review_capacity * 12.0
        )
        ai_system_risk = clamp(
            group_b_error * 0.24
            + false_positive_gap * 0.20
            + false_negative_gap * 0.16
            + drift * 0.16
            + automation_burden * 0.14
            + human_review_backlog * 0.10
            - governance_readiness * 0.20
        )
        public_trust = clamp(
            78.0
            - ai_system_risk * 0.45
            - automation_burden * 0.18
            + contestability_index * 0.20
            + scenario.remedy_strength * 8.0
        )

        rows.append({
            "period": period,
            "scenario": scenario.name,
            "drift_index": round(drift, 3),
            "feedback_bias_index": round(feedback_bias, 3),
            "group_a_error": round(group_a_error, 3),
            "group_b_error": round(group_b_error, 3),
            "false_positive_gap": round(false_positive_gap, 3),
            "false_negative_gap": round(false_negative_gap, 3),
            "automation_burden": round(automation_burden, 3),
            "human_review_backlog": round(human_review_backlog, 3),
            "contestability_index": round(contestability_index, 3),
            "governance_readiness": round(governance_readiness, 3),
            "ai_system_risk": round(ai_system_risk, 3),
            "public_trust": round(public_trust, 3),
        })
    return rows


def scenarios() -> list[AIScenario]:
    return [
        AIScenario("Unmanaged automation", 36, 82.0, 18.0, 0.62, 2.2, 0.86, 0.20, 0.15, 0.10, 0.08, 55.0),
        AIScenario("Biased feedback loop", 36, 84.0, 24.0, 0.78, 1.8, 0.78, 0.28, 0.18, 0.18, 0.12, 62.0),
        AIScenario("Monitored deployment", 36, 85.0, 14.0, 0.34, 1.4, 0.58, 0.58, 0.52, 0.68, 0.48, 42.0),
        AIScenario("Accountable human-centered governance", 36, 86.0, 10.0, 0.22, 1.1, 0.42, 0.78, 0.82, 0.84, 0.78, 34.0),
    ]


def write_csv(path: Path, rows: list[dict[str, object]]) -> None:
    if not rows:
        raise ValueError(f"No rows to write for {path}")
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", newline="", encoding="utf-8") as handle:
        writer = csv.DictWriter(handle, fieldnames=list(rows[0].keys()))
        writer.writeheader()
        writer.writerows(rows)


def summarize(rows: list[dict[str, object]]) -> list[dict[str, object]]:
    names = sorted({str(row["scenario"]) for row in rows})
    summary: list[dict[str, object]] = []
    for name in names:
        subset = [row for row in rows if row["scenario"] == name]
        final = subset[-1]
        average_risk = mean(float(row["ai_system_risk"]) for row in subset)
        max_gap = max(float(row["false_positive_gap"]) for row in subset)
        max_backlog = max(float(row["human_review_backlog"]) for row in subset)
        min_trust = min(float(row["public_trust"]) for row in subset)
        summary.append({
            "scenario": name,
            "final_ai_system_risk": final["ai_system_risk"],
            "average_ai_system_risk": round(average_risk, 3),
            "maximum_false_positive_gap": round(max_gap, 3),
            "maximum_human_review_backlog": round(max_backlog, 3),
            "minimum_public_trust": round(min_trust, 3),
            "final_governance_readiness": final["governance_readiness"],
            "final_contestability_index": final["contestability_index"],
            "diagnostic": (
                "high-risk AI system" if average_risk >= 45 or max_gap >= 25 else
                "moderate risk requiring stronger governance" if average_risk >= 28 or max_backlog >= 35 else
                "comparatively accountable AI pathway"
            )
        })
    return summary


def main() -> None:
    all_rows: list[dict[str, object]] = []
    for scenario in scenarios():
        all_rows.extend(run_scenario(scenario))
    summary = summarize(all_rows)
    write_csv(TABLES / "ai_technology_systems_timeseries.csv", all_rows)
    write_csv(TABLES / "ai_technology_systems_summary.csv", summary)
    print("\nAI and technology systems scenario summary:")
    for row in summary:
        print(f"{row['scenario']}: avg risk={row['average_ai_system_risk']}, max FP gap={row['maximum_false_positive_gap']}, diagnostic={row['diagnostic']}")


if __name__ == "__main__":
    main()
