from __future__ import annotations

from common import read_csv, write_csv


def main() -> None:
    teams = {row["team_id"]: row for row in read_csv("synthetic_teams.csv")}
    events = read_csv("synthetic_workload_events.csv")
    rows = []
    for event in events:
        team = teams[event["team_id"]]
        capacity = float(team["baseline_capacity"])
        workload = float(event["new_work"]) + float(event["urgent_work"]) + float(event["rework"])
        meeting_drag = float(event["meetings_hours"]) * 0.4
        effective_capacity = max(1.0, capacity - meeting_drag)
        pressure = workload / effective_capacity
        rows.append({
            "period": event["period"],
            "team_id": event["team_id"],
            "team_name": team["team_name"],
            "workload": round(workload, 2),
            "effective_capacity": round(effective_capacity, 2),
            "pressure_ratio": round(pressure, 3),
            "risk_flag": "high" if pressure > 1.55 else "moderate" if pressure > 1.25 else "watch",
        })
    out = write_csv("workload_capacity_summary.csv", rows, ["period", "team_id", "team_name", "workload", "effective_capacity", "pressure_ratio", "risk_flag"])
    print(f"Wrote {out}")


if __name__ == "__main__":
    main()
