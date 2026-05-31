from __future__ import annotations

from _common import f, read_csv, write_csv

rows = []
for row in read_csv("synthetic_repeated_errors.csv"):
    prior = f(row, "prior_lesson_available")
    consulted = f(row, "lesson_consulted")
    repeat_count = f(row, "repeat_count")
    preventability = f(row, "preventability_score")
    risk = preventability * (1 + repeat_count * 0.12) * (1 - consulted * 0.35) * (1 + prior * 0.08)
    rows.append({
        "error_id": row["error_id"],
        "domain": row["domain"],
        "error_type": row["error_type"],
        "repeat_error_risk": round(min(risk, 1.0), 3),
    })

write_csv("repeated_mistake_risk.csv", rows)
