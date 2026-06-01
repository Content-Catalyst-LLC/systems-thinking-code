from __future__ import annotations

from common import f, read_csv, write_csv

workload = read_csv("synthetic_workload_events.csv")
recovery = read_csv("synthetic_recovery_indicators.csv")
rec_by_key = {(r["period"], r["role_id"]): r for r in recovery}
rows = []
for row in workload:
    rec = rec_by_key[(row["period"], row["role_id"])]
    demand = f(row, "visible_workload") + f(row, "meeting_load") + f(row, "rework_hours")
    recovery_supply = f(rec, "protected_focus_hours") + f(rec, "recovery_hours") + f(rec, "training_hours")
    deficit = max(0.0, demand * 0.35 - recovery_supply)
    rows.append(
        {
            "period": row["period"],
            "role_id": row["role_id"],
            "demand_proxy": round(demand, 2),
            "recovery_supply": round(recovery_supply, 2),
            "recovery_deficit": round(deficit, 2),
            "autonomy_score": rec["autonomy_score"],
            "peer_support_score": rec["peer_support_score"],
        }
    )
write_csv("recovery_deficit_simulation.csv", rows)
print("Wrote outputs/tables/recovery_deficit_simulation.csv")
