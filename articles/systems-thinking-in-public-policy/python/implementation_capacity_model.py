"""Implementation-capacity diagnostics for public institutions."""
from __future__ import annotations
from _policy_utils import DATA, OUT_TABLES, ensure_outputs, read_csv_dict, to_float, write_csv_dict

FIELDS = ["staffing", "knowledge", "data_systems", "institutional_memory", "authority"]


def main() -> None:
    ensure_outputs()
    rows = read_csv_dict(DATA / "synthetic_implementation_capacity.csv", ["agency", *FIELDS])
    out = []
    for row in rows:
        scores = {field: to_float(row, field) for field in FIELDS}
        score = sum(scores.values()) / len(scores)
        out.append({
            "agency": row["agency"],
            "implementation_capacity_score": round(score, 2),
            "lowest_capacity_component": min(scores, key=scores.get),
            "capacity_class": "stronger" if score >= 60 else "moderate" if score >= 50 else "fragile",
        })
    write_csv_dict(OUT_TABLES / "implementation_capacity_summary.csv", out)
    print(f"Wrote {OUT_TABLES / 'implementation_capacity_summary.csv'}")

if __name__ == "__main__":
    main()
