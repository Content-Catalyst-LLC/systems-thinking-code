"""Professional administrative-burden diagnostics.

Computes a group-level burden index and identifies the primary burden driver.
"""
from __future__ import annotations
from _policy_utils import DATA, OUT_TABLES, ensure_outputs, read_csv_dict, to_float, write_csv_dict

COST_FIELDS = ["learning_cost", "compliance_cost", "psychological_cost", "digital_cost", "appeal_burden"]


def main() -> None:
    ensure_outputs()
    rows = read_csv_dict(DATA / "synthetic_administrative_burden.csv", ["group", *COST_FIELDS])
    diagnostics = []
    for row in rows:
        costs = {field: to_float(row, field) for field in COST_FIELDS}
        burden_index = sum(costs.values()) / len(costs)
        diagnostics.append({
            "group": row["group"],
            "burden_index": round(burden_index, 2),
            "highest_cost_component": max(costs, key=costs.get),
            "access_risk_flag": "high" if burden_index >= 55 else "moderate" if burden_index >= 35 else "lower",
        })
    write_csv_dict(OUT_TABLES / "administrative_burden_index.csv", diagnostics)
    print(f"Wrote {OUT_TABLES / 'administrative_burden_index.csv'}")

if __name__ == "__main__":
    main()
