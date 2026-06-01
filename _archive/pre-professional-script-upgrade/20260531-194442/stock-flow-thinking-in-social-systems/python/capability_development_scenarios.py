"""Capability development scenario comparison with synthetic values."""

from __future__ import annotations

from pathlib import Path
import csv

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / "outputs" / "tables"
OUT.mkdir(parents=True, exist_ok=True)

SCENARIOS = {
    "baseline": {"learning": 2.0, "health_support": 1.0, "stability": 0.8, "exclusion_stress": 2.6},
    "education_only": {"learning": 3.6, "health_support": 1.0, "stability": 0.8, "exclusion_stress": 2.6},
    "capability_ecosystem": {"learning": 3.2, "health_support": 2.4, "stability": 2.8, "exclusion_stress": 1.2},
}


def simulate(name: str, params: dict[str, float], months: int = 24) -> list[dict[str, float | str]]:
    capability = 45.0
    rows = []
    for month in range(months + 1):
        rows.append({"scenario": name, "month": month, "capability": round(capability, 2), **params})
        capability = min(100.0, max(0.0, capability + params["learning"] + params["health_support"] + params["stability"] - params["exclusion_stress"]))
    return rows


if __name__ == "__main__":
    rows = []
    for scenario, params in SCENARIOS.items():
        rows.extend(simulate(scenario, params))
    path = OUT / "capability_development_scenarios.csv"
    with path.open("w", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=rows[0].keys())
        writer.writeheader()
        writer.writerows(rows)
    print(f"Wrote {path}")
