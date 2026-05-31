from __future__ import annotations

from collections import defaultdict

from _common import f, read_csv, write_csv

by_domain: dict[str, list[dict[str, str]]] = defaultdict(list)
for row in read_csv("synthetic_feedback_signals.csv"):
    by_domain[row["domain"]].append(row)

rows = []
for domain, items in sorted(by_domain.items()):
    received = len(items)
    acted = sum(1 for row in items if f(row, "acted_upon") >= 1)
    closed = sum(1 for row in items if f(row, "loop_closed") >= 1)
    context = sum(1 for row in items if f(row, "context_preserved") >= 1)
    rows.append({
        "domain": domain,
        "feedback_received": received,
        "acted_upon_rate": round(acted / received, 3),
        "loop_closed_rate": round(closed / received, 3),
        "context_preserved_rate": round(context / received, 3),
    })

write_csv("feedback_loop_closure.csv", rows)
