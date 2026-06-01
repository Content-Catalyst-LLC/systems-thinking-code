"""Validation checks for AI technology systems outputs."""
from __future__ import annotations
from pathlib import Path
import csv

ROOT = Path(__file__).resolve().parents[1]
TABLES = ROOT / "outputs" / "tables"
REQUIRED = [
    "ai_technology_systems_timeseries.csv",
    "ai_technology_systems_summary.csv",
]
BOUNDED = [
    "drift_index", "feedback_bias_index", "group_a_error", "group_b_error",
    "false_positive_gap", "false_negative_gap", "automation_burden",
    "human_review_backlog", "contestability_index", "governance_readiness",
    "ai_system_risk", "public_trust",
]


def main() -> None:
    errors: list[str] = []
    for filename in REQUIRED:
        path = TABLES / filename
        if not path.exists():
            errors.append(f"Missing required output: {path}")

    ts = TABLES / "ai_technology_systems_timeseries.csv"
    if ts.exists():
        with ts.open(newline="", encoding="utf-8") as handle:
            reader = csv.DictReader(handle)
            for line_no, row in enumerate(reader, start=2):
                for field in BOUNDED:
                    value = float(row[field])
                    if value < -0.001 or value > 100.001:
                        errors.append(f"{field} outside 0-100 on line {line_no}: {value}")

    report = TABLES / "validation_report.txt"
    report.parent.mkdir(parents=True, exist_ok=True)
    if errors:
        report.write_text("Validation failed.\n" + "\n".join(errors) + "\n", encoding="utf-8")
        raise SystemExit("\n".join(errors))
    report.write_text("Validation passed.\nAll AI system indicators are bounded and required outputs exist.\n", encoding="utf-8")
    print("Validation passed.")


if __name__ == "__main__":
    main()
