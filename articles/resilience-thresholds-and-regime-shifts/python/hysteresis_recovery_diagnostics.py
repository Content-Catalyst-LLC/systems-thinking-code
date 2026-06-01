#!/usr/bin/env python3
"""Synthetic hysteresis and recovery difficulty diagnostics."""

from __future__ import annotations

from pathlib import Path
import pandas as pd

ROOT = Path(__file__).resolve().parents[1]
TABLE_DIR = ROOT / "outputs" / "tables"
TABLE_DIR.mkdir(parents=True, exist_ok=True)


def main() -> None:
    scenarios = [
        {"system": "lake", "collapse_threshold": 70, "recovery_threshold": 42, "current_pressure": 76},
        {"system": "public_institution", "collapse_threshold": 64, "recovery_threshold": 36, "current_pressure": 61},
        {"system": "organization", "collapse_threshold": 68, "recovery_threshold": 44, "current_pressure": 72},
        {"system": "infrastructure", "collapse_threshold": 74, "recovery_threshold": 51, "current_pressure": 69},
        {"system": "community", "collapse_threshold": 66, "recovery_threshold": 45, "current_pressure": 58},
    ]
    df = pd.DataFrame(scenarios)
    df["hysteresis_gap"] = df["collapse_threshold"] - df["recovery_threshold"]
    df["collapse_margin"] = df["collapse_threshold"] - df["current_pressure"]
    df["status"] = df["collapse_margin"].apply(
        lambda x: "shift likely or underway" if x <= 0 else "near threshold" if x <= 8 else "monitor"
    )
    df["recovery_implication"] = df["hysteresis_gap"].apply(
        lambda x: "large restoration burden" if x >= 25 else "moderate restoration burden"
    )
    df.to_csv(TABLE_DIR / "hysteresis_recovery_diagnostics.csv", index=False)
    print("Hysteresis recovery diagnostics")
    print(df.to_string(index=False))


if __name__ == "__main__":
    main()
