"""Trust and legitimacy repair model with synthetic assumptions."""

from __future__ import annotations

from pathlib import Path
import csv

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / "outputs" / "tables"
OUT.mkdir(parents=True, exist_ok=True)


def simulate_trust(months: int, initial: float, reliability: float, harm: float, repair: float) -> list[dict[str, float]]:
    trust = initial
    rows = []
    for month in range(months + 1):
        rows.append({"month": month, "public_trust": round(trust, 2), "reliability": reliability, "harm": harm, "repair": repair})
        trust = min(100.0, max(0.0, trust + reliability + repair - harm))
    return rows


if __name__ == "__main__":
    scenarios = {
        "communication_only": simulate_trust(24, 42, reliability=2.0, harm=2.8, repair=0.6),
        "structural_repair": simulate_trust(24, 42, reliability=3.8, harm=1.4, repair=2.2),
    }
    for name, rows in scenarios.items():
        path = OUT / f"trust_{name}.csv"
        with path.open("w", newline="") as f:
            writer = csv.DictWriter(f, fieldnames=rows[0].keys())
            writer.writeheader()
            writer.writerows(rows)
        print(f"Wrote {path}")
