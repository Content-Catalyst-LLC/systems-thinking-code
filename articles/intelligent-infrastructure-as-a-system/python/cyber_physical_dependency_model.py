#!/usr/bin/env python3
"""Summarize cyber-physical dependency patterns from intelligent infrastructure outputs."""

from __future__ import annotations
from pathlib import Path
from statistics import mean
import csv

ROOT = Path(__file__).resolve().parents[1]
TABLES = ROOT / "outputs" / "tables"


def main() -> None:
    path = TABLES / "intelligent_infrastructure_timeseries.csv"
    if not path.exists():
        raise FileNotFoundError("Missing intelligent_infrastructure_timeseries.csv. Run the main Python workflow first.")
    with path.open("r", newline="", encoding="utf-8") as handle:
        rows = list(csv.DictReader(handle))
    final_year = max(int(row["year"]) for row in rows)
    final_rows = [row for row in rows if int(row["year"]) == final_year]
    groups = sorted({(row["scenario"], row["category"]) for row in final_rows})
    out = []
    for scenario, category in groups:
        subset = [row for row in final_rows if row["scenario"] == scenario and row["category"] == category]
        avg_dependency = mean(float(row["cyber_physical_dependency"]) for row in subset)
        avg_risk = mean(float(row["risk_score"]) for row in subset)
        out.append(
            {
                "scenario": scenario,
                "category": category,
                "average_cyber_physical_dependency": round(avg_dependency, 3),
                "average_risk_score": round(avg_risk, 3),
                "dependency_warning": "high" if avg_dependency >= 60 else "moderate" if avg_dependency >= 40 else "contained",
            }
        )
    with (TABLES / "cyber_physical_dependency_diagnostics.csv").open("w", newline="", encoding="utf-8") as handle:
        writer = csv.DictWriter(handle, fieldnames=list(out[0].keys()))
        writer.writeheader()
        writer.writerows(out)
    print(f"Wrote {TABLES / 'cyber_physical_dependency_diagnostics.csv'}")


if __name__ == "__main__":
    main()
