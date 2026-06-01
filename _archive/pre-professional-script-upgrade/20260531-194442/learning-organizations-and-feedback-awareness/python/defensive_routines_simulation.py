from __future__ import annotations

from _common import f, read_csv, write_csv

rows = []
for row in read_csv("synthetic_defensive_routines.csv"):
    defensive_load = sum(f(row[col]) for col in ["blame_language", "polished_reporting", "avoided_topics", "ritual_meetings", "action_items_without_change"])
    learning_blockage = defensive_load / 50
    rows.append({
        "period": row["period"],
        "unit_id": row["unit_id"],
        "defensive_load": round(defensive_load, 2),
        "learning_blockage_index": round(learning_blockage, 4),
    })

path = write_csv("defensive_routines_simulation.csv", rows)
print(f"Wrote {path}")
