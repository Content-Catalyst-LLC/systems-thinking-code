from __future__ import annotations

from collections import defaultdict

from _common import f, read_csv, write_csv

by_domain: dict[str, list[dict[str, str]]] = defaultdict(list)
for row in read_csv("synthetic_feedback_signals.csv"):
    by_domain[row["domain"]].append(row)

rows = []
for domain, signals in sorted(by_domain.items()):
    n = len(signals)
    acted = sum(1 for row in signals if f(row, "acted_upon") >= 1)
    closed = sum(1 for row in signals if f(row, "loop_closed") >= 1)
    context = sum(1 for row in signals if f(row, "context_preserved") >= 1)
    rows.append({
        "domain": domain,
        "signals_received": n,
        "acted_upon_rate": round(acted / n, 3),
        "loop_closed_rate": round(closed / n, 3),
        "context_preserved_rate": round(context / n, 3),
    })

write_csv("policy_feedback_closure.csv", rows)
