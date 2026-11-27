# === Stage 11: Постраничный вывод ===
# Project: RadioLogbook
from typing import Iterable, List, Optional

DEFAULT_PAGE_SIZE = 20
DEFAULT_PAGE_NUMBER = 1


def page_size(page_size: Optional[int], count: int) -> int:
    if page_size is None:
        return DEFAULT_PAGE_SIZE
    try:
        value = int(page_size)
    except (TypeError, ValueError):
        return DEFAULT_PAGE_SIZE
    if value <= 0:
        return DEFAULT_PAGE_SIZE
    if value > count and count > 0:
        return count
    return value


def page_number(page_number: Optional[int], count: int) -> int:
    if page_number is None:
        return DEFAULT_PAGE_NUMBER
    try:
        value = int(page_number)
    except (TypeError, ValueError):
        return DEFAULT_PAGE_NUMBER
    if value < 1:
        return DEFAULT_PAGE_NUMBER
    if value > _last_page(count, page_size(page_number, count)):
        return _last_page(count, page_size(page_number, count))
    return value


def last_page(count: int, page_size: Optional[int] = None) -> int:
    size = page_size(page_size, count)
    if count <= 0:
        return 1
    return max(1, (count + size - 1) // size)


def page_range(count: int, page_number: Optional[int] = None, page_size: Optional[int] = None) -> range:
    start = (page_number(page_number, count) - 1) * page_size(page_size, count)
    end = min(start + page_size(page_size, count), count)
    if start >= end:
        return range(0, 0)
    return range(start, end)


def paginated_contacts(
    contacts: Iterable,
    page_number: Optional[int] = None,
    page_size: Optional[int] = None,
) -> List:
    items = list(contacts)
    return items[page_range(len(items), page_number, page_size)]


def total_pages(contacts: Iterable, page_size: Optional[int] = None) -> int:
    return last_page(len(list(contacts)), page_size)
