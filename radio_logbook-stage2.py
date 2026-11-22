# === Stage 2: Проверка полей ===
# Project: RadioLogbook
import datetime


def normalize_call_sign(raw):
    """Normalize a callsign: strip whitespace, drop non-alphanumeric chars,
    collapse internal whitespace, and return the cleaned value."""
    cleaned = "".join(ch for ch in raw if ch.isalnum())
    cleaned = "".join(cleaned.split())
    return cleaned


DATE_FORMAT = "%Y-%m-%d"


def normalize_date(raw):
    """Parse a user date string into a datetime.date. Returns None on failure."""
    if not raw or not isinstance(raw, str):
        return None
    try:
        return datetime.datetime.strptime(raw.strip(), DATE_FORMAT).date()
    except (ValueError, TypeError):
        return None


def normalize_band(raw):
    """Map a user band name to a canonical band identifier.
    Returns None if the input does not match a known band."""
    bands = {
        "hf": "HF",
        "160m": "HF",
        "80m": "HF",
        "60m": "HF",
        "40m": "HF",
        "30m": "HF",
        "20m": "HF",
        "17m": "HF",
        "15m": "HF",
        "12m": "HF",
        "10m": "HF",
        "6m": "HF",
        "2m": "VHF",
        "70cm": "VHF",
        "23cm": "UHF",
        "uhf": "UHF",
        "microwave": "UHF",
    }
    key = normalize_call_sign(raw).lower()
    return bands.get(key)


def normalize_report(raw):
    """Normalize a QSO report into uppercase, stripping surrounding spaces."""
    if not raw:
        return ""
    return raw.strip().upper()


FIELD_ERROR_MESSAGES = {
    "date": "Please enter a valid date in YYYY-MM-DD format.",
    "band": "Please select a valid band.",
    "call_sign": "Callsign cannot be empty.",
    "report": "Report cannot be empty.",
}


def validate_qso(qso):
    """Validate a QSO dictionary. Returns a list of human-readable error
    messages. An empty list means the QSO is valid."""
    errors = []

    date_value = normalize_date(qso.get("date"))
    if date_value is None:
        errors.append(FIELD_ERROR_MESSAGES["date"])
    else:
        qso["date"] = date_value

    band_value = normalize_band(qso.get("band"))
    if band_value is None:
        errors.append(FIELD_ERROR_MESSAGES["band"])
    else:
        qso["band"] = band_value

    call_sign = normalize_call_sign(qso.get("call_sign"))
    if not call_sign:
        errors.append(FIELD_ERROR_MESSAGES["call_sign"])
    else:
        qso["call_sign"] = call_sign

    report = normalize_report(qso.get("report"))
    if not report:
        errors.append(FIELD_ERROR_MESSAGES["report"])
    else:
        qso["report"] = report

    return errors
