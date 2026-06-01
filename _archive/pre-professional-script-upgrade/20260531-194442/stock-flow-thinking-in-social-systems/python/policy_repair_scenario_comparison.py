"""Compare social repair policy scenarios using synthetic policy assumptions."""

from __future__ import annotations

import csv
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "data" / "synthetic_policy_scenarios.csv"
OUT = ROOT / "outputs" / "tables"
OUT.mkdir(parents=True, exist_ok=True)


def run_scenario(row: dict[str, str], months: int = 18) -> list[dict[str, float | str]]:
    trust = 42.0
    burden = 18.0
    capacity = 55.0
    results = []
    trust_repair = float(row["trust_repair_rate"])
    burden_reduction = float(row["burden_reduction_rate"])
    capacity_investment = float(row["capacity_investment_rate"])
    harm_reduction = float(row["harm_reduction_rate"])
    for month in range(months + 1):
        results.append({
            "scenario_id": row["scenario_id"],
            "month": month,
            "trust": round(trust, 2),
            "burden": round(burden, 2),
            "capacity": round(capacity, 2),
        })
        trust = min(100.0, max(0.0, trust + trust_repair + harm_reduction - 2.2))
        burden = max(0.0, burden + 2.0 - burden_reduction)
        capacity = max(0.0, capacity + capacity_investment - 0.7)
    return results


if __name__ == "__main__":
    rows = []
    with DATA.open() as f:
        for row in csv.DictReader(f):
            rows.extend(run_scenario(row))
    path = OUT / "policy_repair_scenario_comparison.csv"
    with path.open("w", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=rows[0].keys())
        writer.writeheader()
        writer.writerows(rows)
    print(f"Wrote {path}")
