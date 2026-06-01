#!/usr/bin/env python3
"""Simple deterministic sensitivity analysis for resilience threshold risk."""

from __future__ import annotations

from pathlib import Path
import pandas as pd

ROOT = Path(__file__).resolve().parents[1]
TABLE_DIR = ROOT / "outputs" / "tables"
TABLE_DIR.mkdir(parents=True, exist_ok=True)


def risk_score(pressure_growth: float, buffer: float, learning: float, transformation: float) -> float:
    base = 50 + pressure_growth * 14 - buffer * 0.85 - learning * 0.65 - transformation * 60
    return max(0, min(100, round(base, 2)))


def main() -> None:
    baseline = {"pressure_growth": 2.4, "buffer": 8.0, "learning": 7.0, "transformation": 0.10}
    rows = []
    for parameter, values in {
        "pressure_growth": [1.6, 2.0, 2.4, 2.8, 3.2],
        "buffer": [0, 6, 12, 18, 24],
        "learning": [2, 5, 8, 11, 14],
        "transformation": [0.00, 0.05, 0.10, 0.15, 0.22],
    }.items():
        for value in values:
            settings = baseline.copy()
            settings[parameter] = value
            rows.append({"parameter": parameter, "value": value, "threshold_risk_score": risk_score(**settings)})
    df = pd.DataFrame(rows)
    ranking = (
        df.groupby("parameter")
        .agg(risk_range=("threshold_risk_score", lambda s: round(s.max() - s.min(), 2)))
        .reset_index()
        .sort_values("risk_range", ascending=False)
    )
    df.to_csv(TABLE_DIR / "resilience_sensitivity_results.csv", index=False)
    ranking.to_csv(TABLE_DIR / "resilience_sensitivity_ranking.csv", index=False)
    print("Sensitivity ranking")
    print(ranking.to_string(index=False))


if __name__ == "__main__":
    main()
