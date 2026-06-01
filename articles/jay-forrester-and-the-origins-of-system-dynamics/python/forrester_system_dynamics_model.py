#!/usr/bin/env python3
"""
Dependency-light professional workflow for Jay Forrester and system dynamics.

Purpose:
- Simulate stocks, flows, delays, corrective action, policy resistance,
  structural leverage, institutional learning, trust, and performance.
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
class DynamicsScenario:
    name: str
    periods: int
    initial_backlog: float
    initial_capacity: float
    desired_backlog: float
    demand_growth: float
    correction_strength: float
    delay_periods: int
    investment_fraction: float
    learning_strength: float
    compensating_feedback: float
    participatory_quality: float


def ensure_outputs() -> None:
    OUTPUT_TABLES.mkdir(parents=True, exist_ok=True)
    (ARTICLE_ROOT / "outputs" / "figures").mkdir(parents=True, exist_ok=True)


def clamp(value: float, low: float = 0.0, high: float = 100.0) -> float:
    return max(low, min(high, value))


def delayed_value(series: list[float], delay: int) -> float:
    if len(series) <= delay:
        return series[0]
    return series[-delay - 1]


def run_scenario(scenario: DynamicsScenario) -> list[dict[str, object]]:
    backlog = scenario.initial_backlog
    capacity = scenario.initial_capacity
    trust = 55.0
    institutional_learning = 35.0
    perceived_backlog_history = [backlog]
    rows: list[dict[str, object]] = []

    for period in range(scenario.periods + 1):
        perceived_backlog = delayed_value(perceived_backlog_history, scenario.delay_periods)
        backlog_gap = perceived_backlog - scenario.desired_backlog

        corrective_action = clamp(
            scenario.correction_strength * backlog_gap
            + scenario.learning_strength * institutional_learning * 0.05
        )

        investment = clamp(
            scenario.investment_fraction * corrective_action
            + scenario.participatory_quality * 4.0
        )

        resistance = clamp(
            scenario.compensating_feedback * corrective_action * 0.45
            + max(0.0, 50.0 - trust) * 0.12
        )

        demand_pressure = scenario.demand_growth * (1.0 + period / max(1, scenario.periods)) * 5.0

        service_flow = clamp(
            capacity * 0.42
            + corrective_action * 0.15
            - resistance * 0.08
        )

        new_backlog = clamp(backlog + demand_pressure - service_flow, 0.0, 200.0)

        capacity = clamp(
            capacity
            + investment * 0.20
            - resistance * 0.04
            - backlog * 0.015,
            0.0,
            140.0
        )

        institutional_learning = clamp(
            institutional_learning
            + scenario.learning_strength * 2.4
            + scenario.participatory_quality * 2.0
            - resistance * 0.05
        )

        trust = clamp(
            trust
            + service_flow * 0.08
            + scenario.participatory_quality * 1.5
            - new_backlog * 0.035
            - resistance * 0.08
        )

        policy_resistance_index = clamp(resistance + max(0.0, new_backlog - backlog) * 0.30)

        system_performance = clamp(
            100.0
            - new_backlog * 0.35
            + capacity * 0.18
            + trust * 0.16
            + institutional_learning * 0.12
            - policy_resistance_index * 0.20
        )

        rows.append(
            {
                "period": period,
                "scenario": scenario.name,
                "backlog_stock": round(backlog, 3),
                "capacity_stock": round(capacity, 3),
                "perceived_backlog": round(perceived_backlog, 3),
                "corrective_action": round(corrective_action, 3),
                "investment_flow": round(investment, 3),
                "service_flow": round(service_flow, 3),
                "resistance_index": round(policy_resistance_index, 3),
                "trust_stock": round(trust, 3),
                "institutional_learning_stock": round(institutional_learning, 3),
                "system_performance": round(system_performance, 3),
            }
        )

        backlog = new_backlog
        perceived_backlog_history.append(backlog)

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

        avg_backlog = mean(float(row["backlog_stock"]) for row in subset)
        avg_resistance = mean(float(row["resistance_index"]) for row in subset)
        avg_performance = mean(float(row["system_performance"]) for row in subset)
        max_corrective_action = max(float(row["corrective_action"]) for row in subset)

        if avg_performance >= 65 and float(final["backlog_stock"]) <= 45:
            diagnostic = "structural improvement pathway"
        elif avg_resistance >= 35:
            diagnostic = "high policy resistance and delayed correction"
        else:
            diagnostic = "partial improvement requiring deeper feedback redesign"

        summary.append(
            {
                "scenario": scenario_name,
                "final_backlog_stock": final["backlog_stock"],
                "final_capacity_stock": final["capacity_stock"],
                "average_backlog_stock": round(avg_backlog, 3),
                "average_policy_resistance_index": round(avg_resistance, 3),
                "average_system_performance": round(avg_performance, 3),
                "maximum_corrective_action": round(max_corrective_action, 3),
                "final_trust_stock": final["trust_stock"],
                "final_institutional_learning_stock": final["institutional_learning_stock"],
                "diagnostic": diagnostic,
            }
        )

    return summary


def validate(rows: list[dict[str, object]]) -> list[str]:
    errors: list[str] = []
    bounded_fields = [
        "capacity_stock",
        "corrective_action",
        "investment_flow",
        "service_flow",
        "resistance_index",
        "trust_stock",
        "institutional_learning_stock",
        "system_performance",
    ]

    for row in rows:
        for field in bounded_fields:
            value = float(row[field])
            if value < -0.001 or value > 150.001:
                errors.append(f"{field} outside expected range in {row['scenario']} period {row['period']}: {value}")

        backlog = float(row["backlog_stock"])
        if backlog < -0.001 or backlog > 220.001:
            errors.append(f"backlog outside expected range in {row['scenario']} period {row['period']}: {backlog}")

    return errors


def build_scenarios() -> list[DynamicsScenario]:
    return [
        DynamicsScenario(
            name="Reactive management",
            periods=48,
            initial_backlog=58.0,
            initial_capacity=46.0,
            desired_backlog=25.0,
            demand_growth=0.82,
            correction_strength=0.34,
            delay_periods=6,
            investment_fraction=0.24,
            learning_strength=0.18,
            compensating_feedback=0.70,
            participatory_quality=0.16,
        ),
        DynamicsScenario(
            name="Delayed correction",
            periods=48,
            initial_backlog=58.0,
            initial_capacity=46.0,
            desired_backlog=25.0,
            demand_growth=0.76,
            correction_strength=0.58,
            delay_periods=10,
            investment_fraction=0.34,
            learning_strength=0.24,
            compensating_feedback=0.62,
            participatory_quality=0.24,
        ),
        DynamicsScenario(
            name="Structural leverage",
            periods=48,
            initial_backlog=58.0,
            initial_capacity=46.0,
            desired_backlog=25.0,
            demand_growth=0.60,
            correction_strength=0.42,
            delay_periods=4,
            investment_fraction=0.68,
            learning_strength=0.58,
            compensating_feedback=0.30,
            participatory_quality=0.56,
        ),
        DynamicsScenario(
            name="Participatory learning",
            periods=48,
            initial_backlog=58.0,
            initial_capacity=46.0,
            desired_backlog=25.0,
            demand_growth=0.56,
            correction_strength=0.38,
            delay_periods=3,
            investment_fraction=0.64,
            learning_strength=0.78,
            compensating_feedback=0.22,
            participatory_quality=0.82,
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

    write_csv(OUTPUT_TABLES / "forrester_system_dynamics_timeseries.csv", all_rows)
    write_csv(OUTPUT_TABLES / "forrester_system_dynamics_summary.csv", summary_rows)

    (OUTPUT_TABLES / "validation_report.txt").write_text(
        "Validation passed.\n"
        "Stock-flow, delay, policy resistance, learning, and performance outputs completed.\n",
        encoding="utf-8",
    )

    print("\nForrester system dynamics scenario summary:")
    for row in summary_rows:
        print(
            f"{row['scenario']}: avg backlog={row['average_backlog_stock']}, "
            f"avg resistance={row['average_policy_resistance_index']}, "
            f"diagnostic={row['diagnostic']}"
        )
    print(f"\nWrote {OUTPUT_TABLES / 'forrester_system_dynamics_timeseries.csv'}")


if __name__ == "__main__":
    main()
