# === Stage 1: Каркас модуля ===
# Project: RadioLogbook
from __future__ import annotations

from dataclasses import dataclass, field
from datetime import date
from typing import List


@dataclass
class QSO:
    """A single radio-contact record."""

    date: date
    band: str
    callsign: str
    report: str
    notes: str = ""

    def summary(self) -> str:
        """Return a one-line human-readable summary of the record."""
        return f"{self.date.isoformat()} {self.band} {self.callsign} {self.report}"


def demo_records() -> List[QSO]:
    """Create a handful of demonstration QSO records."""
    return [
        QSO(date(2024, 1, 15), "20m", "DL1ABC", "59"),
        QSO(date(2024, 2, 20), "40m", "EA2XYZ", "57"),
        QSO(date(2024, 3, 3), "15m", "W4QRS", "59"),
    ]


def main() -> None:
    """Print a short overview of the demo logbook."""
    records = demo_records()
    print("RadioLogbook demo")
    print(f"Total contacts: {len(records)}")
    for record in records:
        print("  " + record.summary())


if __name__ == "__main__":
    main()
