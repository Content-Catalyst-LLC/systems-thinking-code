#!/usr/bin/env python3
"""Small preferential-attachment demonstration for visibility and network advantage."""
from __future__ import annotations
import random
from collections import Counter
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / "outputs" / "tables"
OUT.mkdir(parents=True, exist_ok=True)

random.seed(42)
nodes = ["A001", "A002", "A003", "A004", "A005"]
degrees = Counter({node: 1 for node in nodes})

for step in range(100):
    population = []
    for node, degree in degrees.items():
        population.extend([node] * degree)
    target = random.choice(population)
    new_node = f"N{step:03d}"
    degrees[new_node] += 1
    degrees[target] += 1

with (OUT / "preferential_attachment_degrees.csv").open("w") as f:
    f.write("node,degree\n")
    for node, degree in degrees.most_common():
        f.write(f"{node},{degree}\n")

print(f"Wrote {OUT / 'preferential_attachment_degrees.csv'}")
