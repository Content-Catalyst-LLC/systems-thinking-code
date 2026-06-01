#!/usr/bin/env python3
"""
Dependency-light professional workflow for Donella Meadows and structural insight.

Purpose:
- Simulate overshoot, delayed feedback, leverage quality, trust, institutional learning,
  equity alignment, self-organization, and resilience.
- Use only Python standard library.
- Write outputs relative to the article root, no matter where the script is launched.
"""

from __future__ import annotations

from dataclasses import dataclass
from pathlib import Path
import csv
from statistics import mean

ARTICLE_ROOT = Path(__file__).resolve().parents[1]
OUTPUT_TABLES = ARTICLE_ROOT / "outputs" / "tables"


@dataclass
class MeadowsScenario:
    name: str
    periods: int
    initial_resource_stock: float
    initial_trust_stock: float
    consumption_pressure: float
    regeneration_capacity: float
    feedback_delay: int
    information_quality: float
    rule_change_strength: float
    goal_alignment: float
    paradigm_shift_capacity: float
    self_organization_capacity: float
    equity_alignment: float


def ensure_outputs() -> None:
    OUTPUT_TABLES.mkdir(parents=True, exist_ok=True)
    (ARTICLE_ROOT / "outputs" / "figures").mkdir(parents=True, exist_ok=True)


def clamp(value: float, low: float = 0.0, high: float = 100.0) -> float:
    return max(low, min(high, value))


def delayed_value(series: list[float], delay: int) -> float:
    if len(series) <= delay:
        return series[0]
    return series[-delay - 1]


def run_scenario(scenario: MeadowsScenario) -> list[dict[str, object]]:
    resource_stock = scenario.initial_resource_stock
    trust_stock = scenario.initial_trust_stock
    institutional_learning = 35.0
    resilience_capacity = 42.0
    resource_history = [resource_stock]
    rows: list[dict[str, object]] = []

    for period in range(scenario.periods + 1):
        perceived_resource = delayed_value(resource_history, scenario.feedback_delay)
        scarcity_signal = clamp(100.0 - perceived_resource)

        leverage_quality = clamp(
            scenario.information_quality * 18.0
            + scenario.rule_change_strength * 20.0
            + scenario.goal_alignment * 22.0
            + scenario.paradigm_shift_capacity * 24.0
            + scenario.self_organization_capacity * 16.0
        )

        corrective_response = clamp(
            scenario.information_quality * scarcity_signal * 0.24
            + scenario.rule_change_strength * 10.0
            + scenario.goal_alignment * 8.0
            + institutional_learning * 0.10
        )

        consumption_flow = clamp(
            scenario.consumption_pressure * 9.0
            + max(0.0, 70.0 - resource_stock) * 0.04
            - corrective_response * 0.12
            - scenario.paradigm_shift_capacity * 2.0
        )

        regeneration_flow = clamp(
            scenario.regeneration_capacity * 6.0
            + resilience_capacity * 0.05
            + scenario.self_organization_capacity * 1.4
            + scenario.equity_alignment * 1.1
        )

        resource_stock = clamp(resource_stock - consumption_flow + regeneration_flow)

        institutional_learning = clamp(
            institutional_learning
            + scenario.information_quality * 1.5
            + scenario.self_organization_capacity * 1.7
            + scenario.paradigm_shift_capacity * 1.4
            - max(0.0, 45.0 - resource_stock) * 0.04
        )

        trust_stock = clamp(
            trust_stock
            + scenario.equity_alignment * 1.8
            + scenario.information_quality * 1.2
            + scenario.rule_change_strength * 1.0
            - max(0.0, 55.0 - resource_stock) * 0.08
            - max(0.0, consumption_flow - regeneration_flow) * 0.10
        )

        resilience_capacity = clamp(
            resilience_capacity
            + regeneration_flow * 0.08
            + institutional_learning * 0.04
            + scenario.self_organization_capacity * 1.3
            - consumption_flow * 0.05
        )

        overshoot_index = clamp(max(0.0, consumption_flow - regeneration_flow) * 5.0 + scarcity_signal * 0.35)

        structural_insight_score = clamp(
            leverage_quality * 0.34
            + institutional_learning * 0.22
            + trust_stock * 0.16
            + resilience_capacity * 0.18
            + scenario.equity_alignment * 10.0
            - overshoot_index * 0.18
        )

        rows.append(
            {
                "period": period,
                "scenario": scenario.name,
                "resource_stock": round(resource_stock, 3),
                "perceived_resource_stock": round(perceived_resource, 3),
                "consumption_flow": round(consumption_flow, 3),
                "regeneration_flow": round(regeneration_flow, 3),
                "overshoot_index": round(overshoot_index, 3),
                "leverage_quality": round(leverage_quality, 3),
                "trust_stock": round(trust_stock, 3),
                "institutional_learning_stock": round(institutional_learning, 3),
                "resilience_capacity": round(resilience_capacity, 3),
                "structural_insight_score": round(structural_insight_score, 3),
            }
        )

        resource_history.append(resource_stock)

    return rows


def write_csv(path: Path, rows: list[dict[str, object]]) -> None:
    if not rows:
        raise ValueError(f"No rows to write for {path}")
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", newline="", encoding="utf-8") as handle:
        writer = csv.DictWriter(handle, fieldnames=list(rows[0].keys()))
        writer.writeheader()
        writer.writerows(rows)


