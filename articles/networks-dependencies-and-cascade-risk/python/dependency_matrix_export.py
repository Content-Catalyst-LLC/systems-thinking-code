"""Export a dependency matrix from edge-list outputs."""

from __future__ import annotations
import csv
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
TABLES = ROOT / "outputs" / "tables"


def main() -> None:
    source = TABLES / "network_dependencies.csv"
    if not source.exists():
        raise FileNotFoundError(f"Missing {source}. Run network_dependency_cascade_model.py first.")

    with source.open(newline="", encoding="utf-8") as handle:
        deps = list(csv.DictReader(handle))

    nodes = sorted(set([row["dependent"] for row in deps] + [row["provider"] for row in deps]))
    weights = {(row["dependent"], row["provider"]): float(row["dependency_weight"]) for row in deps}

    path = TABLES / "network_dependency_matrix.csv"
    with path.open("w", newline="", encoding="utf-8") as handle:
        writer = csv.writer(handle)
        writer.writerow(["dependent_provider"] + nodes)
        for dependent in nodes:
            writer.writerow([dependent] + [weights.get((dependent, provider), 0.0) for provider in nodes])
    print(f"Wrote {path}")


if __name__ == "__main__":
    main()
