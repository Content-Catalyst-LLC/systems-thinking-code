#!/usr/bin/env python3
"""Detect simple trend direction and recurring event types in synthetic data."""
from pathlib import Path
import pandas as pd

ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "data"
OUT = ROOT / "outputs"
OUT.mkdir(exist_ok=True)


def trend_label(series: pd.Series) -> str:
    delta = series.iloc[-1] - series.iloc[0]
    if delta > 0:
        return "increasing"
    if delta < 0:
        return "decreasing"
    return "flat"


def main() -> None:
    indicators = pd.read_csv(DATA / "synthetic_time_series_indicators.csv")
    events = pd.read_csv(DATA / "synthetic_events.csv")
    trend_rows = []
    for col in indicators.columns:
        if col != "year":
            trend_rows.append({"indicator": col, "trend": trend_label(indicators[col]), "change": indicators[col].iloc[-1] - indicators[col].iloc[0]})
    trends = pd.DataFrame(trend_rows)
    recurrence = events.groupby(["system_area", "event_type"]).size().reset_index(name="count").sort_values("count", ascending=False)
    trends.to_csv(OUT / "trend_summary.csv", index=False)
    recurrence.to_csv(OUT / "recurrence_summary.csv", index=False)
    print("Trend summary")
    print(trends)
    print("\nRecurring event types")
    print(recurrence)


if __name__ == "__main__":
    main()
