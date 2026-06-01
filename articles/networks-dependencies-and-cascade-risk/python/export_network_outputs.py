"""Create a plain-text executive summary for network-risk outputs."""

from __future__ import annotations
import csv
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
TABLES = ROOT / "outputs" / "tables"


def load_rows(path: Path) -> list[dict[str, str]]:
    with path.open(newline="", encoding="utf-8") as handle:
        return list(csv.DictReader(handle))


def main() -> None:
    criticality_path = TABLES / "network_node_criticality_ranked.csv"
    cascade_path = TABLES / "network_cascade_summary.csv"
    if not criticality_path.exists():
        raise FileNotFoundError(f"Missing {criticality_path}. Run node_criticality_diagnostics.py first.")
    if not cascade_path.exists():
        raise FileNotFoundError(f"Missing {cascade_path}. Run network_dependency_cascade_model.py first.")

    critical = load_rows(criticality_path)[:5]
    cascades = load_rows(cascade_path)

    lines = [
        "Network dependency and cascade-risk executive summary",
        "=" * 58,
        "",
        "Top critical nodes:",
    ]
    for row in critical:
        lines.append(f"- #{row['rank']} {row['node_id']} ({row['category']}): criticality {row['criticality_index']}")

    lines.extend(["", "Cascade scenarios:"])
    for row in cascades:
        lines.append(f"- {row['scenario']}: failed nodes={row['final_failed_count']}, cascade depth={row['cascade_depth']}, diagnostic={row['diagnostic']}")

    path = TABLES / "network_risk_executive_summary.txt"
    path.write_text("\n".join(lines) + "\n", encoding="utf-8")
    print(f"Wrote {path}")


if __name__ == "__main__":
    main()
