#!/usr/bin/env python3
"""Simple free-riding and cooperation scoring for commons users."""
from __future__ import annotations

import csv
from pathlib import Path

BASE = Path(__file__).resolve().parents[1]
DATA = BASE / "data"
OUT = BASE / "outputs" / "tables"
OUT.mkdir(parents=True, exist_ok=True)


def main() -> None:
    with (DATA / "synthetic_resource_users.csv").open(newline="") as handle:
        users = list(csv.DictReader(handle))
    rows = []
    for user in users:
        baseline_use = float(user["baseline_use"])
        compliance = float(user["governance_compliance"])
        power = float(user["relative_power"])
        benefit = float(user["private_benefit_per_unit"])
        cost = float(user["private_cost_per_unit"])
        free_riding_risk = (1.0 - compliance) * power * baseline_use / 100.0
        private_margin = benefit - cost
        rows.append(
            {
                "user_id": user["user_id"],
                "user_group": user["user_group"],
                "resource_id": user["resource_id"],
                "private_margin": round(private_margin, 3),
                "free_riding_risk": round(free_riding_risk, 3),
                "cooperation_score": round(compliance * (1.0 - min(1.0, free_riding_risk)), 3),
            }
        )
    output = OUT / "free_riding_and_cooperation_scores.csv"
    with output.open("w", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=list(rows[0].keys()))
        writer.writeheader()
        writer.writerows(rows)
    print(f"Wrote {output}")


if __name__ == "__main__":
    main()
