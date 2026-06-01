from __future__ import annotations

from common import read_csv, write_csv, clamp


def main() -> None:
    rows = []
    for row in read_csv("synthetic_burnout_indicators.csv"):
        overtime = float(row["overtime_hours"])
        recovery = float(row["recovery_hours"])
        turnover = float(row["turnover_risk"])
        error = float(row["error_rate"])
        safety = float(row["psychological_safety"])
        burnout_index = clamp((overtime / 50.0) + turnover + error - (recovery / 80.0) - (safety * 0.20))
        rows.append({
            "period": row["period"],
            "team_id": row["team_id"],
            "burnout_index": round(burnout_index, 3),
            "interpretation": "critical" if burnout_index > 0.75 else "high" if burnout_index > 0.55 else "elevated",
        })
    out = write_csv("burnout_feedback_summary.csv", rows, ["period", "team_id", "burnout_index", "interpretation"])
    print(f"Wrote {out}")


if __name__ == "__main__":
    main()
