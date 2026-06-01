#!/usr/bin/env python3
from __future__ import annotations

from pathlib import Path
import csv
from statistics import mean

ARTICLE_ROOT = Path(__file__).resolve().parents[1]
TABLES = ARTICLE_ROOT / "outputs" / "tables"
CORE = TABLES / "intelligent_infrastructure_timeseries.csv"
OUT = TABLES / "cyber_physical_dependency_diagnostics.csv"


def main() -> None:
    if not CORE.exists():
        print(f"Skipping cyber-physical diagnostics; missing {CORE}")
        return

    rows = list(csv.DictReader(CORE.open("r", encoding="utf-8")))
    final_year = max(int(r["year"]) for r in rows)
    final = [r for r in rows if int(r["year"]) == final_year]

    output = []
    for scenario in sorted(set(r["scenario"] for r in final)):
        subset = [r for r in final if r["scenario"] == scenario]
        high_dependency = [r for r in subset if float(r["cyber_physical_dependency"]) >= 60]
        output.append({
            "scenario": scenario,
            "average_cyber_physical_dependency": round(mean(float(r["cyber_physical_dependency"]) for r in subset), 3),
            "high_dependency_asset_count": len(high_dependency),
            "highest_dependency_asset": max(subset, key=lambda r: float(r["cyber_physical_dependency"]))["asset_id"],
            "diagnostic": "digital fragility requires review" if len(high_dependency) >= 2 else "cyber-physical dependency comparatively contained"
        })

    with OUT.open("w", newline="", encoding="utf-8") as handle:
        writer = csv.DictWriter(handle, fieldnames=list(output[0].keys()))
        writer.writeheader()
        writer.writerows(output)

    print(f"Wrote {OUT}")


if __name__ == "__main__":
    main()
