import os

import requests

# from app.services.models.event_schema import Event

# API_BASE = os.getenv("API_BASE", "https://api.cyberscallywags.uk")

listings = [
    {
        "id": 1,
        "name": "CyberScallywags Workshop",
        "emoji": "💻",
        "event_type": "Workshop",
        "status": "upcoming",
        "description": "First proper in-person working group — hands-on hacking, mentoring, and community building.",
        "long_description": (
            "Our inaugural in-person Working Group brings the CyberScallywags community "
            "together for a full day of hands-on technical work, peer mentoring, and "
            "collaborative problem solving. Expect lightning talks, breakout sessions on "
            "current open-source projects, and plenty of time to pair with other engineers "
            "on real codebases."
        ),
        "date": "2025-10-04T09:00:00Z",
        "end_date": "2025-10-04T17:00:00Z",
        "timezone": "Europe/London",
        "location": "UnCommon Holborn",
        "address": "34 Procter Street, Holborn, London WC1V 6NX",
        "is_online": False,
        "meeting_url": None,
        "organizer": "Cyber Scallywags Exec Team",
        "organizer_url": "https://cyberscallywags.uk",
        "speakers": [
            {
                "name": "Colin Moore-Hill",
                "role": "Community Lead",
                "avatar": "🌐",
                "bio": "Founder of CyberScallywags, focused on graph databases and community-driven engineering."
            },
            {
                "name": "Dean Foulds",
                "role": "Design & Frontend",
                "avatar": "🎨",
                "bio": "Frontend craft and design systems for the DSF Companion project."
            }
        ],
        "agenda": [
            {"time": "09:00", "title": "Doors & Coffee", "description": "Arrival, registration, and warm-up."},
            {"time": "10:00", "title": "Opening Talk", "description": "What CyberScallywags is building this year."},
            {"time": "11:00", "title": "Working Group Sessions", "description": "Breakouts: graph DBs, AI tooling, web platform."},
            {"time": "13:00", "title": "Lunch", "description": "Provided. Vegetarian and vegan options available."},
            {"time": "14:00", "title": "Pair Programming", "description": "Paired sessions on live community projects."},
            {"time": "16:30", "title": "Wrap & Demos", "description": "Show-and-tell from the day's work."},
        ],
        "tags": ["Workshop", "Community", "Open Source"],
        "capacity": 40,
        "registered_count": 28,
        "is_sold_out": False,
        "is_free": True,
        "price": None,
        "image_url": None,
        "registration_url": None,
        "prerequisites": ["Laptop with development environment", "GitHub account"],
        "createdAt": "2025-10-01T10:00:00Z",
        "lastUpdated": "2025-10-02T19:00:00Z",
    },
    {
        "id": 2,
        "name": "CyberScallywags Workshop — Hastings",
        "emoji": "🌊",
        "event_type": "Workshop",
        "status": "upcoming",
        "description": "Second in-person working group — coastal edition at the Observer Building.",
        "long_description": (
            "We're heading to the south coast for the second CyberScallywags Working Group. "
            "Hosted at the historic Observer Building in Hastings, this session focuses on "
            "regional community building, AI-augmented developer workflows, and shipping "
            "from outside the London bubble."
        ),
        "date": "2025-11-01T11:00:00Z",
        "end_date": "2025-11-01T18:00:00Z",
        "timezone": "Europe/London",
        "location": "OSB (Observer Building)",
        "address": "Claremont, Hastings, East Sussex TN34 1HE",
        "is_online": False,
        "meeting_url": None,
        "organizer": "Cyber Scallywags Exec Team",
        "organizer_url": "https://cyberscallywags.uk",
        "speakers": [
            {
                "name": "Colin Moore-Hill",
                "role": "Community Lead",
                "avatar": "🌐",
                "bio": "Founder of CyberScallywags, focused on graph databases and community-driven engineering."
            }
        ],
        "agenda": [
            {"time": "11:00", "title": "Doors & Coffee", "description": "Arrival and intros."},
            {"time": "12:00", "title": "Regional Communities Panel", "description": "Building dev community outside major cities."},
            {"time": "13:30", "title": "Lunch", "description": "Local catering."},
            {"time": "14:30", "title": "AI Tooling Hack", "description": "Hands-on with AI-assisted dev tools."},
            {"time": "17:30", "title": "Wrap & Networking", "description": "Pub afterwards (optional)."},
        ],
        "tags": ["Workshop", "Community", "Regional"],
        "capacity": 30,
        "registered_count": 12,
        "is_sold_out": False,
        "is_free": True,
        "price": None,
        "image_url": None,
        "registration_url": None,
        "prerequisites": ["Laptop"],
        "createdAt": "2025-10-25T10:00:00Z",
        "lastUpdated": "2025-10-29T19:00:00Z",
    },
    {
        "id": 3,
        "name": "DSF Birthday Bash",
        "emoji": "🎂",
        "event_type": "Talk",
        "status": "upcoming",
        "description": "Talk: Introduction to Context as the brain of AI — celebrating one year of DSF Companion.",
        "long_description": (
            "Join us at Codenode to celebrate the first birthday of the DSF Companion project. "
            "The headline talk explores how context engineering — not model size — is the real "
            "lever for useful AI systems, with live examples from the Companion stack. "
            "Cake, drinks, and demos to follow."
        ),
        "date": "2026-05-16T11:00:00Z",
        "end_date": "2026-05-16T15:00:00Z",
        "timezone": "Europe/London",
        "location": "CodeNode",
        "address": "10 South Place, London EC2M 7EB",
        "is_online": False,
        "meeting_url": None,
        "organizer": "Create Communities",
        "organizer_url": "https://createcommunities.org",
        "speakers": [
            {
                "name": "Colin Moore-Hill",
                "role": "Speaker",
                "avatar": "🧠",
                "bio": "Talking about context engineering as the real brain of modern AI systems."
            }
        ],
        "agenda": [
            {"time": "11:00", "title": "Keynote: Context as the Brain of AI", "description": "Why context engineering wins over model size."},
        ],
        "tags": ["AI", "Talk", "Community", "Birthday"],
        "capacity": 600,
        "registered_count": 575,
        "is_sold_out": False,
        "is_free": True,
        "price": None,
        "image_url": None,
        "registration_url": None,
        "prerequisites": [],
        "createdAt": "2025-11-01T10:00:00Z",
        "lastUpdated": "2025-11-20T12:00:00Z",
    },
    {
        "id": 4,
        "name": "AI & Machine Learning Summit",
        "emoji": "🤖",
        "event_type": "Conference",
        "status": "upcoming",
        "description": "A full-day online conference featuring community experts on the latest trends in AI and ML.",
        "long_description": (
            "Pydantic-Aura UK presents a full-day virtual summit gathering practitioners "
            "across the UK AI/ML community. Expect deep-dive talks on retrieval, agents, "
            "evaluation, and production deployment, plus an open panel on the state of "
            "open-weight models. All sessions recorded and shared with attendees afterwards."
        ),
        "date": "2026-06-25T09:00:00Z",
        "end_date": "2026-06-25T17:00:00Z",
        "timezone": "Europe/London",
        "location": "Online (Zoom)",
        "address": "Streamed online",
        "is_online": True,
        "meeting_url": "https://zoom.us/j/placeholder",
        "organizer": "Pydantic-Aura UK",
        "organizer_url": "https://pydantic-aura.uk",
        "speakers": [
            {
                "name": "Edward Bensa",
                "role": "Keynote: RAG",
                "avatar": "🎤",
                "bio": "Keynote speaker bio to be added."
            },{
                "name": "Amit Kumar",
                "role": "Keynote",
                "avatar": "🎤",
                "bio": "Keynote speaker bio to be added."
            }
        ],
        "agenda": [
            {"time": "09:00", "title": "Opening", "description": "Welcome and orientation."},
            {"time": "09:30", "title": "Keynote", "description": "State of AI/ML in 2026."},
            {"time": "10:30", "title": "Track 1: Retrieval & RAG", "description": "Talks on retrieval-augmented systems."},
            {"time": "13:00", "title": "Lunch Break", "description": "Asynchronous networking."},
            {"time": "14:00", "title": "Track 2: Agents", "description": "Building reliable agentic systems."},
            {"time": "16:00", "title": "Closing Panel", "description": "Open-weight models and the future."},
        ],
        "tags": ["AI", "Machine Learning", "Conference", "Online"],
        "capacity": 300,
        "registered_count": 7,
        "is_sold_out": False,
        "is_free": False,
        "price": "£25",
        "image_url": None,
        "registration_url": None,
        "prerequisites": [],
        "createdAt": "2025-11-05T10:00:00Z",
        "lastUpdated": "2025-11-20T12:00:00Z",
    },
]


def get_all_events():
    # resp = requests.get(f"{API_BASE}/events")

    data = {'events': listings}
    return data


def get_event_by_id(event_id: int):
    """Return a single event by id, or None if not found."""
    for event in listings:
        if event.get("id") == event_id:
            return event
    return None


if __name__ == "__main__":
    lst = get_all_events()
    print(f"All events: {lst}")
