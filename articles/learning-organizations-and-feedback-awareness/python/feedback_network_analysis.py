from __future__ import annotations

from _common import f, read_csv, write_csv

rows = []
for row in read_csv("synthetic_feedback_channels.csv"):
    channel_value = f(row["signal_richness"]) * f(row["decision_proximity"]) * f(row["closure_quality"])
    risk_adjusted_value = channel_value * (1 - f(row["retaliation_risk"]))
    rows.append({
        "channel_id": row["channel_id"],
        "channel_name": row["channel_name"],
        "formality": row["formality"],
        "channel_value": round(channel_value, 4),
        "risk_adjusted_value": round(risk_adjusted_value, 4),
    })

path = write_csv("feedback_network_analysis.csv", rows)
print(f"Wrote {path}")
