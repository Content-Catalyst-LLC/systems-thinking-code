#!/usr/bin/env python3
"""Create climate and resilience diagnostics for intelligent infrastructure scenarios."""

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
    scenarios = sorted({row["scenario"] for row in final_rows})
    out = []
    for scenario in scenarios:
        subset = [row for row in final_rows if row["scenario"] == scenario]
        vulnerable_assets = [row for row in subset if float(row["equity_priority"]) >= 75]
        out.append(
            {
                "scenario": scenario,
                "average_resilience_all_assets": round(mean(float(row["resilience_score"]) for row in subset), 3),
                "average_resilience_high_equity_priority_assets": round(mean(float(row["resilience_score"]) for row in vulnerable_assets), 3) if vulnerable_assets else "NA",
                "average_risk_high_equity_priority_assets": round(mean(float(row["risk_score"]) for row in vulnerable_assets), 3) if vulnerable_assets else "NA",
                "high_equity_priority_asset_count": len(vulnerable_assets),
            }
        )
    with (TABLES / "climate_resilience_diagnostics.csv").open("w", newline="", encoding="utf-8") as handle:
        writer = csv.DictWriter(handle, fieldnames=list(out[0].keys()))
        writer.writeheader()
        writer.writerows(out)
    print(f"Wrote {TABLES / 'climate_resilience_diagnostics.csv'}")


if __name__ == "__main__":
    main()
