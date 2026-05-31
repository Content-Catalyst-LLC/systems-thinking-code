from __future__ import annotations

from common import f, read_csv, write_csv

scenarios = read_csv("synthetic_redesign_scenarios.csv")
outputs = read_csv("synthetic_outputs.csv")
out_by_id = {row["scenario_id"]: row for row in outputs}
rows = []
for row in scenarios:
    out = out_by_id[row["scenario_id"]]
    redesign_strength = (
        f(row, "workload_reduction")
        + f(row, "capacity_increase")
        + f(row, "recovery_increase")
        + f(row, "rework_reduction")
        + f(row, "hidden_labor_visibility")
    ) / 5
    rows.append(
        {
            "scenario_id": row["scenario_id"],
            "scenario_name": row["scenario_name"],
            "redesign_strength": round(redesign_strength, 3),
            "expected_burnout_reduction": row["expected_burnout_reduction"],
            "projected_burnout_risk": out["projected_burnout_risk"],
            "projected_memory_fragility": out["projected_memory_fragility"],
        }
    )
write_csv("burnout_redesign_scenarios.csv", rows)
print("Wrote outputs/tables/burnout_redesign_scenarios.csv")
