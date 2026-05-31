from __future__ import annotations

from _common import f, read_csv, write_csv

rows = []
for row in read_csv("synthetic_feedback_signals.csv"):
    usable_feedback = f(row["raw_feedback"]) * f(row["signal_quality"]) * f(row["timeliness"]) * f(row["authority_connection"])
    rows.append({
        "period": row["period"],
        "unit_id": row["unit_id"],
        "unit_name": row["unit_name"],
        "usable_feedback_index": round(usable_feedback, 4),
        "feedback_burden": row["feedback_burden"],
    })

path = write_csv("feedback_awareness_baseline.csv", rows)
print(f"Wrote {path}")
