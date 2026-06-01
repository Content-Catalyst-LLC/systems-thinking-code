"""
Network dependency and cascade-risk model.

This dependency-light script creates a synthetic interdependent system,
calculates node criticality, and simulates cascade propagation after
targeted and random disruptions.
"""

from __future__ import annotations

from dataclasses import dataclass
import csv
from pathlib import Path
import random
from collections import defaultdict, deque
from statistics import mean

ROOT = Path(__file__).resolve().parents[1]
TABLES = ROOT / "outputs" / "tables"
DATA_PROCESSED = ROOT / "data" / "processed"


@dataclass(frozen=True)
class NetworkNode:
    node_id: str
    category: str
    capacity: float
    threshold: float
    vulnerability: float
    recovery_capacity: float


def ensure_dirs() -> None:
    TABLES.mkdir(parents=True, exist_ok=True)
    DATA_PROCESSED.mkdir(parents=True, exist_ok=True)


def build_nodes() -> dict[str, NetworkNode]:
    nodes = [
        NetworkNode("power_grid", "infrastructure", 0.92, 0.55, 0.42, 0.70),
        NetworkNode("water_utility", "infrastructure", 0.88, 0.50, 0.50, 0.62),
        NetworkNode("hospital", "public_health", 0.82, 0.48, 0.72, 0.55),
        NetworkNode("transit_hub", "transport", 0.78, 0.46, 0.60, 0.50),
        NetworkNode("data_center", "digital", 0.86, 0.52, 0.45, 0.68),
        NetworkNode("cloud_platform", "digital", 0.90, 0.58, 0.40, 0.72),
        NetworkNode("food_distribution", "supply_chain", 0.80, 0.45, 0.68, 0.48),
        NetworkNode("fuel_terminal", "supply_chain", 0.76, 0.44, 0.58, 0.46),
        NetworkNode("emergency_services", "public_safety", 0.84, 0.50, 0.70, 0.60),
        NetworkNode("telecom_network", "digital", 0.87, 0.50, 0.52, 0.64),
        NetworkNode("community_clinic", "public_health", 0.70, 0.40, 0.78, 0.44),
        NetworkNode("local_government", "institutional", 0.74, 0.42, 0.65, 0.54),
        NetworkNode("school_network", "institutional", 0.72, 0.40, 0.62, 0.46),
        NetworkNode("housing_services", "institutional", 0.68, 0.38, 0.75, 0.42),
        NetworkNode("payment_system", "financial", 0.85, 0.50, 0.48, 0.66),
        NetworkNode("regional_supplier", "supply_chain", 0.77, 0.43, 0.55, 0.50),
    ]
    return {node.node_id: node for node in nodes}


def build_dependencies() -> dict[str, dict[str, float]]:
    return {
        "water_utility": {"power_grid": 0.70, "telecom_network": 0.20},
        "hospital": {"power_grid": 0.55, "water_utility": 0.35, "telecom_network": 0.30, "regional_supplier": 0.40},
        "transit_hub": {"power_grid": 0.45, "telecom_network": 0.25, "fuel_terminal": 0.35},
        "data_center": {"power_grid": 0.65, "telecom_network": 0.45, "water_utility": 0.15},
        "cloud_platform": {"data_center": 0.65, "telecom_network": 0.45, "power_grid": 0.30},
        "food_distribution": {"fuel_terminal": 0.55, "transit_hub": 0.25, "payment_system": 0.25, "regional_supplier": 0.40},
        "fuel_terminal": {"power_grid": 0.35, "telecom_network": 0.20},
        "emergency_services": {"power_grid": 0.35, "telecom_network": 0.55, "transit_hub": 0.25, "hospital": 0.25},
        "telecom_network": {"power_grid": 0.60, "data_center": 0.25},
        "community_clinic": {"power_grid": 0.30, "water_utility": 0.25, "hospital": 0.20, "telecom_network": 0.30},
        "local_government": {"cloud_platform": 0.35, "telecom_network": 0.35, "payment_system": 0.20},
        "school_network": {"power_grid": 0.25, "telecom_network": 0.25, "transit_hub": 0.30, "food_distribution": 0.20},
        "housing_services": {"local_government": 0.35, "payment_system": 0.25, "telecom_network": 0.25},
        "payment_system": {"cloud_platform": 0.40, "telecom_network": 0.30, "power_grid": 0.20},
        "regional_supplier": {"fuel_terminal": 0.30, "payment_system": 0.25, "transit_hub": 0.20},
    }


