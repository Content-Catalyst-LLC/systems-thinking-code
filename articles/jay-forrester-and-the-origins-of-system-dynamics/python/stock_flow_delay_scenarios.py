#!/usr/bin/env python3
from __future__ import annotations

from pathlib import Path
import csv
from statistics import mean

ARTICLE_ROOT = Path(__file__).resolve().parents[1]
TABLES = ARTICLE_ROOT / "outputs" / "tables"
CORE = TABLES / "forrester_system_dynamics_timeseries.csv"
OUT = TABLES / "stock_flow_delay_scenarios.csv"


def main() -> None:
    if not CORE.exists():
        print(f"Skipping stock-flow delay diagnostics; missing {CORE}")
        return

    rows = list(csv.DictReader(CORE.open("r", encoding="utf-8")))
    output = []

    for scenario in sorted({r["scenario"] for r in rows}):
        subset = [r for r in rows if r["scenario"] == scenario]
        avg_gap = mean(abs(float(r["backlog_stock"]) - float(r["perceived_backlog"])) for r in subset)
        max_gap = max(abs(float(r["backlog_stock"]) - float(r["perceived_backlog"])) for r in subset)
        output.append({
            "scenario": scenario,
            "average_perception_gap": round(avg_gap, 3),
            "maximum_perception_gap": round(max_gap, 3),
            "diagnostic": "high delay distortion" if max_gap >= 25 else "delay distortion comparatively contained",
        })

    with OUT.open("w", newline="", encoding="utf-8") as handle:
        writer = csv.DictWriter(handle, fieldnames=list(output[0].keys()))
        writer.writeheader()
        writer.writerows(output)

    print(f"Wrote {OUT}")


if __name__ == "__main__":
    main()
