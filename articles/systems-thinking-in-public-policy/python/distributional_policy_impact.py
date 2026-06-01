"""Distributional policy impact analysis.

Computes net policy impact as benefits minus burdens and risks, while preserving
access-score context for equity-centered interpretation.
"""
from __future__ import annotations
from _policy_utils import DATA, OUT_TABLES, ensure_outputs, read_csv_dict, to_float, write_csv_dict


def main() -> None:
    ensure_outputs()
    rows = read_csv_dict(DATA / "synthetic_distributional_impacts.csv", ["group", "benefits", "burdens", "risks", "access_score"])
    out = []
    for row in rows:
        benefits = to_float(row, "benefits")
        burdens = to_float(row, "burdens")
        risks = to_float(row, "risks")
        access = to_float(row, "access_score")
        net = benefits - burdens - risks
        out.append({
            "group": row["group"],
            "benefits": benefits,
            "burdens": burdens,
            "risks": risks,
            "access_score": access,
            "net_policy_impact": round(net, 2),
            "equity_attention_flag": "urgent" if net < -40 or access < 40 else "monitor" if net < 0 else "favorable",
        })
    out.sort(key=lambda row: float(row["net_policy_impact"]))
    write_csv_dict(OUT_TABLES / "distributional_policy_impact.csv", out)
    print(f"Wrote {OUT_TABLES / 'distributional_policy_impact.csv'}")

if __name__ == "__main__":
    main()
