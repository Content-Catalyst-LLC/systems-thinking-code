#!/usr/bin/env python3
"""
Early warning indicator analysis for resilience scenarios.
Requires only the Python standard library.
"""

from __future__ import annotations

import csv
from pathlib import Path
from statistics import mean, variance
from typing import Dict, List

ROOT = Path(__file__).resolve().parents[1]
TABLES = ROOT / "outputs" / "tables"
INPUT = TABLES / "resilience_threshold_regime_results.csv"
OUTPUT = TABLES / "resilience_early_warning_indicators.csv"


def read_rows(path: Path) -> List[Dict[str, str]]:
    with path.open("r", newline="", encoding="utf-8") as handle:
        return list(csv.DictReader(handle))


def autocorrelation(values: List[float]) -> float:
    if len(values) < 3:
        return 0.0
    xs = values[:-1]
    ys = values[1:]
    x_mean = mean(xs)
    y_mean = mean(ys)
    numerator = sum((x - x_mean) * (y - y_mean) for x, y in zip(xs, ys))
    denom_x = sum((x - x_mean) ** 2 for x in xs)
    denom_y = sum((y - y_mean) ** 2 for y in ys)
    denominator = (denom_x * denom_y) ** 0.5
    return numerator / denominator if denominator else 0.0


def classify_warning(min_margin: float, recovery_slope: float, rolling_variance: float, acf: float) -> str:
    if min_margin <= 0:
        return "threshold crossed"
    if min_margin <= 10 or recovery_slope > 0.02 or acf > 0.85:
        return "strong early warning"
    if rolling_variance > 25 or recovery_slope > 0.01:
        return "moderate warning"
    return "limited warning"


def main() -> None:
    if not INPUT.exists():
        raise FileNotFoundError(f"Missing input file: {INPUT}. Run resilience_threshold_regime_model.py first.")

    rows = read_rows(INPUT)
    grouped: Dict[str, List[Dict[str, str]]] = {}
    for row in rows:
        grouped.setdefault(row["scenario"], []).append(row)

    output_rows: List[Dict[str, object]] = []
    for scenario, scenario_rows in grouped.items():
        scenario_rows = sorted(scenario_rows, key=lambda r: int(r["year"]))
        margins = [float(r["threshold_margin"]) for r in scenario_rows]
        recovery = [float(r["recovery_time_index"]) for r in scenario_rows]
        resilience = [float(r["resilience"]) for r in scenario_rows]
        min_margin = min(margins)
        recovery_slope = (recovery[-1] - recovery[0]) / max(1, len(recovery) - 1)
        rolling_variance = variance(resilience[-10:]) if len(resilience) >= 10 else 0.0
        acf = autocorrelation(resilience[-15:]) if len(resilience) >= 15 else 0.0
        warning = classify_warning(min_margin, recovery_slope, rolling_variance, acf)
        first_near_threshold = next((r["year"] for r in scenario_rows if r["regime"] == "near threshold"), "")
        first_shifted = next((r["year"] for r in scenario_rows if r["regime"] == "shifted regime"), "")

        output_rows.append(
            {
                "scenario": scenario,
                "minimum_threshold_margin": round(min_margin, 2),
                "recovery_time_slope": round(recovery_slope, 4),
                "recent_resilience_variance": round(rolling_variance, 3),
                "recent_resilience_autocorrelation": round(acf, 3),
                "first_near_threshold_year": first_near_threshold,
                "first_shifted_year": first_shifted,
                "early_warning_class": warning,
            }
        )

    with OUTPUT.open("w", newline="", encoding="utf-8") as handle:
        writer = csv.DictWriter(handle, fieldnames=list(output_rows[0].keys()))
        writer.writeheader()
        writer.writerows(output_rows)

    print("\nEarly warning diagnostics:")
    for row in output_rows:
        print(f"- {row['scenario']}: {row['early_warning_class']} | min margin={row['minimum_threshold_margin']}")


if __name__ == "__main__":
    main()
