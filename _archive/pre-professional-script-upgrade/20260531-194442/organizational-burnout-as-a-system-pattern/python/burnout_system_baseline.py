from __future__ import annotations

from common import f, group_by, read_csv, write_csv

workload = read_csv("synthetic_workload_events.csv")
hidden = read_csv("synthetic_hidden_labor.csv")
risk = read_csv("synthetic_burnout_risk.csv")

hidden_by_key = {(r["period"], r["role_id"]): r for r in hidden}
risk_by_key = {(r["period"], r["role_id"]): r for r in risk}

rows = []
for row in workload:
    key = (row["period"], row["role_id"])
    hidden_row = hidden_by_key[key]
    risk_row = risk_by_key[key]
    total_work = (
        f(row, "visible_workload")
        + f(row, "meeting_load")
        + f(row, "rework_hours")
        + f(hidden_row, "coordination_hours")
        + f(hidden_row, "emotional_labor_hours")
        + f(hidden_row, "workaround_hours")
        + f(hidden_row, "unpaid_extra_hours")
    )
    pressure = total_work / max(f(row, "capacity_index"), 1.0)
    rows.append(
        {
            "period": row["period"],
            "role_id": row["role_id"],
            "total_modeled_work": round(total_work, 2),
            "capacity_index": row["capacity_index"],
            "pressure_index": round(pressure, 3),
            "burnout_risk_proxy": risk_row["reported_stress"],
            "quality_risk": risk_row["quality_risk"],
        }
    )

write_csv("burnout_system_baseline.csv", rows)

summary = []
for role_id, items in group_by(rows, "role_id").items():
    summary.append(
        {
            "role_id": role_id,
            "avg_pressure_index": round(sum(float(x["pressure_index"]) for x in items) / len(items), 3),
            "max_pressure_index": round(max(float(x["pressure_index"]) for x in items), 3),
            "latest_quality_risk": items[-1]["quality_risk"],
        }
    )
write_csv("burnout_system_summary.csv", summary)
print("Wrote outputs/tables/burnout_system_baseline.csv and burnout_system_summary.csv")
