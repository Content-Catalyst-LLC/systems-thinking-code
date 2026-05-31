from __future__ import annotations

from _common import f, read_csv, write_csv

rows = []
for row in read_csv("synthetic_turnover_events.csv"):
    turnover = f(row, "turnover_count")
    critical = f(row, "critical_role_departures")
    handoff = f(row, "handoff_quality")
    relationship_loss = f(row, "relationship_loss_score")
    memory_loss = (turnover * 0.12 + critical * 0.18 + relationship_loss * 0.25) * (1 - handoff * 0.65)
    rows.append({
        "period": row["period"],
        "team": row["team"],
        "memory_loss_index": round(memory_loss, 3),
        "handoff_quality": handoff,
    })

write_csv("turnover_knowledge_loss.csv", rows)
