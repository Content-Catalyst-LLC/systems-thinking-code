#!/usr/bin/env python3
"""Shock-response diagnostics for adaptive complexity scenarios."""

from __future__ import annotations

import csv
import os

ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
TABLES = os.path.join(ROOT, "outputs", "tables")
INPUT = os.path.join(TABLES, "emergence_adaptation_complexity_timeseries.csv")
OUTPUT = os.path.join(TABLES, "shock_response_diagnostics.csv")


def main() -> None:
    if not os.path.exists(INPUT):
        raise FileNotFoundError("Run emergence_adaptation_complexity_model.py first.")
    with open(INPUT, newline="", encoding="utf-8") as handle:
        rows = list(csv.DictReader(handle))
    output_rows = []
    for scenario in sorted({row["scenario"] for row in rows}):
        subset = [row for row in rows if row["scenario"] == scenario]
        pre = next(row for row in subset if int(row["period"]) == 31)
        post = next(row for row in subset if int(row["period"]) == 36)
        final = subset[-1]
        output_rows.append({
            "scenario": scenario,
            "complexity_before_shock_window": pre["complexity_index"],
            "complexity_after_shock_window": post["complexity_index"],
            "final_complexity_index": final["complexity_index"],
            "final_system_mean": final["system_mean"],
        })
    with open(OUTPUT, "w", newline="", encoding="utf-8") as handle:
        writer = csv.DictWriter(handle, fieldnames=list(output_rows[0].keys()))
        writer.writeheader()
        writer.writerows(output_rows)
    print(f"Wrote {OUTPUT}")


if __name__ == "__main__":
    main()