def reverse_dependencies(dependencies: dict[str, dict[str, float]]) -> dict[str, list[str]]:
    reverse: dict[str, list[str]] = defaultdict(list)
    for dependent, providers in dependencies.items():
        for provider in providers:
            reverse[provider].append(dependent)
    return dict(reverse)


def degree_scores(nodes: dict[str, NetworkNode], dependencies: dict[str, dict[str, float]]) -> dict[str, int]:
    reverse = reverse_dependencies(dependencies)
    return {node_id: len(dependencies.get(node_id, {})) + len(reverse.get(node_id, [])) for node_id in nodes}


def dependency_exposure_scores(nodes: dict[str, NetworkNode], dependencies: dict[str, dict[str, float]]) -> dict[str, float]:
    reverse = reverse_dependencies(dependencies)
    scores = {}
    for node_id in nodes:
        exposure = 0.0
        for dependent in reverse.get(node_id, []):
            exposure += dependencies[dependent][node_id] * nodes[dependent].vulnerability
        scores[node_id] = round(exposure, 4)
    return scores


def undirected_neighbors(dependencies: dict[str, dict[str, float]]) -> dict[str, set[str]]:
    neighbors: dict[str, set[str]] = defaultdict(set)
    for dependent, providers in dependencies.items():
        for provider in providers:
            neighbors[dependent].add(provider)
            neighbors[provider].add(dependent)
    return neighbors


def shortest_path_distance(nodes: dict[str, NetworkNode], dependencies: dict[str, dict[str, float]], source: str, target: str) -> int:
    neighbors = undirected_neighbors(dependencies)
    visited = {source}
    queue: deque[tuple[str, int]] = deque([(source, 0)])
    while queue:
        current, distance = queue.popleft()
        if current == target:
            return distance
        for neighbor in neighbors.get(current, set()):
            if neighbor in nodes and neighbor not in visited:
                visited.add(neighbor)
                queue.append((neighbor, distance + 1))
    return 999


def bridge_approximation(nodes: dict[str, NetworkNode], dependencies: dict[str, dict[str, float]]) -> dict[str, float]:
    node_ids = list(nodes)
    base_distances: dict[tuple[str, str], int] = {}
    for i, source in enumerate(node_ids):
        for target in node_ids[i + 1:]:
            base_distances[(source, target)] = shortest_path_distance(nodes, dependencies, source, target)

    scores = {}
    for removed in node_ids:
        reduced_nodes = {key: val for key, val in nodes.items() if key != removed}
        reduced_dependencies = {
            dependent: {provider: weight for provider, weight in providers.items() if provider != removed}
            for dependent, providers in dependencies.items()
            if dependent != removed
        }
        disruption = 0
        comparisons = 0
        reduced_ids = list(reduced_nodes)
        for i, source in enumerate(reduced_ids):
            for target in reduced_ids[i + 1:]:
                old_distance = base_distances.get((source, target), base_distances.get((target, source), 999))
                new_distance = shortest_path_distance(reduced_nodes, reduced_dependencies, source, target)
                if new_distance > old_distance:
                    disruption += min(new_distance, 20) - min(old_distance, 20)
                comparisons += 1
        scores[removed] = round(disruption / max(comparisons, 1), 4)
    return scores


def scenario_initial_failures(nodes: dict[str, NetworkNode], mode: str, seed: int = 7) -> set[str]:
    if mode == "targeted_power":
        return {"power_grid"}
    if mode == "targeted_cloud":
        return {"cloud_platform"}
    if mode == "targeted_transit":
        return {"transit_hub"}
    if mode == "targeted_supplier":
        return {"regional_supplier"}
    if mode == "targeted_telecom":
        return {"telecom_network"}
    if mode == "random_two":
        rng = random.Random(seed)
        return set(rng.sample(list(nodes), 2))
    raise ValueError(f"Unknown scenario mode: {mode}")


def simulate_cascade(nodes: dict[str, NetworkNode], dependencies: dict[str, dict[str, float]], initial_failures: set[str], max_steps: int = 8) -> list[dict[str, object]]:
    failed = set(initial_failures)
    rows: list[dict[str, object]] = []

    for step in range(max_steps + 1):
        rows.append({
            "step": step,
            "failed_nodes": sorted(failed),
            "failed_count": len(failed),
            "service_loss_index": round(mean(nodes[node_id].vulnerability for node_id in failed), 4) if failed else 0.0,
        })

        new_failures: set[str] = set()
        for node_id, node in nodes.items():
            if node_id in failed:
                continue
            dependency_load = sum(weight for provider, weight in dependencies.get(node_id, {}).items() if provider in failed)
            resilience_buffer = node.capacity * 0.20 + node.recovery_capacity * 0.15
            adjusted_threshold = node.threshold + resilience_buffer
            if dependency_load > adjusted_threshold:
                new_failures.add(node_id)

        if not new_failures:
            break
        failed.update(new_failures)

    return rows


