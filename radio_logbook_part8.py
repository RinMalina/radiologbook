# === Stage 8: Фильтрация записей ===
# Project: RadioLogbook
from datetime import datetime

def filter_by_band(records, band, ignore_case=True):
    """Return records whose band field matches the requested band value.
    Comparison is case-insensitive when ignore_case is True."""
    normalized = band.strip().lower() if ignore_case else band
    return [r for r in records if str(r.get("band", "")).lower() == normalized]


def filter_by_date_range(records, start_date, end_date):
    """Return records whose date falls within [start_date, end_date].
    Accepts datetime, date, or string (ISO format) for the boundaries."""
    def parse(value):
        if isinstance(value, str):
            return datetime.fromisoformat(value)
        return value

    start = parse(start_date)
    end = parse(end_date)
    filtered = []
    for record in records:
        raw = record.get("date")
        try:
            record_date = parse(raw)
        except (ValueError, TypeError):
            continue
        if start <= record_date <= end:
            filtered.append(record)
    return filtered


def filter_by_band_and_date(records, band, start_date, end_date):
    """Combine band and date-range filters for a single pass over records."""
    return filter_by_date_range(filter_by_band(records, band), start_date, end_date)


def filter_by_multiple_bands(records, bands):
    """Return records whose band matches any value in the provided list."""
    normalized = set(b.strip().lower() for b in bands)
    return [r for r in records if str(r.get("band", "")).lower() in normalized]


def filter_by_call_sign(records, call_sign, ignore_case=True):
    """Return records whose callsign field matches the provided value."""
    normalized = call_sign.strip().lower() if ignore_case else call_sign
    return [r for r in records if str(r.get("callsign", "")).lower() == normalized]


def filter_records(records, band=None, date_range=None, call_sign=None, bands=None):
    """Apply all provided filters in sequence and return the resulting list.
    Each argument is optional; unspecified filters are skipped.
    date_range should be a (start_date, end_date) tuple."""
    result = records
    if bands is not None:
        result = filter_by_multiple_bands(result, bands)
    elif band is not None:
        result = filter_by_band(result, band)
    if call_sign is not None:
        result = filter_by_call_sign(result, call_sign)
    if date_range is not None:
        start, end = date_range
        result = filter_by_date_range(result, start, end)
    return result
