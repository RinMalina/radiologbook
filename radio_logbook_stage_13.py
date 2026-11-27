# === Stage 13: Избранное ===
# Project: RadioLogbook
from typing import Optional

FAVORITE = "favorite"


class FavoriteBookmarks:
    def __init__(self) -> None:
        self._bookmarks: set[str] = set()

    def add(self, callsign: str) -> None:
        self._bookmarks.add(callsign.upper())

    def remove(self, callsign: str) -> None:
        self._bookmarks.discard(callsign.upper())

    def is_favorite(self, callsign: str) -> bool:
        return callsign.upper() in self._bookmarks

    def favorites(self) -> list[str]:
        return sorted(self._bookmarks)

    def __len__(self) -> int:
        return len(self._bookmarks)


def mark_favorite(bookmarks: FavoriteBookmarks, callsign: str) -> bool:
    if bookmarks.is_favorite(callsign):
        return False
    bookmarks.add(callsign)
    return True


def unmark_favorite(bookmarks: FavoriteBookmarks, callsign: str) -> bool:
    if not bookmarks.is_favorite(callsign):
        return False
    bookmarks.remove(callsign)
    return True


def toggle_favorite(
    bookmarks: FavoriteBookmarks, callsign: str
) -> Optional[bool]:
    if bookmarks.is_favorite(callsign):
        return unmark_favorite(bookmarks, callsign)
    return mark_favorite(bookmarks, callsign)


def format_favorite_list(bookmarks: FavoriteBookmarks) -> str:
    lines = ["Favorites:"]
    if not bookmarks:
        lines.append("  (none)")
        return "\n".join(lines)
    for callsign in bookmarks.favorites():
        lines.append(f"  {callsign}")
    return "\n".join(lines)


def favorite_of(callsign: str) -> bool:
    return FAVORITE in callsign.upper()


def is_favorite_callsign(callsign: str) -> bool:
    return callsign.upper() == FAVORITE
