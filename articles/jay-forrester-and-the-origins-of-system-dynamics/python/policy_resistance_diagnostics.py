#!/usr/bin/env python3
from __future__ import annotations

from pathlib import Path
import csv
from statistics import mean

ARTICLE_ROOT = Path(__file__).resolve().parents[1]
TABLES = ARTICLE_ROOT / "outputs" / "tables"
CORE = TABLES / "forrester_system_dynamics_timeseries.csv"
OUT = TABLES / "policy_resistance_diagnostics.csv"


def main() -> None:
    if not CORE.exists():
        print(f"Skipping policy resistance diagnostics; missing {CORE}")
        return

    rows = list(csv.DictReader(CORE.open("r", encoding="utf-8")))
    output = []

    for scenario in sorted({r["scenario"] for r in rows}):
        subset = [r for r in rows if r["scenario"] == scenario]
        avg_resistance = mean(float(r["resistance_index"]) for r in subset)
        peak_resistance = max(float(r["resistance_index"]) for r in subset)
        avg_correction = mean(float(r["corrective_action"]) for r in subset)
        output.append({
            "scenario": scenario,
            "average_resistance_index": round(avg_resistance, 3),
            "peak_resistance_index": round(peak_resistance, 3),
            "average_corrective_action": round(avg_correction, 3),
            "resistance_to_correction_ratio": round(avg_resistance / max(avg_correction, 0.001), 3),
            "diagnostic": "compensating feedback likely undermines direct intervention" if avg_resistance / max(avg_correction, 0.001) >= 0.35 else "resistance comparatively manageable",
        })

    with OUT.open("w", newline="", encoding="utf-8") as handle:
        writer = csv.DictWriter(handle, fieldnames=list(output[0].keys()))
        writer.writeheader()
        writer.writerows(output)

    print(f"Wrote {OUT}")


if __name__ == "__main__":
    main()
