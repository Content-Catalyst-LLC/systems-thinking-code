#!/usr/bin/env python3
from __future__ import annotations

from pathlib import Path
import csv

ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "data"
OUTPUTS = ROOT / "outputs" / "tables"

def main() -> None:
    with (DATA / "synthetic_model_outputs.csv").open(newline="", encoding="utf-8") as f:
        rows = list(csv.DictReader(f))

    final_rows = [row for row in rows if row["year"] == "10"]
    scores = []
    for row in final_rows:
        capacity = float(row["system_capacity"])
        demand = float(row["system_demand"])
        trust = float(row["trust_stock"])
        risk = float(row["risk_stock"])
        score = (capacity / max(demand, 1)) * 40 + (trust / 100) * 35 + ((100 - risk) / 100) * 25
        scores.append({
            "scenario_id": row["scenario_id"],
            "robustness_score": round(score, 2),
            "capacity_demand_ratio": round(capacity / max(demand, 1), 3),
            "trust_stock": trust,
            "risk_stock": risk,
        })

    OUTPUTS.mkdir(parents=True, exist_ok=True)
    out = OUTPUTS / "robustness_assessment.csv"
    with out.open("w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=list(scores[0].keys()))
        writer.writeheader()
        writer.writerows(scores)

    print(f"Wrote {out}")

if __name__ == "__main__":
    main()
