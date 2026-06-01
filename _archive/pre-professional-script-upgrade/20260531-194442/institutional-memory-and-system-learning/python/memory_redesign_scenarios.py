from __future__ import annotations

from _common import f, read_csv, write_csv

rows = []
for row in read_csv("synthetic_model_runs.csv"):
    learning_effectiveness = (f(row, "projected_memory_score") + f(row, "feedback_closure") + f(row, "authority_connection")) / 3
    rows.append({
        "scenario": row["scenario"],
        "projected_memory_score": row["projected_memory_score"],
        "projected_repeat_error_risk": row["projected_repeat_error_risk"],
        "learning_effectiveness": round(learning_effectiveness, 3),
    })

write_csv("memory_redesign_scenarios.csv", rows)
