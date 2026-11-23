# === Stage 4: Редактирование записей ===
# Project: RadioLogbook
ALLOWED_CONNECTION_FIELDS = {"date", "band", "callsign", "report"}


def edit_connection(connection_id, changes, connections):
    for connection in connections:
        if connection["id"] == connection_id:
            for field, value in changes.items():
                if field not in ALLOWED_CONNECTION_FIELDS:
                    raise ValueError(f"Field '{field}' cannot be updated")
                connection[field] = value
            return connection
    return None


def is_valid_update(changes):
    return all(field in ALLOWED_CONNECTION_FIELDS for field in changes)
