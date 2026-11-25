# === Stage 9: Сортировка записей ===
# Project: RadioLogbook
from datetime import datetime


def _parse_date(value):
    return datetime.fromisoformat(value)


def sort_calls_by_date(calls, descending=False):
    return sorted(calls, key=_parse_date, reverse=descending)


def sort_calls_by_created_at(calls, descending=False):
    return sorted(calls, key=lambda call: call.created_at, reverse=descending)


def sort_calls(calls, field="date", descending=False):
    if field == "created_at":
        return sort_calls_by_created_at(calls, descending=descending)
    return sort_calls_by_date(calls, descending=descending)
