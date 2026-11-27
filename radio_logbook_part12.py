# === Stage 12: Слияние записей ===
# Project: RadioLogbook
def merge_contacts(
    records,
    date_wins="first",
    band_wins="first",
    callsign_wins="first",
    qso_wins="first",
):
    """Merge two QSO records field by field.

    For every field choose a winner between the two records. The winner
    selection rule is supplied per field (date, band, callsign, qso) and
    one of the four constants below:

      first  - take the value from the earlier record in the list
      second - take the value from the later record in the list
      longer - take the longer (more detailed) value
      other  - take the value from the record that is not the first one

    ``records`` must contain exactly two contact dicts. The returned dict
    has the same keys as the input records.
    """
    if len(records) != 2:
        raise ValueError("merge_contacts expects exactly two records")

    earlier, later = records

    def pick(rule, field):
        if rule == "first":
            return earlier.get(field)
        if rule == "second":
            return later.get(field)
        if rule == "longer":
            return later.get(field) if later.get(field) else earlier.get(field)
        if rule == "other":
            return later.get(field)
        raise ValueError(f"unknown winner rule: {rule!r}")

    merged = {
        "date": pick(date_wins, "date"),
        "band": pick(band_wins, "band"),
        "callsign": pick(callsign_wins, "callsign"),
        "qso": pick(qso_wins, "qso"),
    }
    return merged


def merge_records(
    records,
    date_wins="first",
    band_wins="first",
    callsign_wins="first",
    qso_wins="first",
):
    """Merge two contact records and return the combined record.

    Each parameter selects the winner of the corresponding field between
    the two records. See :func:`merge_contacts` for the meaning of the
    rules. The first argument must be a list of exactly two dicts.
    """
    return merge_contacts(
        records,
        date_wins=date_wins,
        band_wins=band_wins,
        callsign_wins=callsign_wins,
        qso_wins=qso_wins,
    )
