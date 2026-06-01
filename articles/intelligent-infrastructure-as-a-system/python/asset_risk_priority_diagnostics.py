#!/usr/bin/env python3
from __future__ import annotations

from pathlib import Path
import csv
from statistics import mean

ARTICLE_ROOT = Path(__file__).resolve().parents[1]
TABLES = ARTICLE_ROOT / "outputs" / "tables"
CORE = TABLES / "intelligent_infrastructure_timeseries.csv"
OUT = TABLES / "asset_risk_priority_diagnostics.csv"


def main() -> None:
    if not CORE.exists():
        print(f"Skipping asset diagnostics; missing {CORE}")
        return

    rows = list(csv.DictReader(CORE.open("r", encoding="utf-8")))
    final_year = max(int(r["year"]) for r in rows)
    final = [r for r in rows if int(r["year"]) == final_year]

    diagnostics = []
    for r in sorted(final, key=lambda x: float(x["risk_score"]), reverse=True):
        diagnostics.append({
            "scenario": r["scenario"],
            "asset_id": r["asset_id"],
            "category": r["category"],
            "risk_score": r["risk_score"],
            "resilience_score": r["resilience_score"],
            "equity_priority": r["equity_priority"],
            "maintenance_action_score": r["maintenance_action_score"],
            "priority_class": "urgent" if float(r["risk_score"]) >= 55 else "elevated" if float(r["risk_score"]) >= 42 else "routine"
        })

    OUT.parent.mkdir(parents=True, exist_ok=True)
    with OUT.open("w", newline="", encoding="utf-8") as handle:
        writer = csv.DictWriter(handle, fieldnames=list(diagnostics[0].keys()))
        writer.writeheader()
        writer.writerows(diagnostics)

    print(f"Wrote {OUT}")


if __name__ == "__main__":
    main()
