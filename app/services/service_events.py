import os

import requests

# from app.services.models.event_schema import Event

# API_BASE = os.getenv("API_BASE", "https://api.cyberscallywags.uk")

listings = [
    {
        "id": 1,
        "name": "First Event",
        "description": "This is the description of the first event.",
        "date": "2026-01-20T12:00:00Z",
        "location": "Location One",
        "organizer": "Organizer One",
        "createdAt": "2025-10-15T10:00:00Z",
        "lastUpdated": "2025-11-20T12:00:00Z"
    },
    {
        "id": 2,
        "name": "Second Event",
        "description": "This is the description of the second event.",
        "date": "2026-02-30T12:00:00Z",
        "location": "Location Two",
        "organizer": "Organizer Two",
        "createdAt": "2025-10-15T10:00:00Z",
        "lastUpdated": "2025-11-20T12:00:00Z"
    },
]


def get_all_events():
    # resp = requests.get(f"{API_BASE}/events")

    data = {'events': listings}
    return data


if __name__ == "__main__":
    lst = get_all_events()
    print(f"All events: {lst}")
