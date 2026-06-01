"""Buffer and resilience diagnostics."""
from __future__ import annotations

from pathlib import Path
import csv

ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "data" / "processed"
OUT = ROOT / "outputs" / "tables"


def main() -> None:
    OUT.mkdir(parents=True, exist_ok=True)
    latest_by_domain: dict[str, dict[str, str]] = {}
    with (DATA / "indicators.csv").open(newline="") as f:
        for row in csv.DictReader(f):
            latest_by_domain[row["domain"]] = row
    rows = []
    for domain, row in latest_by_domain.items():
        buffer_level = float(row["buffer_level"])
        collapse_risk = float(row["collapse_risk"])
        rows.append({
            "domain": domain,
            "latest_month": row["month"],
            "buffer_level": buffer_level,
            "collapse_risk": collapse_risk,
            "diagnostic": "urgent_rebuild" if buffer_level < 0.34 or collapse_risk > 0.60 else "monitor_and_restore",
        })
    out_path = OUT / "buffer_resilience_diagnostics.csv"
    with out_path.open("w", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=list(rows[0].keys()))
        writer.writeheader()
        writer.writerows(rows)
    print(f"Wrote {out_path}")


if __name__ == "__main__":
    main()
