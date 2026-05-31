from __future__ import annotations

from _common import f, read_csv, write_csv

rows = []
for row in read_csv("synthetic_model_runs.csv"):
    # Lower administrative burden is better, so invert it for the composite.
    composite = (
        (1 - f(row, "administrative_burden")) * 0.18
        + f(row, "trust_stock") * 0.18
        + f(row, "coordination_density") * 0.16
        + f(row, "institutional_capacity") * 0.17
        + f(row, "feedback_closure") * 0.16
        + f(row, "public_value_score") * 0.15
    )
    rows.append({
        "scenario": row["scenario"],
        "administrative_burden": row["administrative_burden"],
        "public_value_score": row["public_value_score"],
        "governance_redesign_score": round(composite, 3),
    })

write_csv("governance_redesign_scenarios.csv", rows)
