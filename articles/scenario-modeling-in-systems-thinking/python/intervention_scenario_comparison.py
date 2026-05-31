#!/usr/bin/env python3
from __future__ import annotations

from pathlib import Path
import csv

ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "data"
OUTPUTS = ROOT / "outputs" / "tables"

def read_csv(name: str) -> list[dict[str, str]]:
    with (DATA / name).open(newline="", encoding="utf-8") as f:
        return list(csv.DictReader(f))

def main() -> None:
    scenarios = {row["scenario_id"]: row for row in read_csv("synthetic_scenario_definitions.csv")}
    interventions = read_csv("synthetic_interventions.csv")
    OUTPUTS.mkdir(parents=True, exist_ok=True)

    rows = []
    for item in interventions:
        scenario = scenarios[item["scenario_id"]]
        score = (
            float(item["capacity_boost"]) * 40
            + float(item["burden_reduction"]) * 35
            + float(item["repair_flow"]) * 25
        )
        rows.append({
            "scenario_id": item["scenario_id"],
            "scenario_name": scenario["scenario_name"],
            "intervention_id": item["intervention_id"],
            "start_year": item["start_year"],
            "illustrative_intervention_score": round(score, 3),
        })

    out = OUTPUTS / "intervention_scenario_comparison.csv"
    with out.open("w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=list(rows[0].keys()))
        writer.writeheader()
        writer.writerows(rows)

    print(f"Wrote {out}")

if __name__ == "__main__":
    main()
