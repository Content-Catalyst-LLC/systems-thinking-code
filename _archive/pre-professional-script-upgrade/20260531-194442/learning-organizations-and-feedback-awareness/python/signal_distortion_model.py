from __future__ import annotations

from _common import f, read_csv, write_csv

rows = []
for row in read_csv("synthetic_feedback_signals.csv"):
    distortion = 1 - (f(row["signal_quality"]) * f(row["timeliness"]) * f(row["authority_connection"]))
    received_signal = f(row["raw_feedback"]) * (1 - distortion)
    rows.append({
        "period": row["period"],
        "unit_id": row["unit_id"],
        "raw_feedback": row["raw_feedback"],
        "estimated_distortion": round(distortion, 4),
        "received_signal": round(received_signal, 4),
    })

path = write_csv("signal_distortion_model.csv", rows)
print(f"Wrote {path}")
