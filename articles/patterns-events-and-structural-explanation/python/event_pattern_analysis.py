"""
Event-pattern analysis for "Patterns, Events, and Structural Explanation".

This script groups synthetic event records to show how repeated events become
patterns worthy of structural explanation.
"""

from __future__ import annotations

import csv
from collections import Counter, defaultdict
from pathlib import Path

DATA_PATH = Path(__file__).resolve().parents[1] / "data" / "synthetic_events.csv"


def load_events(path: Path = DATA_PATH) -> list[dict[str, str]]:
    with path.open(newline="", encoding="utf-8") as handle:
        return list(csv.DictReader(handle))


def summarize_patterns(events: list[dict[str, str]]) -> None:
    by_type = Counter(event["event_type"] for event in events)
    by_location = Counter(event["location"] for event in events)
    by_area: dict[str, list[int]] = defaultdict(list)

    for event in events:
        by_area[event["system_area"]].append(int(event["severity"]))

    print("Events by type")
    for event_type, count in by_type.most_common():
        print(f"- {event_type}: {count}")

    print("\nEvents by location")
    for location, count in by_location.most_common():
        print(f"- {location}: {count}")

    print("\nAverage severity by system area")
    for area, severities in sorted(by_area.items()):
        average = sum(severities) / len(severities)
        print(f"- {area}: {average:.2f}")


def main() -> None:
    events = load_events()
    summarize_patterns(events)


if __name__ == "__main__":
    main()
