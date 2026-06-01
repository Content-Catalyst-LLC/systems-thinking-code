from __future__ import annotations

from _common import avg, f, read_csv, write_csv

assets = read_csv("synthetic_memory_assets.csv")
rows = []
for row in assets:
    memory_score = avg([
        f(row, "freshness_score"),
        f(row, "accessibility_score"),
        f(row, "context_score"),
        f(row, "authority_link_score"),
    ])
    rows.append({
        "asset_id": row["asset_id"],
        "asset_type": row["asset_type"],
        "domain": row["domain"],
        "memory_score": round(memory_score, 3),
    })

write_csv("institutional_memory_baseline.csv", rows)
