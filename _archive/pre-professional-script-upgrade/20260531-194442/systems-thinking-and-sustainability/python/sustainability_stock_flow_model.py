"""Python Workflow: Sustainability Feedback, Stock-Flow, and Scenario Modeling."""
from __future__ import annotations
from pathlib import Path
import csv
ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "data"
OUT = ROOT / "outputs" / "tables"
OUT.mkdir(parents=True, exist_ok=True)
YEARS = list(range(2026, 2041))

def load_scenarios() -> list[dict[str, str]]:
    with (DATA / "synthetic_policy_scenarios.csv").open(newline="", encoding="utf-8") as handle:
        return list(csv.DictReader(handle))

def simulate(row: dict[str, str]) -> list[dict[str, float | int | str]]:
    stock = 100.0
    results = []
    delay = int(float(row["policy_delay"]))
    regeneration_rate = float(row["regeneration_rate"])
    extraction_rate = float(row["extraction_rate"])
    rebound_strength = float(row["rebound_strength"])
    for i, year in enumerate(YEARS):
        delayed_policy_effect = max(0, i - delay) * 0.08
        regeneration = regeneration_rate + delayed_policy_effect
        extraction = extraction_rate * (1.0 + rebound_strength * max(0, 5 - i) / 20.0)
        degradation = 0.85 if stock < 80 else 0.35
        stock = max(0.0, stock + regeneration - extraction - degradation)
        results.append({"scenario": row["scenario"], "year": year, "stock": round(stock, 3), "regeneration": round(regeneration, 3), "extraction": round(extraction, 3), "degradation": round(degradation, 3)})
    return results

def main() -> None:
    rows = []
    for scenario in load_scenarios():
        rows.extend(simulate(scenario))
    path = OUT / "sustainability_stock_flow_results.csv"
    with path.open("w", newline="", encoding="utf-8") as handle:
        writer = csv.DictWriter(handle, fieldnames=["scenario", "year", "stock", "regeneration", "extraction", "degradation"])
        writer.writeheader(); writer.writerows(rows)
    print(f"Wrote {path}")
if __name__ == "__main__":
    main()
