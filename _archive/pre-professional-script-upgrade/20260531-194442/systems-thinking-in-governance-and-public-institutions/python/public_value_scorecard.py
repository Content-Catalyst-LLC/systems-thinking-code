from __future__ import annotations

from _common import avg, f, read_csv, write_csv

rows = []
for row in read_csv("synthetic_public_value_metrics.csv"):
    public_value = avg([
        f(row, "equity"),
        f(row, "access"),
        f(row, "service_quality"),
        f(row, "trust"),
        f(row, "resilience"),
        f(row, "sustainability"),
        f(row, "dignity"),
    ])
    rows.append({
        "metric_id": row["metric_id"],
        "domain": row["domain"],
        "public_value_score": round(public_value, 3),
    })

write_csv("public_value_scorecard.csv", rows)
