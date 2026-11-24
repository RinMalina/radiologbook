# === Stage 6: Связи между сущностями ===
# Project: RadioLogbook
# RadioLogbook - Stage 6: correspondent retrieval and link integrity check
# A self-contained module. Standard library only. No external references.

from datetime import date


class Correspondent:
    """A station contacted on a link."""

    def __init__(self, callsign, qso_date=None):
        self.callsign = callsign
        self.qso_date = qso_date or date.today()

    def __repr__(self):
        return f"Correspondent({self.callsign!r}, {self.qso_date!r})"


class Link:
    """A QSO record."""

    def __init__(self, qso_date, band, callsign, report):
        self.qso_date = qso_date
        self.band = band
        self.callsign = callsign
        self.report = report

    def __repr__(self):
        return (f"Link({self.qso_date!r}, {self.band!r}, "
                f"{self.callsign!r}, {self.report!r})")


def get_correspondents(link, contacts):
    """Return all Correspondent objects matching the given link.

    A correspondent matches the link when both the callsign and the date
    agree with the link's fields. Missing date fields are treated as today.
    """
    result = []
    for contact in contacts:
        if isinstance(contact, Correspondent):
            if contact.callsign == link.callsign:
                if contact.qso_date == link.qso_date:
                    result.append(contact)
    return result


def check_link_integrity(link, contacts):
    """Validate a link against the available contacts.

    Returns a tuple (is_valid, message).

    - is_valid is True when at least one matching correspondent exists.
    - The message explains the outcome or lists the matching callsigns.
    """
    matches = get_correspondents(link, contacts)
    if not matches:
        return False, "No matching correspondent found for the given link."
    callsigns = sorted({m.callsign for m in matches})
    return True, f"Link confirmed with {len(callsigns)} correspondent(s): {callsigns}."


if __name__ == "__main__":
    demo = [
        Correspondent("DL1ABC", date(2024, 5, 1)),
        Correspondent("DL1ABC", date(2024, 6, 1)),
        Correspondent("DL2XYZ", date(2024, 5, 1)),
    ]
    link = Link(date(2024, 5, 1), "20m", "DL1ABC", "59")

    print("Correspondents for link:", get_correspondents(link, demo))
    print("Integrity check:", check_link_integrity(link, demo))

    missing = Link(date(2030, 1, 1), "40m", "DL9NOPE", "59")
    print("Integrity check (missing):", check_link_integrity(missing, demo))
