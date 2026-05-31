#!/usr/bin/env python3
"""Estimate restoration pathways for depleted commons stocks."""
from __future__ import annotations

import csv
from pathlib import Path

BASE = Path(__file__).resolve().parents[1]
DATA = BASE / "data"
OUT = BASE / "outputs" / "tables"
OUT.mkdir(parents=True, exist_ok=True)


def read_csv(name: str) -> list[dict[str, str]]:
    with (DATA / name).open(newline="") as handle:
        return list(csv.DictReader(handle))


def main() -> None:
    resources = {r["resource_id"]: r for r in read_csv("synthetic_shared_resources.csv")}
    actions = read_csv("synthetic_restoration_actions.csv")
    rows = []
    for action in actions:
        resource = resources[action["resource_id"]]
        initial = float(resource["initial_stock"])
        target = initial * 0.90
        depleted = initial * 0.45
        recovery_rate = float(action["expected_recovery_rate"])
        delay = int(action["implementation_delay"])
        stock = depleted
        year = 0
        while stock < target and year < 50:
            if year >= delay:
                stock += (target - stock) * recovery_rate
            year += 1
        rows.append(
            {
                "resource_id": action["resource_id"],
                "action_name": action["action_name"],
                "starting_stock": round(depleted, 2),
                "target_stock": round(target, 2),
                "years_to_target": year,
                "distributional_priority": action["distributional_priority"],
            }
        )
    output = OUT / "restoration_pathway_estimates.csv"
    with output.open("w", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=list(rows[0].keys()))
        writer.writeheader()
        writer.writerows(rows)
    print(f"Wrote {output}")


if __name__ == "__main__":
    main()
