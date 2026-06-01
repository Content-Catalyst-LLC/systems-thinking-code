"""Group-level fairness and drift diagnostics."""
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
        avg_group_a_error = mean(float(r["group_a_error"]) for r in subset)
        avg_group_b_error = mean(float(r["group_b_error"]) for r in subset)
        avg_drift = mean(float(r["drift_index"]) for r in subset)
        out.append({
            "scenario": scenario,
            "average_group_a_error": round(avg_group_a_error, 3),
            "average_group_b_error": round(avg_group_b_error, 3),
            "average_error_gap": round(avg_group_b_error - avg_group_a_error, 3),
            "average_drift_index": round(avg_drift, 3),
            "fairness_drift_diagnostic": "requires immediate review" if avg_group_b_error - avg_group_a_error > 18 or avg_drift > 35 else "monitor with periodic audit",
        })
    path = TABLES / "fairness_drift_diagnostics.csv"
    with path.open("w", newline="", encoding="utf-8") as handle:
        writer = csv.DictWriter(handle, fieldnames=list(out[0].keys()))
        writer.writeheader(); writer.writerows(out)
    print(f"Wrote {path}")

if __name__ == "__main__":
    main()
