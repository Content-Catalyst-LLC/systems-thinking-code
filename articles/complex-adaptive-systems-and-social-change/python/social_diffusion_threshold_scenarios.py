#!/usr/bin/env python3
from __future__ import annotations

from pathlib import Path
import csv

ARTICLE_ROOT = Path(__file__).resolve().parents[1]
RAW = ARTICLE_ROOT / "data" / "raw"
TABLES = ARTICLE_ROOT / "outputs" / "tables"
OUT = TABLES / "social_diffusion_threshold_diagnostics.csv"


def clamp(value: float) -> float:
    return max(0.0, min(1.0, value))


def main() -> None:
    agents_path = RAW / "synthetic_agents.csv"
    edges_path = RAW / "synthetic_network_edges.csv"
    if not agents_path.exists() or not edges_path.exists():
        print("Skipping threshold diagnostics; missing synthetic agent or edge data.")
        return

    agents = {row["agent_id"]: row for row in csv.DictReader(agents_path.open("r", encoding="utf-8"))}
    edges = list(csv.DictReader(edges_path.open("r", encoding="utf-8")))

    adopted = {agent_id for agent_id, row in agents.items() if int(row["initial_adoption"]) == 1}
    rows = []

    for period in range(1, 13):
        next_adopted = set(adopted)
        for agent_id, row in agents.items():
            if agent_id in adopted:
                continue
            incoming = [edge for edge in edges if edge["target"] == agent_id or edge["source"] == agent_id]
            if not incoming:
                continue
            exposure = 0.0
            total_weight = 0.0
            for edge in incoming:
                neighbor = edge["source"] if edge["target"] == agent_id else edge["target"]
                weight = float(edge["tie_strength"])
                total_weight += weight
                if neighbor in adopted:
                    exposure += weight
            adoption_signal = exposure / total_weight if total_weight else 0.0
            threshold = float(row["threshold"])
            if adoption_signal >= threshold:
                next_adopted.add(agent_id)
        adopted = next_adopted
        rows.append({
            "period": period,
            "adopted_count": len(adopted),
            "adoption_share": round(len(adopted) / len(agents), 3),
            "adopted_agents": ";".join(sorted(adopted)),
        })

    TABLES.mkdir(parents=True, exist_ok=True)
    with OUT.open("w", newline="", encoding="utf-8") as handle:
        writer = csv.DictWriter(handle, fieldnames=list(rows[0].keys()))
        writer.writeheader()
        writer.writerows(rows)

    print(f"Wrote {OUT}")


if __name__ == "__main__":
    main()
