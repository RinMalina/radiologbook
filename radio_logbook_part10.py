# === Stage 10: Поиск по нескольким словам ===
# Project: RadioLogbook
from __future__ import annotations


def parse_query(query: str) -> list[tuple[str, ...]]:
    query = query.strip()
    if not query:
        return []
    terms = []
    for token in query.split():
        if token.startswith("-"):
            terms.append("-" + token[1:].strip().lower())
        else:
            terms.append(token.strip().lower())
    return tuple(terms)


def tokenize_call(call: str) -> list[str]:
    call = call.strip().lower()
    if not call:
        return []
    return [part.strip() for part in call.replace("/", " ").split() if part.strip()]


def matches(call: str, required: list[str], exclusions: list[str]) -> bool:
    tokens = tokenize_call(call)
    if not tokens:
        return False
    required = [t for t in required if t]
    if required and not all(t in tokens for t in required):
        return False
    exclusions = [e for e in exclusions if e]
    if exclusions and any(e in tokens for e in exclusions):
        return False
    return True


def find_calls(calls: list[str], query: str) -> list[str]:
    terms = parse_query(query)
    required: list[str] = []
    exclusions: list[str] = []
    for term in terms:
        if term.startswith("-"):
            exclusions.append(term[1:].strip().lower())
        else:
            required.append(term.strip().lower())
    result: list[str] = []
    for call in calls:
        if matches(call, required, exclusions):
            result.append(call)
    return result
