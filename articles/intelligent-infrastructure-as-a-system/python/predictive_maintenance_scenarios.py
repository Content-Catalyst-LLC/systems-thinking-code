#!/usr/bin/env python3
from __future__ import annotations

from pathlib import Path
import csv
from statistics import mean

ARTICLE_ROOT = Path(__file__).resolve().parents[1]
TABLES = ARTICLE_ROOT / "outputs" / "tables"
CORE = TABLES / "intelligent_infrastructure_timeseries.csv"
OUT = TABLES / "predictive_maintenance_scenario_summary.csv"


def main() -> None:
    if not CORE.exists():
        print(f"Skipping maintenance scenarios; missing {CORE}")
        return

    rows = list(csv.DictReader(CORE.open("r", encoding="utf-8")))
    scenarios = sorted(set(r["scenario"] for r in rows))
    output = []

    for scenario in scenarios:
        subset = [r for r in rows if r["scenario"] == scenario]
        average_maintenance = mean(float(r["maintenance_action_score"]) for r in subset)
        average_risk = mean(float(r["risk_score"]) for r in subset)
        average_condition = mean(float(r["condition"]) for r in subset)
        output.append({
            "scenario": scenario,
            "average_maintenance_action_score": round(average_maintenance, 3),
            "average_risk_score": round(average_risk, 3),
            "average_asset_condition": round(average_condition, 3),
            "diagnostic": "maintenance capacity aligned with risk" if average_maintenance >= average_risk else "maintenance capacity lags risk"
        })

    with OUT.open("w", newline="", encoding="utf-8") as handle:
        writer = csv.DictWriter(handle, fieldnames=list(output[0].keys()))
        writer.writeheader()
        writer.writerows(output)

    print(f"Wrote {OUT}")


if __name__ == "__main__":
    main()
