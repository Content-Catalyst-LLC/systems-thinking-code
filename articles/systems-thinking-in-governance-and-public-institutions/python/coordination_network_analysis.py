from __future__ import annotations

from collections import Counter, defaultdict

from _common import f, read_csv, write_csv

edges = read_csv("synthetic_coordination_edges.csv")
degree: Counter[str] = Counter()
strength: defaultdict[str, float] = defaultdict(float)
for row in edges:
    s = row["source"]
    t = row["target"]
    weight = (f(row, "frequency") + f(row, "trust") + f(row, "shared_data") + f(row, "shared_authority")) / 4
    degree[s] += 1
    degree[t] += 1
    strength[s] += weight
    strength[t] += weight

rows = []
for node in sorted(degree):
    rows.append({
        "institution": node,
        "coordination_degree": degree[node],
        "coordination_strength": round(strength[node], 3),
        "bridge_role": "high" if degree[node] >= 3 else "moderate",
    })

write_csv("coordination_network_analysis.csv", rows)
