from __future__ import annotations

from _common import avg, f, read_csv, write_csv

rows = []
for row in read_csv("synthetic_public_institutions.csv"):
    governance_health = avg([
        f(row, "capacity_score"),
        f(row, "trust_score"),
        f(row, "coordination_score"),
        f(row, "memory_score"),
    ])
    rows.append({
        "institution_id": row["institution_id"],
        "domain": row["domain"],
        "institution_type": row["institution_type"],
        "governance_health_score": round(governance_health, 3),
    })

write_csv("governance_system_baseline.csv", rows)
