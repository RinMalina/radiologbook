# === Stage 7: Генерация идентификаторов ===
# Project: RadioLogbook
import uuid


PROJECT_ID_PREFIX = "RADIOLOGBOOK"


def generate_unique_id():
    """Return a unique identifier with the project prefix and collision check."""
    counter = {}

    def _is_unique(candidate):
        return candidate not in counter

    def _register(candidate):
        counter[candidate] = counter.get(candidate, 0) + 1

    while True:
        candidate = f"{PROJECT_ID_PREFIX}-{uuid.uuid4().hex}"
        if _is_unique(candidate):
            _register(candidate)
            return candidate
