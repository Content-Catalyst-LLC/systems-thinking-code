#!/usr/bin/env python3
from __future__ import annotations

from pathlib import Path
import csv

ARTICLE_ROOT = Path(__file__).resolve().parents[1]
RAW = ARTICLE_ROOT / "data" / "raw"
TABLES = ARTICLE_ROOT / "outputs" / "tables"
OUT = TABLES / "feedback_loop_leverage_diagnostics.csv"


def main() -> None:
    path = RAW / "synthetic_feedback_loops.csv"
    if not path.exists():
        print("Skipping feedback loop leverage model; missing synthetic_feedback_loops.csv")
        return

    loops = list(csv.DictReader(path.open("r", encoding="utf-8")))
    output = []

    for loop in loops:
        if loop["loop_type"].lower() == "reinforcing":
            leverage = "change growth driver or constraint"
        else:
            leverage = "change target, information quality, delay, or response strength"
        output.append({
            "loop_id": loop["loop_id"],
            "loop_name": loop["loop_name"],
            "loop_type": loop["loop_type"],
            "policy_risk": loop["policy_risk"],
            "recommended_leverage_focus": leverage,
        })

    TABLES.mkdir(parents=True, exist_ok=True)
    with OUT.open("w", newline="", encoding="utf-8") as handle:
        writer = csv.DictWriter(handle, fieldnames=list(output[0].keys()))
        writer.writeheader()
        writer.writerows(output)

    print(f"Wrote {OUT}")


if __name__ == "__main__":
    main()
