from __future__ import annotations

from _common import avg, f, read_csv, write_csv

rows = []
for row in read_csv("synthetic_capacity_stocks.csv"):
    capacity = avg([
        f(row, "staff_capacity"),
        f(row, "technical_capacity"),
        f(row, "memory_capacity"),
        f(row, "maintenance_capacity"),
        f(row, "coordination_capacity"),
        f(row, "public_trust_capacity"),
    ])
    rows.append({
        "period": row["period"],
        "domain": row["domain"],
        "institutional_capacity_score": round(capacity, 3),
    })

write_csv("institutional_capacity_model.csv", rows)
