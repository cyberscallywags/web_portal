import os

import requests

from models.blog_schema import Event

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


def get_all_events() -> list[Event]:
    # resp = requests.get(f"{API_BASE}/events")

    data = {'events': listings}
    return data


if __name__ == "__main__":

    lst = get_all_blogs()
    print(f" A blogs in a lst :: {lst}")


id: int = Field(..., description="The unique identifier for the event")
    name: str = Field(..., description="The name of the event")
    date: str = Field(..., description="The date of the event")
    location: str = Field(..., description="The location of the event")
    description: str = Field(..., description="A brief description of the event")
    createdAt: str = Field(..., description="The date and time when the event was created")
    lastUpdated: str = Field(..., description="The date and time when the event was last updated")