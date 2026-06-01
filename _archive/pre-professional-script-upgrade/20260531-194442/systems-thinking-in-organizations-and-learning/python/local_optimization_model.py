from __future__ import annotations

from common import read_csv, write_csv


def main() -> None:
    rows = []
    for row in read_csv("synthetic_workload_events.csv"):
        new_work = float(row["new_work"])
        rework = float(row["rework"])
        urgent = float(row["urgent_work"])
        local_throughput_score = new_work / (new_work + urgent + 1.0)
        whole_system_cost = (rework * 1.7) + (urgent * 0.6) + (float(row["meetings_hours"]) * 0.3)
        rows.append({
            "period": row["period"],
            "team_id": row["team_id"],
            "local_throughput_score": round(local_throughput_score, 3),
            "whole_system_cost_index": round(whole_system_cost, 2),
            "redesign_need": "high" if whole_system_cost > 60 else "moderate" if whole_system_cost > 45 else "watch",
        })
    out = write_csv("local_optimization_summary.csv", rows, ["period", "team_id", "local_throughput_score", "whole_system_cost_index", "redesign_need"])
    print(f"Wrote {out}")


if __name__ == "__main__":
    main()
