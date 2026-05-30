import os

from app.services.models.vlog_schema import Vlog

API_BASE = os.getenv("API_BASE", "http://localhost:8000")

listings = [
    {
        "id": 1,
        "title": "DSF Companion — Where We Are Now",
        "slug": "dsf-companion-where-we-are-now",
        "excerpt": (
            "A walkthrough of the first year of the DSF Companion: what we shipped, what we "
            "scrapped, and what's coming next."
        ),
        "description": """
            <p>This vlog is a candid retrospective of the DSF Companion's first year. We cover the architectural decisions that aged well, the ones we'd undo, and the patterns we want to double down on.</p>

            <h3>What's Inside</h3>
            <ul>
              <li>Why we picked Neo4j as the memory layer.</li>
              <li>How the streaming UI evolved from Server-Sent Events to a hybrid approach.</li>
              <li>The reason we dropped a planned mobile build (for now).</li>
            </ul>

            <p>If you only watch one section, jump to the chapter on context engineering — it's the one that changed how we think about the whole product.</p>
        """,
        "creator": {
            "name": "Amit Kumar",
            "avatar": "/static/images/team/amit/pic.jpeg",
            "bio": "Project Lead",
            "role": "Project Lead",
            "channel_url": "https://youtube.com/@cyberscallywags",
            "team_slug": "amit-kumar",
        },
        "published_date": "2025-11-02T18:00:00Z",
        "last_updated": "2025-11-02T18:00:00Z",
        "thumbnail": "/static/images/logo/dsf_Companion_logo.png",
        "video_url": "https://www.youtube.com/watch?v=dQw4w9WgXcQ",
        "youtube_id": "dQw4w9WgXcQ",
        "emoji": "🦾",
        "duration": "18:42",
        "chapters": [],
        "tags": ["product", "ai", "retrospective", "dsf"],
        "category": "Project review",
        "status": "published",
        "views": 13,
        "likes": 2,
        "featured": True,
    },
    {
        "id": 2,
        "title": "Graphs Aren't Scary: A 10-Minute Intro",
        "slug": "graphs-arent-scary-intro",
        "excerpt": (
            "A friendly, jargon-light primer on graph databases — what they are, when to "
            "reach for one, and a tiny live demo with Neo4j."
        ),
        "description": """
            <p>If the words "node", "edge", and "Cypher" make your eyes glaze over, this one's for you. We strip away the jargon and walk through a tiny, real example you can run on your laptop in five minutes.</p>

            <h3>What You'll Learn</h3>
            <ul>
              <li>When a graph is the right tool — and when it really isn't.</li>
              <li>How to model a small social network in Cypher.</li>
              <li>Where to go next if you want to go deeper.</li>
            </ul>
        """,
        "creator": {
            "name": "Colin Moore-Hill",
            "avatar": "/static/images/team/colin/pic.jpeg",
            "bio": "Founder & Community Lead",
            "role": "Community Lead",
            "channel_url": "https://youtube.com/@cyberscallywags",
            "team_slug": "colin-moore-hill",
        },
        "published_date": "2025-09-12T16:00:00Z",
        "last_updated": "2025-09-12T16:00:00Z",
        "thumbnail": "/static/images/logo/logo.png",
        "video_url": "https://www.youtube.com/watch?v=dQw4w9WgXcQ",
        "youtube_id": "dQw4w9WgXcQ",
        "emoji": "🕸️",
        "duration": "10:08",
        "chapters": [],
        "tags": ["tutorials", "graphs", "neo4j", "education"],
        "category": "tutorials",
        "status": "published",
        "views": 2317,
        "likes": 104,
        "featured": True,
    },
]


def get_all_vlogs() -> dict:
    """Return all vlogs wrapped in the standard response shape."""
    return {"vlogs": listings}


def get_vlog_by_slug(slug: str):
    """Return a single vlog by slug, or None if not found."""
    for vlog in listings:
        if vlog.get("slug") == slug:
            return vlog
    return None


def get_related_vlogs(slug: str, limit: int = 3) -> list[dict]:
    """Return up to `limit` other vlogs, excluding the one with `slug`."""
    return [v for v in listings if v.get("slug") != slug][:limit]


if __name__ == "__main__":
    lst = get_all_vlogs()
    print(f"All vlogs :: {lst}")
