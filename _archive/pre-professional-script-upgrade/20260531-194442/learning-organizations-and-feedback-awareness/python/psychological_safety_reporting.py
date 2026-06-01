from __future__ import annotations

from _common import f, read_csv, write_csv

rows = []
for row in read_csv("synthetic_psychological_safety_indicators.csv"):
    safety = (f(row["speak_up_score"]) + f(row["leader_response_score"]) + f(row["closure_score"])) / 3
    suppression = f(row["retaliation_fear"]) * (1 - safety)
    rows.append({
        "period": row["period"],
        "unit_id": row["unit_id"],
        "psychological_safety_index": round(safety, 4),
        "feedback_suppression_risk": round(suppression, 4),
        "reported_near_misses": row["reported_near_misses"],
    })

path = write_csv("psychological_safety_reporting.csv", rows)
print(f"Wrote {path}")
