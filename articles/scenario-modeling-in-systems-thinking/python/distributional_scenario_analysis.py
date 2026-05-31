#!/usr/bin/env python3
from __future__ import annotations

from pathlib import Path
import csv
from collections import defaultdict

ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "data"
OUTPUTS = ROOT / "outputs" / "tables"

def main() -> None:
    with (DATA / "synthetic_distributional_outcomes.csv").open(newline="", encoding="utf-8") as f:
        rows = list(csv.DictReader(f))

    by_scenario = defaultdict(list)
    for row in rows:
        by_scenario[row["scenario_id"]].append(row)

    summary = []
    for scenario_id, items in by_scenario.items():
        access_values = [float(x["access_index"]) for x in items]
        burden_values = [float(x["burden_index"]) for x in items]
        risk_values = [float(x["risk_index"]) for x in items]
        summary.append({
            "scenario_id": scenario_id,
            "access_gap": round(max(access_values) - min(access_values), 3),
            "burden_gap": round(max(burden_values) - min(burden_values), 3),
            "risk_gap": round(max(risk_values) - min(risk_values), 3),
        })

    OUTPUTS.mkdir(parents=True, exist_ok=True)
    out = OUTPUTS / "distributional_gap_summary.csv"
    with out.open("w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=list(summary[0].keys()))
        writer.writeheader()
        writer.writerows(summary)

    print(f"Wrote {out}")

if __name__ == "__main__":
    main()
