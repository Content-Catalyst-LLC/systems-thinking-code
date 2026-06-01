#!/usr/bin/env python3
"""Summarize engagement amplification and creator adaptation diagnostics."""

from __future__ import annotations

from pathlib import Path
import csv
from statistics import mean

ROOT = Path(__file__).resolve().parents[1]
TABLES = ROOT / "outputs" / "tables"
INPUT = TABLES / "platform_feedback_timeseries.csv"
OUTPUT = TABLES / "engagement_amplification_diagnostics.csv"


def read_rows(path: Path) -> list[dict[str, str]]:
    if not path.exists():
        raise FileNotFoundError(f"Missing {path}. Run the base platform model first.")
    with path.open("r", newline="", encoding="utf-8") as handle:
        return list(csv.DictReader(handle))


def write_csv(path: Path, rows: list[dict[str, object]]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", newline="", encoding="utf-8") as handle:
        writer = csv.DictWriter(handle, fieldnames=list(rows[0].keys()))
        writer.writeheader()
        writer.writerows(rows)


def main() -> None:
    rows = read_rows(INPUT)
    scenarios = sorted({row["scenario"] for row in rows})
    diagnostics: list[dict[str, object]] = []

    for scenario in scenarios:
        subset = [row for row in rows if row["scenario"] == scenario]
        first = subset[0]
        final = subset[-1]
        engagement_gain = float(final["engagement_index"]) - float(first["engagement_index"])
        creator_pressure_gain = float(final["creator_metric_pressure"]) - float(first["creator_metric_pressure"])
        average_engagement = mean(float(row["engagement_index"]) for row in subset)
        average_creator_pressure = mean(float(row["creator_metric_pressure"]) for row in subset)
        diagnostics.append(
            {
                "scenario": scenario,
                "engagement_gain": round(engagement_gain, 3),
                "creator_pressure_gain": round(creator_pressure_gain, 3),
                "average_engagement_index": round(average_engagement, 3),
                "average_creator_metric_pressure": round(average_creator_pressure, 3),
                "interpretation": "amplification pressure dominates" if creator_pressure_gain > 25 else "managed amplification dynamics",
            }
        )

    write_csv(OUTPUT, diagnostics)
    print(f"Wrote {OUTPUT}")


if __name__ == "__main__":
    main()
