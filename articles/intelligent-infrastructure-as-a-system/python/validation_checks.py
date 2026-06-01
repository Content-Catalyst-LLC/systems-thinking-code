#!/usr/bin/env python3
"""
Validation checks for intelligent infrastructure workflow outputs.
Uses only Python standard library and article-root paths.
"""

from __future__ import annotations

from pathlib import Path
import csv

ARTICLE_ROOT = Path(__file__).resolve().parents[1]
TABLES_DIR = ARTICLE_ROOT / "outputs" / "tables"

REQUIRED = [
    "intelligent_infrastructure_timeseries.csv",
    "intelligent_infrastructure_summary.csv",
]

BOUNDED_FIELDS = [
    "condition",
    "failure_probability",
    "failure_consequence",
    "cyber_physical_dependency",
    "risk_score",
    "maintenance_action_score",
    "resilience_score",
    "equity_priority",
    "redundancy",
]


def read_rows(path: Path) -> list[dict[str, str]]:
    with path.open("r", encoding="utf-8", newline="") as handle:
        return list(csv.DictReader(handle))


def main() -> None:
    missing = [name for name in REQUIRED if not (TABLES_DIR / name).exists()]
    if missing:
        raise FileNotFoundError("Missing required output files: " + ", ".join(missing))

    rows = read_rows(TABLES_DIR / "intelligent_infrastructure_timeseries.csv")
    if not rows:
        raise ValueError("intelligent_infrastructure_timeseries.csv has no data rows.")

    errors: list[str] = []
    for row in rows:
        for field in BOUNDED_FIELDS:
            value = float(row[field])
            if value < -0.001 or value > 100.001:
                errors.append(
                    f"{field} outside 0-100 range in {row.get('scenario')} "
                    f"{row.get('asset_id')} year {row.get('year')}: {value}"
                )

    if errors:
        raise ValueError("Validation failed:\n" + "\n".join(errors[:25]))

    print("Validation passed.")


if __name__ == "__main__":
    main()
