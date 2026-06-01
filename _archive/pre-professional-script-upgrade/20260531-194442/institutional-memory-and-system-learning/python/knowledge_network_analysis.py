from __future__ import annotations

from collections import Counter

from _common import read_csv, write_csv

owners = Counter(row["owner_role"] for row in read_csv("synthetic_memory_assets.csv"))
rows = []
for role, count in owners.most_common():
    bottleneck_risk = "high" if count >= 2 else "moderate"
    rows.append({"owner_role": role, "memory_assets_owned": count, "bottleneck_risk": bottleneck_risk})

write_csv("knowledge_network_analysis.csv", rows)
