from __future__ import annotations

from common import f, group_by, read_csv, write_csv

rows = read_csv("synthetic_workload_events.csv")
output = []
for role_id, items in group_by(rows, "role_id").items():
    items = sorted(items, key=lambda r: int(r["period"]))
    first = items[0]
    last = items[-1]
    demand_first = f(first, "visible_workload") + f(first, "meeting_load") + f(first, "rework_hours")
    demand_last = f(last, "visible_workload") + f(last, "meeting_load") + f(last, "rework_hours")
    cap_change = f(last, "capacity_index") - f(first, "capacity_index")
    output.append(
        {
            "role_id": role_id,
            "initial_visible_demand": round(demand_first, 2),
            "latest_visible_demand": round(demand_last, 2),
            "demand_change": round(demand_last - demand_first, 2),
            "capacity_change": round(cap_change, 2),
            "capacity_warning": "yes" if cap_change < -10 else "monitor",
        }
    )
write_csv("workload_capacity_change.csv", output)
print("Wrote outputs/tables/workload_capacity_change.csv")
