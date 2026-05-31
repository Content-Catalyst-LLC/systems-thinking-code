from __future__ import annotations

from common import write_csv

EDGES = [
    ("Frontline", "Manager", 0.72, 2),
    ("Manager", "Director", 0.58, 3),
    ("Customer", "Support", 0.80, 1),
    ("Support", "Product", 0.46, 4),
    ("Operations", "Strategy", 0.40, 5),
    ("Community", "Executive", 0.31, 6),
]


def main() -> None:
    rows = []
    for source, target, signal_strength, delay in EDGES:
        learning_value = max(0.0, signal_strength - (delay * 0.06))
        rows.append({
            "source": source,
            "target": target,
            "signal_strength": signal_strength,
            "delay": delay,
            "learning_value": round(learning_value, 3),
        })
    out = write_csv("information_flow_network.csv", rows, ["source", "target", "signal_strength", "delay", "learning_value"])
    print(f"Wrote {out}")


if __name__ == "__main__":
    main()
