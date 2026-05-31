from __future__ import annotations

from _common import avg, f, read_csv, write_csv

rows = []
for row in read_csv("synthetic_documentation_quality.csv"):
    freshness = max(0.0, 1 - min(f(row, "last_review_months"), 24) / 24)
    quality = avg([
        f(row, "completeness"),
        f(row, "searchability"),
        f(row, "ownership_defined"),
        freshness,
        f(row, "decision_rationale"),
        f(row, "context_preserved"),
    ])
    rows.append({
        "asset_id": row["asset_id"],
        "documentation_quality_score": round(quality, 3),
        "update_status": row["update_status"],
    })

write_csv("documentation_quality_score.csv", rows)
