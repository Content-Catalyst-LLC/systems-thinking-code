#!/usr/bin/env python3
"""
Professional resilience, threshold, and regime-shift scenario model.

Purpose
-------
This script creates synthetic but realistic resilience-system scenarios for
practitioner analysis. It requires only the Python standard library.

Outputs
-------
- outputs/tables/resilience_threshold_regime_results.csv
- outputs/tables/resilience_threshold_regime_summary.csv
- outputs/tables/resilience_validation_report.csv
- docs/python_workflow_notes.md

Responsible use
---------------
The outputs are synthetic and intended for methods demonstration, early-stage
policy/system diagnostics, and reproducible workflow scaffolding. They are not
predictions about a real ecosystem, institution, infrastructure system, or
community unless replaced with validated local data and reviewed by domain
experts and affected stakeholders.
"""

from __future__ import annotations

import csv
from dataclasses import dataclass
from pathlib import Path
from statistics import mean
from typing import Dict, Iterable, List

ROOT = Path(__file__).resolve().parents[1]
TABLES = ROOT / "outputs" / "tables"
DOCS = ROOT / "docs"
TABLES.mkdir(parents=True, exist_ok=True)
DOCS.mkdir(parents=True, exist_ok=True)


@dataclass(frozen=True)
class ResilienceScenario:
    name: str
    initial_resilience: float
    initial_pressure: float
    pressure_growth: float
    adaptive_capacity: float
    buffer_investment: float
    learning_rate: float
    degradation_rate: float
    intervention_year: int
    transformation_effect: float
    equity_protection: float


def clamp(value: float, low: float = 0.0, high: float = 100.0) -> float:
    return max(low, min(high, value))


def classify_regime(resilience: float, pressure: float, threshold_margin: float) -> str:
    if pressure >= resilience:
        return "shifted regime"
    if threshold_margin <= 10:
        return "near threshold"
    if resilience >= 70 and threshold_margin >= 25:
        return "resilient regime"
    return "stressed but recoverable"


def run_scenario(scenario: ResilienceScenario, years: int = 35) -> List[Dict[str, object]]:
    resilience = scenario.initial_resilience
    pressure = scenario.initial_pressure
    vulnerability_index = 48.0
    rows: List[Dict[str, object]] = []

    for year in range(years + 1):
        intervention_active = year >= scenario.intervention_year

        pressure += scenario.pressure_growth
        adaptive_gain = scenario.adaptive_capacity * 0.10
        learning_gain = scenario.learning_rate * 0.08
        buffer_gain = scenario.buffer_investment * 0.12 if intervention_active else 0.0
        vulnerability_reduction = scenario.equity_protection * 0.10 if intervention_active else 0.0

        if intervention_active:
            pressure *= 1 - scenario.transformation_effect
            adaptive_gain *= 1 + scenario.transformation_effect

        degradation = scenario.degradation_rate + (pressure * 0.03) + (vulnerability_index * 0.015)
        resilience = clamp(resilience + adaptive_gain + learning_gain + buffer_gain - degradation)
        vulnerability_index = clamp(vulnerability_index + 0.35 - vulnerability_reduction, 0, 100)

        threshold_margin = resilience - pressure
        recovery_time_index = max(0.0, pressure / max(resilience, 1.0))
        regime = classify_regime(resilience, pressure, threshold_margin)

        rows.append(
            {
                "year": year,
                "scenario": scenario.name,
                "resilience": round(resilience, 2),
                "pressure": round(pressure, 2),
                "threshold_margin": round(threshold_margin, 2),
                "recovery_time_index": round(recovery_time_index, 3),
                "vulnerability_index": round(vulnerability_index, 2),
                "intervention_active": str(intervention_active).lower(),
                "regime": regime,
            }
        )
    return rows


def summarize(rows: Iterable[Dict[str, object]]) -> List[Dict[str, object]]:
    grouped: Dict[str, List[Dict[str, object]]] = {}
    for row in rows:
        grouped.setdefault(str(row["scenario"]), []).append(row)

    summary: List[Dict[str, object]] = []
    for scenario, scenario_rows in grouped.items():
        margins = [float(r["threshold_margin"]) for r in scenario_rows]
        recovery_times = [float(r["recovery_time_index"]) for r in scenario_rows]
        resilience_values = [float(r["resilience"]) for r in scenario_rows]
        pressure_values = [float(r["pressure"]) for r in scenario_rows]
        vulnerability_values = [float(r["vulnerability_index"]) for r in scenario_rows]
        regimes = [str(r["regime"]) for r in scenario_rows]
        years_near_threshold = sum(1 for r in regimes if r == "near threshold")
        years_shifted = sum(1 for r in regimes if r == "shifted regime")

        if years_shifted:
            diagnostic = "high regime-shift risk"
        elif years_near_threshold:
            diagnostic = "threshold warning"
        elif min(margins) < 20:
            diagnostic = "stressed but recoverable"
        else:
            diagnostic = "resilience maintained"

        summary.append(
            {
                "scenario": scenario,
                "final_resilience": round(resilience_values[-1], 2),
                "final_pressure": round(pressure_values[-1], 2),
                "minimum_threshold_margin": round(min(margins), 2),
                "maximum_recovery_time": round(max(recovery_times), 3),
                "average_resilience": round(mean(resilience_values), 2),
                "final_vulnerability_index": round(vulnerability_values[-1], 2),
                "years_near_threshold": years_near_threshold,
                "years_shifted": years_shifted,
                "diagnostic": diagnostic,
            }
        )
    return summary


