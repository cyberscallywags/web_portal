import os

import requests

# from app.services.models.event_schema import Event

# API_BASE = os.getenv("API_BASE", "https://api.cyberscallywags.uk")

listings = [
    {
        "id": 1,
        "name": "CyberScallywags Workshop",
        "description": "First proper in-person working Group",
        "date": "2025-10-04T09:00:00Z",
        "location": "UnCommon Holborn, London",
        "organizer": "Cyber Scallywags Exec Team",
        "createdAt": "2025-10-01T10:00:00Z",
        "lastUpdated": "2025-10-02T19:00:00Z"
    },
    {
        "id": 2,
        "name": "CyberScallywags Workshop",
        "description": "Second proper in-person working Group",
        "date": "2025-11-01T11:00:00Z",
        "location": "OSB (Observer building) Hastings, East Sussex",
        "organizer": "Cyber Scallywags Exec Team",
        "createdAt": "2025-10-25T10:00:00Z",
        "lastUpdated": "2025-10-29T19:00:00Z"
    },
    {
        "id": 3,
        "name": "Python for Data Science",
        "description": "Introduction to data analysis and visualization using Python, pandas, and matplotlib. Perfect for beginners!",
        "date": "2026-02-20T10:00:00Z",
        "location": "Online (Zoom)",
        "organizer": "Dr. Sarah Chen",
        "createdAt": "2025-11-01T10:00:00Z",
        "lastUpdated": "2025-11-20T12:00:00Z"
    },
    {
        "id": 4,
        "name": "AI & Machine Learning Summit",
        "description": "A full-day conference featuring industry experts discussing the latest trends in AI and machine learning applications.",
        "date": "2026-03-15T09:00:00Z",
        "location": "Birmingham Conference Centre",
        "organizer": "Tech Innovators UK",
        "createdAt": "2025-11-05T10:00:00Z",
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