def summarize(rows: list[dict[str, object]]) -> list[dict[str, object]]:
    summary: list[dict[str, object]] = []

    for scenario_name in sorted({str(row["scenario"]) for row in rows}):
        subset = [row for row in rows if row["scenario"] == scenario_name]
        final = subset[-1]
        avg_resource = mean(float(row["resource_stock"]) for row in subset)
        avg_overshoot = mean(float(row["overshoot_index"]) for row in subset)
        avg_insight = mean(float(row["structural_insight_score"]) for row in subset)
        min_resource = min(float(row["resource_stock"]) for row in subset)

        if float(final["resource_stock"]) >= 60 and avg_overshoot <= 20 and avg_insight >= 60:
            diagnostic = "structural leverage pathway"
        elif avg_overshoot >= 35 or min_resource <= 30:
            diagnostic = "overshoot risk requiring deeper leverage"
        else:
            diagnostic = "partial improvement with remaining structural risk"

        summary.append(
            {
                "scenario": scenario_name,
                "final_resource_stock": final["resource_stock"],
                "minimum_resource_stock": round(min_resource, 3),
                "average_resource_stock": round(avg_resource, 3),
                "average_overshoot_index": round(avg_overshoot, 3),
                "average_structural_insight_score": round(avg_insight, 3),
                "final_trust_stock": final["trust_stock"],
                "final_resilience_capacity": final["resilience_capacity"],
                "final_leverage_quality": final["leverage_quality"],
                "diagnostic": diagnostic,
            }
        )

    return summary


def validate(rows: list[dict[str, object]]) -> list[str]:
    errors: list[str] = []
    bounded_fields = [
        "resource_stock",
        "perceived_resource_stock",
        "consumption_flow",
        "regeneration_flow",
        "overshoot_index",
        "leverage_quality",
        "trust_stock",
        "institutional_learning_stock",
        "resilience_capacity",
        "structural_insight_score",
    ]

    for row in rows:
        for field in bounded_fields:
            value = float(row[field])
            if value < -0.001 or value > 120.001:
                errors.append(f"{field} outside expected range in {row['scenario']} period {row['period']}: {value}")

    return errors


def build_scenarios() -> list[MeadowsScenario]:
    return [
        MeadowsScenario(
            name="Growth with weak feedback",
            periods=60,
            initial_resource_stock=82.0,
            initial_trust_stock=52.0,
            consumption_pressure=0.88,
            regeneration_capacity=0.34,
            feedback_delay=10,
            information_quality=0.28,
            rule_change_strength=0.22,
            goal_alignment=0.20,
            paradigm_shift_capacity=0.14,
            self_organization_capacity=0.24,
            equity_alignment=0.24,
        ),
        MeadowsScenario(
            name="Delayed correction",
            periods=60,
            initial_resource_stock=82.0,
            initial_trust_stock=52.0,
            consumption_pressure=0.78,
            regeneration_capacity=0.42,
            feedback_delay=8,
            information_quality=0.46,
            rule_change_strength=0.34,
            goal_alignment=0.32,
            paradigm_shift_capacity=0.22,
            self_organization_capacity=0.34,
            equity_alignment=0.36,
        ),
        MeadowsScenario(
            name="Technical efficiency",
            periods=60,
            initial_resource_stock=82.0,
            initial_trust_stock=56.0,
            consumption_pressure=0.62,
            regeneration_capacity=0.50,
            feedback_delay=5,
            information_quality=0.64,
            rule_change_strength=0.44,
            goal_alignment=0.40,
            paradigm_shift_capacity=0.26,
            self_organization_capacity=0.42,
            equity_alignment=0.44,
        ),
        MeadowsScenario(
            name="Structural leverage",
            periods=60,
            initial_resource_stock=82.0,
            initial_trust_stock=60.0,
            consumption_pressure=0.52,
            regeneration_capacity=0.62,
            feedback_delay=3,
            information_quality=0.78,
            rule_change_strength=0.74,
            goal_alignment=0.80,
            paradigm_shift_capacity=0.76,
            self_organization_capacity=0.72,
            equity_alignment=0.78,
        ),
    ]


def main() -> None:
    ensure_outputs()

    all_rows: list[dict[str, object]] = []
    for scenario in build_scenarios():
        all_rows.extend(run_scenario(scenario))

    validation_errors = validate(all_rows)
    if validation_errors:
        raise ValueError("Validation failed:\n" + "\n".join(validation_errors))

    summary_rows = summarize(all_rows)

    write_csv(OUTPUT_TABLES / "meadows_structural_insight_timeseries.csv", all_rows)
    write_csv(OUTPUT_TABLES / "meadows_structural_insight_summary.csv", summary_rows)

    (OUTPUT_TABLES / "validation_report.txt").write_text(
        "Validation passed.\n"
        "Overshoot, leverage, trust, resilience, learning, and structural insight outputs completed.\n",
        encoding="utf-8",
    )

    print("\nMeadows structural insight scenario summary:")
    for row in summary_rows:
        print(
            f"{row['scenario']}: final resource={row['final_resource_stock']}, "
            f"avg overshoot={row['average_overshoot_index']}, "
            f"diagnostic={row['diagnostic']}"
        )
    print(f"\nWrote {OUTPUT_TABLES / 'meadows_structural_insight_timeseries.csv'}")


if __name__ == "__main__":
    main()
