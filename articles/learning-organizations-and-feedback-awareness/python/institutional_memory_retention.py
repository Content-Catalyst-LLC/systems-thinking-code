from __future__ import annotations

from _common import f, read_csv, write_csv

rows = []
for row in read_csv("synthetic_memory_assets.csv"):
    assets = f(row["decision_records"]) + f(row["postmortems"]) + f(row["reused_lessons"]) + f(row["living_playbooks"]) + f(row["onboarding_links"])
    retained_memory = assets * (1 - f(row["knowledge_decay_risk"]))
    rows.append({
        "unit_id": row["unit_id"],
        "memory_asset_score": round(assets, 2),
        "knowledge_decay_risk": row["knowledge_decay_risk"],
        "retained_memory_index": round(retained_memory, 2),
    })

path = write_csv("institutional_memory_retention.csv", rows)
print(f"Wrote {path}")
