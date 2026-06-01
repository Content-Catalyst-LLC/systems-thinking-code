"""
Causal network analysis for systems thinking.

Edges include signs to indicate positive or negative influence.
"""

from __future__ import annotations

import pandas as pd
import networkx as nx


def build_causal_network() -> nx.DiGraph:
    edges = [
        ("Learning", "Adaptive Capacity", "+"),
        ("Adaptive Capacity", "Resilience", "+"),
        ("Resilience", "Recovery Speed", "+"),
        ("Disruption Pressure", "Capacity", "-"),
        ("Capacity", "Service Quality", "+"),
        ("Service Quality", "Public Trust", "+"),
        ("Public Trust", "Cooperation", "+"),
        ("Cooperation", "Adaptive Capacity", "+"),
        ("Administrative Burden", "Public Trust", "-"),
        ("Resource Depletion", "Capacity", "-")
    ]

    graph = nx.DiGraph()

    for source, target, sign in edges:
        graph.add_edge(source, target, sign=sign)

    return graph


def graph_metrics(graph: nx.DiGraph) -> pd.DataFrame:
    centrality = nx.degree_centrality(graph)
    betweenness = nx.betweenness_centrality(graph)

    return pd.DataFrame({
        "node": list(graph.nodes()),
        "in_degree": [graph.in_degree(node) for node in graph.nodes()],
        "out_degree": [graph.out_degree(node) for node in graph.nodes()],
        "degree_centrality": [centrality[node] for node in graph.nodes()],
        "betweenness": [betweenness[node] for node in graph.nodes()]
    }).sort_values("degree_centrality", ascending=False)


def main() -> None:
    graph = build_causal_network()
    metrics = graph_metrics(graph)

    print(metrics)
    metrics.to_csv("../outputs/causal_network_metrics.csv", index=False)


if __name__ == "__main__":
    main()
