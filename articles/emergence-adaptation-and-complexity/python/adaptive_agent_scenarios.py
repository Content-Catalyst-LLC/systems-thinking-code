#!/usr/bin/env python3
"""Additional adaptive-agent scenario summary for article documentation."""

from __future__ import annotations

import csv
import os
from statistics import mean

ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
TABLES = os.path.join(ROOT, "outputs", "tables")
INPUT = os.path.join(TABLES, "emergence_adaptation_complexity_timeseries.csv")
OUTPUT = os.path.join(TABLES, "adaptive_agent_diagnostics.csv")


def main() -> None:
    if not os.path.exists(INPUT):
        raise FileNotFoundError("Run emergence_adaptation_complexity_model.py first.")
    with open(INPUT, newline="", encoding="utf-8") as handle:
        rows = list(csv.DictReader(handle))
    output_rows = []
    for scenario in sorted({row["scenario"] for row in rows}):
        subset = [row for row in rows if row["scenario"] == scenario]
        early = subset[:10]
        late = subset[-10:]
        output_rows.append({
            "scenario": scenario,
            "early_mean_complexity": round(mean(float(row["complexity_index"]) for row in early), 4),
            "late_mean_complexity": round(mean(float(row["complexity_index"]) for row in late), 4),
            "late_mean_diversity": round(mean(float(row["diversity_index"]) for row in late), 4),
            "late_mean_synchronization": round(mean(float(row["synchronization_index"]) for row in late), 4),
        })
    with open(OUTPUT, "w", newline="", encoding="utf-8") as handle:
        writer = csv.DictWriter(handle, fieldnames=list(output_rows[0].keys()))
        writer.writeheader()
        writer.writerows(output_rows)
    print(f"Wrote {OUTPUT}")


if __name__ == "__main__":
    main()
