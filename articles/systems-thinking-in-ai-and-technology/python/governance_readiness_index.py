"""Governance readiness and contestability diagnostics."""
from pathlib import Path
import csv
from statistics import mean

ROOT = Path(__file__).resolve().parents[1]
TABLES = ROOT / "outputs" / "tables"


def main() -> None:
    with (TABLES / "ai_technology_systems_timeseries.csv").open(newline="", encoding="utf-8") as handle:
        rows = list(csv.DictReader(handle))
    out = []
    for scenario in sorted({r["scenario"] for r in rows}):
        subset = [r for r in rows if r["scenario"] == scenario]
        avg_gov = mean(float(r["governance_readiness"]) for r in subset)
        avg_contest = mean(float(r["contestability_index"]) for r in subset)
        min_trust = min(float(r["public_trust"]) for r in subset)
        out.append({
            "scenario": scenario,
            "average_governance_readiness": round(avg_gov, 3),
            "average_contestability_index": round(avg_contest, 3),
            "minimum_public_trust": round(min_trust, 3),
            "governance_diagnostic": "governance gap" if avg_gov < 45 or avg_contest < 35 else "comparatively accountable governance pathway",
        })
    path = TABLES / "governance_readiness_diagnostics.csv"
    with path.open("w", newline="", encoding="utf-8") as handle:
        writer = csv.DictWriter(handle, fieldnames=list(out[0].keys()))
        writer.writeheader(); writer.writerows(out)
    print(f"Wrote {path}")

if __name__ == "__main__":
    main()
