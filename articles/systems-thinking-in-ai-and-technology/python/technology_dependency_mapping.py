"""Synthetic dependency map for AI and technology systems."""
from pathlib import Path
import csv

ROOT = Path(__file__).resolve().parents[1]
TABLES = ROOT / "outputs" / "tables"
DATA = ROOT / "data" / "processed"

DEPENDENCIES = [
    ("model_service", "cloud_provider", 0.72, "digital infrastructure"),
    ("model_service", "training_data_pipeline", 0.81, "data pipeline"),
    ("model_service", "human_review_team", 0.46, "labor and governance"),
    ("public_benefits_workflow", "model_service", 0.64, "decision support"),
    ("public_benefits_workflow", "appeals_process", 0.56, "contestability"),
    ("content_platform", "recommendation_engine", 0.83, "attention system"),
    ("recommendation_engine", "user_behavior_data", 0.78, "feedback loop"),
    ("smart_infrastructure", "sensor_network", 0.68, "field data"),
    ("smart_infrastructure", "cybersecurity_team", 0.58, "security"),
    ("governance_board", "incident_reports", 0.61, "accountability"),
]


def main() -> None:
    TABLES.mkdir(parents=True, exist_ok=True)
    DATA.mkdir(parents=True, exist_ok=True)
    rows = []
    for dependent, provider, weight, category in DEPENDENCIES:
        rows.append({
            "dependent_system": dependent,
            "provider_system": provider,
            "dependency_weight": weight,
            "dependency_category": category,
            "critical_dependency": "yes" if weight >= 0.70 else "no",
        })
    for folder in (TABLES, DATA):
        path = folder / "technology_dependency_map.csv"
        with path.open("w", newline="", encoding="utf-8") as handle:
            writer = csv.DictWriter(handle, fieldnames=list(rows[0].keys()))
            writer.writeheader(); writer.writerows(rows)
    print(f"Wrote {TABLES / 'technology_dependency_map.csv'}")

if __name__ == "__main__":
    main()