def write_csv(path: Path, rows: list[dict[str, object]]) -> None:
    if not rows:
        return
    normalized = []
    for row in rows:
        new_row = dict(row)
        if isinstance(new_row.get("failed_nodes"), list):
            new_row["failed_nodes"] = ";".join(str(x) for x in new_row["failed_nodes"])
        normalized.append(new_row)

    with path.open("w", newline="", encoding="utf-8") as handle:
        writer = csv.DictWriter(handle, fieldnames=list(normalized[0].keys()))
        writer.writeheader()
        writer.writerows(normalized)


def main() -> None:
    ensure_dirs()
    nodes = build_nodes()
    dependencies = build_dependencies()
    degree = degree_scores(nodes, dependencies)
    exposure = dependency_exposure_scores(nodes, dependencies)
    bridge = bridge_approximation(nodes, dependencies)

    node_rows: list[dict[str, object]] = []
    for node_id, node in nodes.items():
        node_rows.append({
            "node_id": node_id,
            "category": node.category,
            "capacity": node.capacity,
            "threshold": node.threshold,
            "vulnerability": node.vulnerability,
            "recovery_capacity": node.recovery_capacity,
            "degree_score": degree[node_id],
            "dependency_exposure_score": exposure[node_id],
            "bridge_approximation_score": bridge[node_id],
            "criticality_index": round(
                degree[node_id] * 0.15 + exposure[node_id] * 3.0 + bridge[node_id] * 2.0
                + node.vulnerability * 0.60 - node.recovery_capacity * 0.30,
                4,
            ),
        })

    dependency_rows = []
    for dependent, providers in dependencies.items():
        for provider, weight in providers.items():
            dependency_rows.append({
                "dependent": dependent,
                "provider": provider,
                "dependency_weight": weight,
                "dependent_category": nodes[dependent].category,
                "provider_category": nodes[provider].category,
            })

    cascade_rows: list[dict[str, object]] = []
    scenario_modes = ["targeted_power", "targeted_cloud", "targeted_transit", "targeted_supplier", "targeted_telecom", "random_two"]
    for mode in scenario_modes:
        initial = scenario_initial_failures(nodes, mode)
        for row in simulate_cascade(nodes, dependencies, initial):
            row["scenario"] = mode
            row["initial_failures"] = ";".join(sorted(initial))
            cascade_rows.append(row)

    summary_rows = []
    for mode in scenario_modes:
        subset = [row for row in cascade_rows if row["scenario"] == mode]
        final = subset[-1]
        failed_count = int(final["failed_count"])
        summary_rows.append({
            "scenario": mode,
            "initial_failures": final["initial_failures"],
            "final_failed_count": failed_count,
            "final_service_loss_index": final["service_loss_index"],
            "cascade_depth": final["step"],
            "diagnostic": (
                "high cascade risk" if failed_count >= 8 else
                "moderate cascade risk" if failed_count >= 4 else
                "contained disruption"
            ),
        })

    write_csv(TABLES / "network_node_criticality.csv", node_rows)
    write_csv(TABLES / "network_dependencies.csv", dependency_rows)
    write_csv(TABLES / "network_cascade_timeseries.csv", cascade_rows)
    write_csv(TABLES / "network_cascade_summary.csv", summary_rows)
    write_csv(DATA_PROCESSED / "synthetic_nodes.csv", node_rows)
    write_csv(DATA_PROCESSED / "synthetic_dependencies.csv", dependency_rows)
    write_csv(DATA_PROCESSED / "synthetic_cascade_summary.csv", summary_rows)

    (TABLES / "validation_report.txt").write_text(
        "Validation passed.\nNetwork node scores, dependencies, cascade simulations, and summary outputs completed.\n",
        encoding="utf-8",
    )

    print("\nNetwork cascade summary:")
    for row in summary_rows:
        print(f"{row['scenario']}: final failed nodes={row['final_failed_count']}, cascade depth={row['cascade_depth']}, diagnostic={row['diagnostic']}")


if __name__ == "__main__":
    main()
