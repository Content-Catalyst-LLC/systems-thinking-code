#!/usr/bin/env python3
"""Baseline shifting-the-burden simulation using synthetic article data."""

from __future__ import annotations

from pathlib import Path
import csv

ARTICLE_DIR = Path(__file__).resolve().parents[1]
DATA_PATH = ARTICLE_DIR / "data" / "synthetic_problem_symptoms.csv"
OUTPUT_PATH = ARTICLE_DIR / "outputs" / "tables" / "baseline_problem_pressure_summary.csv"


def read_rows(path: Path) -> list[dict[str, str]]:
    with path.open(newline="", encoding="utf-8") as handle:
        return list(csv.DictReader(handle))


def main() -> None:
    rows = read_rows(DATA_PATH)
    pressures = [float(row["problem_pressure"]) for row in rows]
    summary = {
        "periods": len(pressures),
        "initial_pressure": pressures[0],
        "final_pressure": pressures[-1],
        "change": pressures[-1] - pressures[0],
        "average_pressure": sum(pressures) / len(pressures),
    }

    OUTPUT_PATH.parent.mkdir(parents=True, exist_ok=True)
    with OUTPUT_PATH.open("w", newline="", encoding="utf-8") as handle:
        writer = csv.DictWriter(handle, fieldnames=list(summary.keys()))
        writer.writeheader()
        writer.writerow(summary)

    print("Baseline problem-pressure summary")
    for key, value in summary.items():
        print(f"{key}: {value}")


if __name__ == "__main__":
    main()
