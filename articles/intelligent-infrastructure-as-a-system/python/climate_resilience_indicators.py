#!/usr/bin/env python3
from __future__ import annotations

from pathlib import Path
import csv
from statistics import mean

ARTICLE_ROOT = Path(__file__).resolve().parents[1]
TABLES = ARTICLE_ROOT / "outputs" / "tables"
CORE = TABLES / "intelligent_infrastructure_timeseries.csv"
OUT = TABLES / "climate_resilience_diagnostics.csv"


def main() -> None:
    if not CORE.exists():
        print(f"Skipping climate resilience diagnostics; missing {CORE}")
        return

    rows = list(csv.DictReader(CORE.open("r", encoding="utf-8")))
    final_year = max(int(r["year"]) for r in rows)
    final = [r for r in rows if int(r["year"]) == final_year]

    output = []
    for scenario in sorted(set(r["scenario"] for r in final)):
        subset = [r for r in final if r["scenario"] == scenario]
        vulnerable = [r for r in subset if float(r["equity_priority"]) >= 75]
        output.append({
            "scenario": scenario,
            "average_resilience_score": round(mean(float(r["resilience_score"]) for r in subset), 3),
            "vulnerable_high_priority_asset_count": len(vulnerable),
            "average_risk_for_high_equity_assets": round(mean(float(r["risk_score"]) for r in vulnerable), 3) if vulnerable else 0,
            "diagnostic": "equity-priority climate resilience review needed" if vulnerable and mean(float(r["risk_score"]) for r in vulnerable) >= 42 else "equity-priority assets comparatively stable"
        })

    with OUT.open("w", newline="", encoding="utf-8") as handle:
        writer = csv.DictWriter(handle, fieldnames=list(output[0].keys()))
        writer.writeheader()
        writer.writerows(output)

    print(f"Wrote {OUT}")


if __name__ == "__main__":
    main()
