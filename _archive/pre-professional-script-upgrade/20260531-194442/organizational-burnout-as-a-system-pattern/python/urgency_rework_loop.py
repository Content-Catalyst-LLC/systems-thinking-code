from __future__ import annotations

from common import f, read_csv, write_csv

rows = read_csv("synthetic_workload_events.csv")
output = []
for row in rows:
    urgency = f(row, "urgent_requests")
    rework = f(row, "rework_hours")
    ratio = rework / max(urgency, 1.0)
    output.append(
        {
            "period": row["period"],
            "role_id": row["role_id"],
            "urgent_requests": urgency,
            "rework_hours": rework,
            "rework_per_urgent_request": round(ratio, 3),
            "loop_warning": "high" if ratio > 0.7 else "moderate",
        }
    )
write_csv("urgency_rework_loop.csv", output)
print("Wrote outputs/tables/urgency_rework_loop.csv")
