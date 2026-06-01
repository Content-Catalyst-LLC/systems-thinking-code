"""Automation burden and human review capacity diagnostics."""
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
        avg_burden = mean(float(r["automation_burden"]) for r in subset)
        max_backlog = max(float(r["human_review_backlog"]) for r in subset)
        min_contest = min(float(r["contestability_index"]) for r in subset)
        out.append({
            "scenario": scenario,
            "average_automation_burden": round(avg_burden, 3),
            "maximum_human_review_backlog": round(max_backlog, 3),
            "minimum_contestability_index": round(min_contest, 3),
            "workflow_diagnostic": "symbolic oversight risk" if avg_burden > 35 and min_contest < 35 else "oversight capacity comparatively stronger",
        })
    path = TABLES / "automation_burden_diagnostics.csv"
    with path.open("w", newline="", encoding="utf-8") as handle:
        writer = csv.DictWriter(handle, fieldnames=list(out[0].keys()))
        writer.writeheader(); writer.writerows(out)
    print(f"Wrote {path}")

if __name__ == "__main__":
    main()