def write_csv(path: Path, rows: List[Dict[str, object]]) -> None:
    if not rows:
        raise ValueError(f"No rows to write for {path}")
    with path.open("w", newline="", encoding="utf-8") as handle:
        writer = csv.DictWriter(handle, fieldnames=list(rows[0].keys()))
        writer.writeheader()
        writer.writerows(rows)


def validate(results: List[Dict[str, object]], summary: List[Dict[str, object]]) -> List[Dict[str, object]]:
    checks = []
    checks.append(
        {
            "check": "results_have_rows",
            "status": "pass" if len(results) > 0 else "fail",
            "detail": f"{len(results)} result rows generated",
        }
    )
    checks.append(
        {
            "check": "all_scenarios_summarized",
            "status": "pass" if len(summary) >= 4 else "fail",
            "detail": f"{len(summary)} scenarios summarized",
        }
    )
    invalid_regime = [r for r in results if str(r["regime"]) not in {"resilient regime", "stressed but recoverable", "near threshold", "shifted regime"}]
    checks.append(
        {
            "check": "regime_labels_valid",
            "status": "pass" if not invalid_regime else "fail",
            "detail": f"{len(invalid_regime)} invalid regime labels",
        }
    )
    negative_values = [r for r in results if float(r["resilience"]) < 0 or float(r["pressure"]) < 0]
    checks.append(
        {
            "check": "nonnegative_core_values",
            "status": "pass" if not negative_values else "fail",
            "detail": f"{len(negative_values)} rows with negative resilience/pressure",
        }
    )
    return checks


def main() -> None:
    scenarios = [
        ResilienceScenario("Baseline pressure", 78, 35, 2.4, 8, 0, 4, 2.6, 999, 0.00, 0),
        ResilienceScenario("Delayed response", 78, 35, 2.8, 6, 5, 4, 2.8, 20, 0.08, 4),
        ResilienceScenario("Buffer-building adaptation", 78, 35, 2.2, 10, 16, 9, 2.2, 8, 0.10, 12),
        ResilienceScenario("Transformative adaptation", 78, 35, 2.0, 12, 18, 12, 2.0, 6, 0.22, 18),
    ]

    results: List[Dict[str, object]] = []
    for scenario in scenarios:
        results.extend(run_scenario(scenario))

    summary = summarize(results)
    validation = validate(results, summary)

    write_csv(TABLES / "resilience_threshold_regime_results.csv", results)
    write_csv(TABLES / "resilience_threshold_regime_summary.csv", summary)
    write_csv(TABLES / "resilience_validation_report.csv", validation)

    notes = """# Python Workflow Notes: Resilience, Thresholds, and Regime Shifts

This dependency-light Python workflow models resilience as a dynamic stock shaped by
pressure, adaptive capacity, buffers, learning, vulnerability, and transformation.
It is intended for professional adaptation with real system data after local
validation.

## Generated outputs

- `outputs/tables/resilience_threshold_regime_results.csv`
- `outputs/tables/resilience_threshold_regime_summary.csv`
- `outputs/tables/resilience_validation_report.csv`

## Professional interpretation

The workflow helps compare whether a system remains resilient, approaches a
threshold, or enters a shifted regime under different intervention timings and
capacity-building strategies. Replace synthetic assumptions with local evidence
before using for operational decisions.
"""
    (DOCS / "python_workflow_notes.md").write_text(notes, encoding="utf-8")

    print("\nResilience scenario summary:")
    for row in summary:
        print(
            f"- {row['scenario']}: {row['diagnostic']} | "
            f"final resilience={row['final_resilience']} | "
            f"min margin={row['minimum_threshold_margin']}"
        )

    failed = [row for row in validation if row["status"] != "pass"]
    if failed:
        raise SystemExit(f"Validation failed: {failed}")


if __name__ == "__main__":
    main()
