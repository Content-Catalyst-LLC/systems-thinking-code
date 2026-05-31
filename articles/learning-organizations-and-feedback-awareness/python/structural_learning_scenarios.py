from __future__ import annotations

from _common import f, read_csv, write_csv

rows = []
for row in read_csv("synthetic_model_runs.csv"):
    structural_score = (
        f(row["feedback_closure"]) * 0.25
        + f(row["blame_reduction"]) * 0.20
        + f(row["memory_investment"]) * 0.20
        + f(row["authority_connection"]) * 0.25
        + f(row["expected_learning_gain"]) * 0.10
    )
    rows.append({
        "run_id": row["run_id"],
        "scenario": row["scenario"],
        "structural_learning_score": round(structural_score, 4),
        "expected_learning_gain": row["expected_learning_gain"],
    })

path = write_csv("structural_learning_scenarios.csv", rows)
print(f"Wrote {path}")
