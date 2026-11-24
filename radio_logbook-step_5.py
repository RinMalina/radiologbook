# === Stage 5: Удаление и восстановление ===
# Project: RadioLogbook
def soft_delete_entry(logbook, entry_id):
    for entry in logbook["entries"]:
        if entry["id"] == entry_id:
            entry["deleted"] = True
            entry["deleted_at"] = datetime.datetime.now(datetime.timezone.utc).isoformat()
            logbook["deleted_ids"].append(entry_id)
            return True
    return False


def restore_entry(logbook, entry_id):
    if entry_id not in logbook.get("deleted_ids", []):
        return False
    logbook["deleted_ids"].remove(entry_id)
    for entry in logbook["entries"]:
        if entry["id"] == entry_id:
            entry["deleted"] = False
            entry.pop("deleted_at", None)
            return True
    return False


def permanently_delete_entry(logbook, entry_id):
    for entry in logbook["entries"]:
        if entry["id"] == entry_id:
            logbook["entries"].remove(entry)
            if entry_id in logbook["deleted_ids"]:
                logbook["deleted_ids"].remove(entry_id)
            return True
    return False


def list_deleted_entries(logbook):
    return [
        dict(entry)
        for entry in logbook["entries"]
        if entry.get("deleted")
    ]


def get_entry(logbook, entry_id):
    for entry in logbook["entries"]:
        if entry["id"] == entry_id:
            return dict(entry)
    return None


def remove_entry(logbook, entry_id):
    if get_entry(logbook, entry_id) is None:
        return False
    permanently_delete_entry(logbook, entry_id)
    return True


def purge_deleted_entries(logbook):
    logbook["entries"] = [entry for entry in logbook["entries"] if not entry.get("deleted")]
    logbook["deleted_ids"] = []
    return True
