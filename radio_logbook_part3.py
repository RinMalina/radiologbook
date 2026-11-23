# === Stage 3: Хранилище в памяти ===
# Project: RadioLogbook
import uuid
from datetime import datetime


class RadioLogbookMemoryStore:
    """In-memory storage for radio logbook contacts."""

    def __init__(self):
        self._contacts = {}

    def add_contact(self, call_sign, band, mode, time, report, date=None, id=None):
        contact_id = id or str(uuid.uuid4())
        if date is None:
            date = datetime.now().date()
        self._contacts[contact_id] = {
            "id": contact_id,
            "call_sign": call_sign,
            "band": band,
            "mode": mode,
            "time": time,
            "report": report,
            "date": date.isoformat(),
        }
        return contact_id

    def get_contact(self, contact_id):
        return self._contacts.get(contact_id)

    def list_contacts(self):
        return list(self._contacts.values())
