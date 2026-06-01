#!/usr/bin/env python3
"""Early warning diagnostics for synthetic resilience trajectories."""

from __future__ import annotations

from pathlib import Path
import subprocess
import sys
import pandas as pd

ROOT = Path(__file__).resolve().parents[1]
TABLE_DIR = ROOT / "outputs" / "tables"
TABLE_DIR.mkdir(parents=True, exist_ok=True)
RESULTS_PATH = TABLE_DIR / "resilience_threshold_regime_results.csv"


def ensure_inputs() -> None:
    if not RESULTS_PATH.exists():
        subprocess.run([sys.executable, str(ROOT / "python" / "resilience_threshold_regime_model.py")], check=True)


def rolling_autocorrelation(values: pd.Series, window: int = 6) -> list[float | None]:
    out: list[float | None] = []
    for i in range(len(values)):
        if i + 1 < window:
            out.append(None)
            continue
        segment = values.iloc[i + 1 - window : i + 1]
        out.append(segment.autocorr(lag=1))
    return out


def main() -> None:
    ensure_inputs()
    results = pd.read_csv(RESULTS_PATH)
    frames = []
    for scenario, group in results.groupby("scenario", sort=False):
        g = group.sort_values("year").copy()
        g["rolling_variance_pressure"] = g["pressure"].rolling(6).var().round(4)
        g["rolling_variance_margin"] = g["threshold_margin"].rolling(6).var().round(4)
        g["rolling_autocorrelation_margin"] = rolling_autocorrelation(g["threshold_margin"], window=6)
        g["early_warning_flag"] = (
            (g["threshold_margin"] <= 15)
            | (g["rolling_variance_margin"].fillna(0) > g["rolling_variance_margin"].median(skipna=True))
            | (g["recovery_time_index"] >= 0.80)
        )
        frames.append(g)

    diagnostics = pd.concat(frames, ignore_index=True)
    summary = (
        diagnostics.groupby("scenario", sort=False)
        .agg(
            warning_years=("early_warning_flag", "sum"),
            max_recovery_time=("recovery_time_index", "max"),
            max_margin_variance=("rolling_variance_margin", "max"),
            lowest_threshold_margin=("threshold_margin", "min"),
        )
        .reset_index()
    )
    summary["warning_level"] = summary["warning_years"].apply(
        lambda x: "high" if x >= 10 else "moderate" if x >= 4 else "low"
    )

    diagnostics.to_csv(TABLE_DIR / "early_warning_indicator_timeseries.csv", index=False)
    summary.to_csv(TABLE_DIR / "early_warning_indicator_summary.csv", index=False)
    print("Early warning indicator summary")
    print(summary.to_string(index=False))


if __name__ == "__main__":
    main()
