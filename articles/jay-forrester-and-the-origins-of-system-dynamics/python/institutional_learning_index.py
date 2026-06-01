#!/usr/bin/env python3
from __future__ import annotations

from pathlib import Path
import csv
from statistics import mean

ARTICLE_ROOT = Path(__file__).resolve().parents[1]
TABLES = ARTICLE_ROOT / "outputs" / "tables"
CORE = TABLES / "forrester_system_dynamics_timeseries.csv"
OUT = TABLES / "institutional_learning_index.csv"


def main() -> None:
    if not CORE.exists():
        print(f"Skipping institutional learning index; missing {CORE}")
        return

    rows = list(csv.DictReader(CORE.open("r", encoding="utf-8")))
    output = []

    for scenario in sorted({r["scenario"] for r in rows}):
        subset = [r for r in rows if r["scenario"] == scenario]
        final = subset[-1]
        avg_learning = mean(float(r["institutional_learning_stock"]) for r in subset)
        avg_trust = mean(float(r["trust_stock"]) for r in subset)
        score = avg_learning * 0.45 + avg_trust * 0.30 + float(final["system_performance"]) * 0.25
        output.append({
            "scenario": scenario,
            "institutional_learning_index": round(score, 3),
            "average_learning_stock": round(avg_learning, 3),
            "average_trust_stock": round(avg_trust, 3),
            "final_system_performance": final["system_performance"],
            "diagnostic": "learning loop supports structural improvement" if score >= 60 else "learning loop requires reinforcement",
        })

    with OUT.open("w", newline="", encoding="utf-8") as handle:
        writer = csv.DictWriter(handle, fieldnames=list(output[0].keys()))
        writer.writeheader()
        writer.writerows(output)

    print(f"Wrote {OUT}")


if __name__ == "__main__":
    main()
