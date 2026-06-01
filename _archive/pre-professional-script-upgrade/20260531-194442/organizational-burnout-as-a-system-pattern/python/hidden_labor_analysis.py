from __future__ import annotations

from common import f, group_by, read_csv, write_csv

rows = read_csv("synthetic_hidden_labor.csv")
output = []
for role_id, items in group_by(rows, "role_id").items():
    totals = []
    for row in items:
        totals.append(
            f(row, "coordination_hours")
            + f(row, "emotional_labor_hours")
            + f(row, "informal_mentoring_hours")
            + f(row, "workaround_hours")
            + f(row, "unpaid_extra_hours")
        )
    output.append(
        {
            "role_id": role_id,
            "avg_hidden_labor_hours": round(sum(totals) / len(totals), 2),
            "latest_hidden_labor_hours": round(totals[-1], 2),
            "hidden_labor_growth": round(totals[-1] - totals[0], 2),
        }
    )
write_csv("hidden_labor_summary.csv", output)
print("Wrote outputs/tables/hidden_labor_summary.csv")
