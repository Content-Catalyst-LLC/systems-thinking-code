#!/usr/bin/env python3
"""
Dependency-light professional workflow for The Ethics of Systems Thinking.

Purpose:
- Simulate boundary inclusion, voice, accountability, harm exposure, repair capacity,
  ecological responsibility, model humility, structural change, and power redistribution.
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
class EthicsScenario:
    name: str
    periods: int
    boundary_inclusion: float
    affected_voice: float
    transparency: float
    contestability: float
    remedy_capacity: float
    oversight_quality: float
    harm_exposure: float
    ecological_responsibility: float
    model_humility: float
    structural_change: float
    power_redistribution: float


def ensure_outputs() -> None:
    OUTPUT_TABLES.mkdir(parents=True, exist_ok=True)
    (ARTICLE_ROOT / "outputs" / "figures").mkdir(parents=True, exist_ok=True)


def clamp(value: float, low: float = 0.0, high: float = 100.0) -> float:
    return max(low, min(high, value))


def run_scenario(scenario: EthicsScenario) -> list[dict[str, object]]:
    trust_stock = 42.0
    cumulative_harm = scenario.harm_exposure * 40.0
    repair_stock = scenario.remedy_capacity * 35.0
    accountability_memory = 36.0
    rows: list[dict[str, object]] = []

    for period in range(scenario.periods + 1):
        accountability_index = clamp(
            scenario.affected_voice * 18.0
            + scenario.transparency * 16.0
            + scenario.contestability * 18.0
            + scenario.remedy_capacity * 18.0
            + scenario.oversight_quality * 18.0
            + accountability_memory * 0.12
        )

        boundary_ethics_score = clamp(
            scenario.boundary_inclusion * 42.0
            + scenario.model_humility * 20.0
            + scenario.affected_voice * 16.0
            + scenario.ecological_responsibility * 22.0
        )

        harm_pressure = clamp(
            scenario.harm_exposure * 18.0
            + max(0.0, 60.0 - boundary_ethics_score) * 0.18
            + max(0.0, 55.0 - accountability_index) * 0.16
            - scenario.structural_change * 5.0
            - scenario.power_redistribution * 4.0
        )

        repair_flow = clamp(
            scenario.remedy_capacity * 5.5
            + scenario.affected_voice * 3.4
            + scenario.oversight_quality * 3.2
            + scenario.power_redistribution * 3.8
            - max(0.0, cumulative_harm - 60.0) * 0.03
        )

        cumulative_harm = clamp(cumulative_harm + harm_pressure * 0.22 - repair_flow * 0.18)
        repair_stock = clamp(repair_stock + repair_flow * 0.26 + scenario.structural_change * 2.0)

        accountability_memory = clamp(
            accountability_memory
            + accountability_index * 0.08
            + scenario.transparency * 1.4
            + scenario.contestability * 1.3
            - harm_pressure * 0.04
        )

        trust_stock = clamp(
            trust_stock
            + accountability_index * 0.07
            + repair_stock * 0.06
            + scenario.affected_voice * 1.2
            - cumulative_harm * 0.05
        )

        ethical_leverage = clamp(
            scenario.structural_change * 25.0
            + scenario.power_redistribution * 22.0
            + repair_stock * 0.20
            + accountability_index * 0.18
            + boundary_ethics_score * 0.15
            - cumulative_harm * 0.10
        )

        model_risk = clamp(
            100.0
            - scenario.model_humility * 38.0
            - scenario.boundary_inclusion * 24.0
            - scenario.affected_voice * 18.0
            + scenario.harm_exposure * 18.0
        )

        ethical_system_score = clamp(
            boundary_ethics_score * 0.22
            + accountability_index * 0.24
            + repair_stock * 0.18
            + ethical_leverage * 0.24
            + trust_stock * 0.12
            - cumulative_harm * 0.18
            - model_risk * 0.10
        )

        rows.append(
            {
                "period": period,
                "scenario": scenario.name,
                "boundary_ethics_score": round(boundary_ethics_score, 3),
                "accountability_index": round(accountability_index, 3),
                "harm_pressure": round(harm_pressure, 3),
                "cumulative_harm": round(cumulative_harm, 3),
                "repair_flow": round(repair_flow, 3),
                "repair_stock": round(repair_stock, 3),
                "accountability_memory": round(accountability_memory, 3),
                "trust_stock": round(trust_stock, 3),
                "ethical_leverage": round(ethical_leverage, 3),
                "model_risk": round(model_risk, 3),
                "ethical_system_score": round(ethical_system_score, 3),
            }
        )

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
        avg_harm = mean(float(row["cumulative_harm"]) for row in subset)
        avg_accountability = mean(float(row["accountability_index"]) for row in subset)
        avg_score = mean(float(row["ethical_system_score"]) for row in subset)
        avg_model_risk = mean(float(row["model_risk"]) for row in subset)

        if float(final["ethical_system_score"]) >= 65 and float(final["cumulative_harm"]) <= 35:
            diagnostic = "ethically accountable systems pathway"
        elif avg_harm >= 55 or avg_model_risk >= 50:
            diagnostic = "high ethical risk requiring boundary and accountability redesign"
        elif avg_accountability >= 55:
            diagnostic = "partial accountability with remaining harm risk"
        else:
            diagnostic = "weak ethical systems capacity"

        summary.append(
            {
                "scenario": scenario_name,
                "final_ethical_system_score": final["ethical_system_score"],
                "final_cumulative_harm": final["cumulative_harm"],
                "final_accountability_index": final["accountability_index"],
                "final_boundary_ethics_score": final["boundary_ethics_score"],
                "final_repair_stock": final["repair_stock"],
                "final_model_risk": final["model_risk"],
                "average_cumulative_harm": round(avg_harm, 3),
                "average_accountability_index": round(avg_accountability, 3),
                "average_ethical_system_score": round(avg_score, 3),
                "diagnostic": diagnostic,
            }
        )

    return summary


def validate(rows: list[dict[str, object]]) -> list[str]:
    errors: list[str] = []
    bounded_fields = [
        "boundary_ethics_score",
        "accountability_index",
        "harm_pressure",
        "cumulative_harm",
        "repair_flow",
        "repair_stock",
        "accountability_memory",
        "trust_stock",
        "ethical_leverage",
        "model_risk",
        "ethical_system_score",
    ]

    for row in rows:
        for field in bounded_fields:
            value = float(row[field])
            if value < -0.001 or value > 120.001:
                errors.append(f"{field} outside expected range in {row['scenario']} period {row['period']}: {value}")

    return errors


def build_scenarios() -> list[EthicsScenario]:
    return [
        EthicsScenario(
            name="Narrow optimization",
            periods=48,
            boundary_inclusion=0.24,
            affected_voice=0.18,
            transparency=0.28,
            contestability=0.14,
            remedy_capacity=0.16,
            oversight_quality=0.22,
            harm_exposure=0.82,
            ecological_responsibility=0.20,
            model_humility=0.24,
            structural_change=0.18,
            power_redistribution=0.10,
        ),
        EthicsScenario(
            name="Consultative weak accountability",
            periods=48,
            boundary_inclusion=0.46,
            affected_voice=0.42,
            transparency=0.52,
            contestability=0.34,
            remedy_capacity=0.32,
            oversight_quality=0.42,
            harm_exposure=0.62,
            ecological_responsibility=0.44,
            model_humility=0.48,
            structural_change=0.34,
            power_redistribution=0.26,
        ),
        EthicsScenario(
            name="Accountable redesign",
            periods=48,
            boundary_inclusion=0.68,
            affected_voice=0.66,
            transparency=0.72,
            contestability=0.64,
            remedy_capacity=0.62,
            oversight_quality=0.68,
            harm_exposure=0.40,
            ecological_responsibility=0.68,
            model_humility=0.70,
            structural_change=0.66,
            power_redistribution=0.58,
        ),
        EthicsScenario(
            name="Repair-centered transformation",
            periods=48,
            boundary_inclusion=0.82,
            affected_voice=0.80,
            transparency=0.78,
            contestability=0.78,
            remedy_capacity=0.82,
            oversight_quality=0.80,
            harm_exposure=0.30,
            ecological_responsibility=0.84,
            model_humility=0.82,
            structural_change=0.84,
            power_redistribution=0.78,
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

    write_csv(OUTPUT_TABLES / "ethical_systems_thinking_timeseries.csv", all_rows)
    write_csv(OUTPUT_TABLES / "ethical_systems_thinking_summary.csv", summary_rows)

    (OUTPUT_TABLES / "validation_report.txt").write_text(
        "Validation passed.\n"
        "Ethical systems, boundary, accountability, repair, and harm outputs completed.\n",
        encoding="utf-8",
    )

    print("\nEthical systems thinking scenario summary:")
    for row in summary_rows:
        print(
            f"{row['scenario']}: ethical score={row['final_ethical_system_score']}, "
            f"harm={row['final_cumulative_harm']}, "
            f"diagnostic={row['diagnostic']}"
        )
    print(f"\nWrote {OUTPUT_TABLES / 'ethical_systems_thinking_timeseries.csv'}")


if __name__ == "__main__":
    main()
