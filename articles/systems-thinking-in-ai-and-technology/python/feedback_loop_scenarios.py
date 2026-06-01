"""Feedback-loop diagnostics for AI systems."""
from pathlib import Path
import csv
from statistics import mean

ROOT = Path(__file__).resolve().parents[1]
TABLES = ROOT / "outputs" / "tables"


def read_rows(filename: str) -> list[dict[str, str]]:
    with (TABLES / filename).open(newline="", encoding="utf-8") as handle:
        return list(csv.DictReader(handle))


def write_rows(filename: str, rows: list[dict[str, object]]) -> None:
    path = TABLES / filename
    with path.open("w", newline="", encoding="utf-8") as handle:
        writer = csv.DictWriter(handle, fieldnames=list(rows[0].keys()))
        writer.writeheader(); writer.writerows(rows)


def main() -> None:
    rows = read_rows("ai_technology_systems_timeseries.csv")
    out = []
    for scenario in sorted({r["scenario"] for r in rows}):
        subset = [r for r in rows if r["scenario"] == scenario]
        start_bias = float(subset[0]["feedback_bias_index"])
        end_bias = float(subset[-1]["feedback_bias_index"])
        avg_risk = mean(float(r["ai_system_risk"]) for r in subset)
        out.append({
            "scenario": scenario,
            "initial_feedback_bias_index": round(start_bias, 3),
            "final_feedback_bias_index": round(end_bias, 3),
            "feedback_bias_change": round(end_bias - start_bias, 3),
            "average_ai_system_risk": round(avg_risk, 3),
            "loop_diagnostic": "self-reinforcing harm" if end_bias - start_bias > 8 else "contained or corrected feedback",
        })
    write_rows("feedback_loop_diagnostics.csv", out)
    print(f"Wrote {TABLES / 'feedback_loop_diagnostics.csv'}")

if __name__ == "__main__":
    main()
