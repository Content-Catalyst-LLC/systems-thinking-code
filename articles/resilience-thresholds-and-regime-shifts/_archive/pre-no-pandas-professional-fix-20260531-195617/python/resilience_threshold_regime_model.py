#!/usr/bin/env python3
"""Professional synthetic resilience, threshold, and regime-shift model.

This script compares resilience trajectories under different intervention designs. It
exports time-series outputs and scenario diagnostics that can be reused by R,
notebooks, or reporting tools.
"""

from __future__ import annotations

from dataclasses import dataclass
from pathlib import Path
import pandas as pd

ROOT = Path(__file__).resolve().parents[1]
TABLE_DIR = ROOT / "outputs" / "tables"
TABLE_DIR.mkdir(parents=True, exist_ok=True)


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


def run_scenario(scenario: ResilienceScenario, years: int = 35) -> pd.DataFrame:
    resilience = scenario.initial_resilience
    pressure = scenario.initial_pressure
    rows: list[dict[str, object]] = []

    for year in range(years + 1):
        intervention_active = year >= scenario.intervention_year
        pressure = pressure + scenario.pressure_growth

        adaptive_gain = scenario.adaptive_capacity * 0.10
        learning_gain = scenario.learning_rate * 0.08
        buffer_gain = scenario.buffer_investment * 0.12 if intervention_active else 0.0
        degradation = scenario.degradation_rate + (pressure * 0.03)

        if intervention_active:
            pressure = pressure * (1 - scenario.transformation_effect)
            adaptive_gain = adaptive_gain * (1 + scenario.transformation_effect)

        resilience = clamp(resilience + adaptive_gain + learning_gain + buffer_gain - degradation)
        threshold_margin = resilience - pressure
        recovery_time_index = round(max(0.0, pressure / max(resilience, 1.0)), 3)
        regime = classify_regime(resilience, pressure, threshold_margin)

        rows.append(
            {
                "year": year,
                "scenario": scenario.name,
                "resilience": round(resilience, 2),
                "pressure": round(pressure, 2),
                "threshold_margin": round(threshold_margin, 2),
                "recovery_time_index": recovery_time_index,
                "intervention_active": intervention_active,
                "regime": regime,
            }
        )

    return pd.DataFrame(rows)


def build_scenarios() -> list[ResilienceScenario]:
    return [
        ResilienceScenario("Baseline pressure", 78, 35, 2.4, 8, 0, 4, 2.6, 999, 0.00),
        ResilienceScenario("Delayed response", 78, 35, 2.8, 6, 5, 4, 2.8, 20, 0.08),
        ResilienceScenario("Buffer-building adaptation", 78, 35, 2.2, 10, 16, 9, 2.2, 8, 0.10),
        ResilienceScenario("Transformative adaptation", 78, 35, 2.0, 12, 18, 12, 2.0, 6, 0.22),
    ]


def summarize(results: pd.DataFrame) -> pd.DataFrame:
    summary = (
        results.groupby("scenario", sort=False)
        .agg(
            final_resilience=("resilience", "last"),
            final_pressure=("pressure", "last"),
            minimum_threshold_margin=("threshold_margin", "min"),
            maximum_recovery_time=("recovery_time_index", "max"),
            years_near_threshold=("regime", lambda x: int((x == "near threshold").sum())),
            years_shifted=("regime", lambda x: int((x == "shifted regime").sum())),
        )
        .reset_index()
    )
    summary["diagnostic"] = summary.apply(
        lambda row: (
            "high regime-shift risk"
            if row["years_shifted"] > 0
            else "threshold warning"
            if row["years_near_threshold"] > 0
            else "resilience maintained"
        ),
        axis=1,
    )
    return summary


def main() -> None:
    results = pd.concat([run_scenario(s) for s in build_scenarios()], ignore_index=True)
    summary = summarize(results)

    results.to_csv(TABLE_DIR / "resilience_threshold_regime_results.csv", index=False)
    summary.to_csv(TABLE_DIR / "resilience_threshold_regime_summary.csv", index=False)

    print("Resilience scenario summary")
    print(summary.to_string(index=False))


if __name__ == "__main__":
    main()
