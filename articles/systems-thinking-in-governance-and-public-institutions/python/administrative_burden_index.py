from __future__ import annotations

from _common import f, read_csv, write_csv

rows = []
for row in read_csv("synthetic_administrative_burden.csv"):
    burden = (
        f(row, "learning_cost") * 0.22
        + f(row, "compliance_cost") * 0.24
        + f(row, "psychological_cost") * 0.20
        + f(row, "digital_burden") * 0.17
        + f(row, "appeal_burden") * 0.17
    ) * (1 - f(row, "support_available") * 0.25)
    rows.append({
        "case_id": row["case_id"],
        "program": row["program"],
        "group": row["group"],
        "administrative_burden_index": round(burden, 3),
    })

write_csv("administrative_burden_index.csv", rows)
