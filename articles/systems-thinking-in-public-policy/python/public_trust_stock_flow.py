"""Public trust stock-flow diagnostics for policy legitimacy."""
from __future__ import annotations
from _policy_utils import DATA, OUT_TABLES, clamp, ensure_outputs, read_csv_dict, to_float, write_csv_dict


def main() -> None:
    ensure_outputs()
    rows = read_csv_dict(DATA / "synthetic_trust_indicators.csv", ["year", "reliability", "fairness", "accountability", "burden", "opacity"])
    trust_stock = 50.0
    out = []
    for row in rows:
        inflow = (to_float(row, "reliability") + to_float(row, "fairness") + to_float(row, "accountability")) / 150.0
        outflow = (to_float(row, "burden") + to_float(row, "opacity")) / 180.0
        trust_stock = clamp(trust_stock + inflow - outflow)
        out.append({
            "year": row["year"],
            "trust_stock": round(trust_stock, 3),
            "trust_inflow": round(inflow, 3),
            "trust_outflow": round(outflow, 3),
        })
    write_csv_dict(OUT_TABLES / "public_trust_stock_flow.csv", out)
    print(f"Wrote {OUT_TABLES / 'public_trust_stock_flow.csv'}")

if __name__ == "__main__":
    main()
