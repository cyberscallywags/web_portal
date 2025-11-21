import os

import requests

# from app.services.models.event_schema import Event

# API_BASE = os.getenv("API_BASE", "https://api.cyberscallywags.uk")

listings = [
    {
        "id": 1,
        "name": "Cybersecurity Workshop",
        "description": "Learn essential cybersecurity practices and protect yourself from common threats. Hands-on workshop covering network security, password management, and threat detection.",
        "date": "2025-12-15T14:00:00Z",
        "location": "Tech Hub London, Floor 3",
        "organizer": "Cyber Scallywags Team",
        "createdAt": "2025-10-15T10:00:00Z",
        "lastUpdated": "2025-11-20T12:00:00Z"
    },
    {
        "id": 2,
        "name": "Web Development Meetup",
        "description": "Join us for an evening of web development talks and networking. Topics include React, Vue, and modern JavaScript frameworks.",
        "date": "2026-01-10T18:30:00Z",
        "location": "Innovation Centre Manchester",
        "organizer": "Cyber Scallywags Team",
        "createdAt": "2025-10-15T10:00:00Z",
        "lastUpdated": "2025-11-20T12:00:00Z"
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
