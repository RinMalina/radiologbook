# === Stage 14: Смена статуса ===
# Project: RadioLogbook
from enum import Enum


class QSOStatus(Enum):
    """Status of a QSO record."""
    LOGGED = "logged"
    CONFIRMED = "confirmed"
    DISPUTED = "disputed"
    DELETED = "deleted"


class StatusTransition(Enum):
    """Allowed transitions between QSO statuses."""
    LOGGED_TO_CONFIRMED = ("logged", "confirmed")
    CONFIRMED_TO_DISPUTED = ("confirmed", "disputed")
    DISPUTED_TO_CONFIRMED = ("disputed", "confirmed")
    DISPUTED_TO_DELETED = ("disputed", "deleted")
    CONFIRMED_TO_DELETED = ("confirmed", "deleted")
    LOGGED_TO_DELETED = ("logged", "deleted")
