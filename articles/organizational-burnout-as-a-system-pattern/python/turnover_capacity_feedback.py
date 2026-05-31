from __future__ import annotations

from common import f, read_csv, write_csv

turnover = read_csv("synthetic_turnover_events.csv")
rows = []
for row in turnover:
    feedback_pressure = f(row, "remaining_staff_load_increase") + f(row, "knowledge_loss_index")
    rows.append(
        {
            "period": row["period"],
            "role_id": row["role_id"],
            "departures": row["departures"],
            "open_positions": row["open_positions"],
            "onboarding_hours": row["onboarding_hours"],
            "turnover_feedback_pressure": round(feedback_pressure, 3),
        }
    )
write_csv("turnover_capacity_feedback.csv", rows)
print("Wrote outputs/tables/turnover_capacity_feedback.csv")
