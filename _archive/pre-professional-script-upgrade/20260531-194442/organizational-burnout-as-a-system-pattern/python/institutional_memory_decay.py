from __future__ import annotations

from common import f, read_csv, write_csv

memory = read_csv("synthetic_memory_assets.csv")
rows = []
for row in memory:
    preservation = (
        f(row, "decision_records") * 0.02
        + f(row, "active_playbooks") * 0.04
        + f(row, "mentoring_coverage") * 0.25
        + f(row, "cross_training_score") * 0.25
        + f(row, "documentation_freshness") * 0.25
    )
    fragility = f(row, "memory_fragility")
    rows.append(
        {
            "role_id": row["role_id"],
            "memory_preservation_score": round(preservation, 3),
            "memory_fragility": fragility,
            "memory_risk": "high" if fragility > 0.62 else "moderate",
        }
    )
write_csv("institutional_memory_decay.csv", rows)
print("Wrote outputs/tables/institutional_memory_decay.csv")
