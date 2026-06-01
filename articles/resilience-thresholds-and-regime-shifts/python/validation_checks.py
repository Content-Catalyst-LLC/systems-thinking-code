#!/usr/bin/env python3
"""Validation checks for generated resilience outputs."""

from __future__ import annotations

from pathlib import Path
import pandas as pd

ROOT = Path(__file__).resolve().parents[1]
TABLE_DIR = ROOT / "outputs" / "tables"


def check_file(path: Path) -> dict[str, object]:
    if not path.exists():
        return {"file": path.name, "status": "missing", "rows": 0}
    df = pd.read_csv(path)
    return {"file": path.name, "status": "ok" if len(df) > 0 else "empty", "rows": len(df)}


def main() -> None:
    expected = [
        "resilience_threshold_regime_results.csv",
        "resilience_threshold_regime_summary.csv",
        "early_warning_indicator_summary.csv",
        "hysteresis_recovery_diagnostics.csv",
        "adaptive_capacity_scorecard.csv",
        "resilience_sensitivity_ranking.csv",
        "distributional_vulnerability_index.csv",
    ]
    report = pd.DataFrame([check_file(TABLE_DIR / name) for name in expected])
    report.to_csv(TABLE_DIR / "validation_report.csv", index=False)
    print("Validation report")
    print(report.to_string(index=False))
    if (report["status"] != "ok").any():
        raise SystemExit("Validation failed: one or more expected outputs missing or empty")


if __name__ == "__main__":
    main()
