#!/usr/bin/env python3
"""Evaluate whether governance quotas remain within replenishment capacity."""
from __future__ import annotations

import csv
from pathlib import Path

BASE = Path(__file__).resolve().parents[1]
DATA = BASE / "data"
OUT = BASE / "outputs" / "tables"
OUT.mkdir(parents=True, exist_ok=True)


def read_csv(path: Path) -> list[dict[str, str]]:
    with path.open(newline="") as handle:
        return list(csv.DictReader(handle))


def main() -> None:
    resources = {r["resource_id"]: r for r in read_csv(DATA / "synthetic_shared_resources.csv")}
    rules = read_csv(DATA / "synthetic_governance_rules.csv")
    rows = []
    for rule in rules:
        resource = resources[rule["resource_id"]]
        initial = float(resource["initial_stock"])
        capacity = float(resource["carrying_capacity"])
        regen = float(resource["regeneration_rate"]) * initial * max(0.0, 1.0 - initial / capacity)
        permitted_use = initial * 0.09 * float(rule["quota_multiplier"])
        rows.append(
            {
                "resource_id": rule["resource_id"],
                "scenario": rule["scenario"],
                "estimated_regeneration": round(regen, 3),
                "permitted_use": round(permitted_use, 3),
                "within_regeneration": permitted_use <= regen,
                "monitoring_strength": rule["monitoring_strength"],
                "sanction_strength": rule["sanction_strength"],
                "participation_score": rule["participation_score"],
            }
        )
    output = OUT / "quota_governance_assessment.csv"
    with output.open("w", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=list(rows[0].keys()))
        writer.writeheader()
        writer.writerows(rows)
    print(f"Wrote {output}")


if __name__ == "__main__":
    main()
