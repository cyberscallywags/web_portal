import os

import requests

from app.services.models.blog_schema import Blog

# API_BASE = os.getenv("API_BASE", "https://api.cyberscallywags.uk")
API_BASE = os.getenv("API_BASE", "http://localhost:8000")

listings = [
    {
        "id": 1,
        "title": "Building Communities Through Code: The Cyber Scallywags Way",
        "slug": "building-communities-through-code",
        "excerpt": (
            "Discover how we're using technology to bring people together and create lasting "
            "change in our communities. From workshops to open-source projects, learn about "
            "our grassroots approach to making technology accessible and meaningful for everyone."
        ),
        "content": """
            <p>In a world increasingly dominated by big tech and profit-driven algorithms, there's something revolutionary about choosing purpose over profit. At Cyber Scallywags, we believe that technology should serve communities, not control them.</p>

            <h3>The Genesis of Our Movement</h3>
            <p>Born in the neon shadows of forgotten steel towns and weather-worn seaside streets, Cyber Scallywags emerged from a simple but powerful idea: that technology can be a force for good when it's built by and for the people who use it.</p>

            <p>We're not your typical tech company. We're the dreamers and doers who live between the circuits — the coders, makers, and data-misfits who understand that behind every line of code is an opportunity to make someone's life better.</p>

            <h3>Community-Driven Development</h3>
            <p>Our approach to building technology is fundamentally different. Instead of starting with the technology and finding users, we start with the community and find solutions. This means:</p>

            <ul>
              <li><strong>Listening First:</strong> We spend time in communities, understanding real needs and challenges before we write a single line of code.</li>
              <li><strong>Inclusive Design:</strong> Our projects are built with accessibility and inclusion at their core, not as an afterthought.</li>
              <li><strong>Open by Default:</strong> Everything we build is open source, ensuring that communities can own and modify their tools.</li>
              <li><strong>Skills Sharing:</strong> We don't just build tools; we teach others to build them too.</li>
            </ul>

            <h3>Real Projects, Real Impact</h3>
            <p>Our community learning platform has helped over 500 people take their first steps into coding. Our local business directory API supports 15 community organisations across Wales. These aren't just numbers — they represent individuals whose lives have been touched by technology that truly serves them.</p>

            <h3>The Path Forward</h3>
            <p>We're not here to hack the system. We're here to rewrite it — together. Every workshop we run, every open-source project we release, and every collaboration we foster is a step toward a more equitable digital future.</p>

            <p>Join us in lighting up the digital night with ideas powered by kindness, not capital. Because our code isn't just syntax — it's solidarity.</p>
        """,
        "author": {
            "name": "Colin Moore-Hill",
            "avatar": "/static/images/team/colin/pic.jpeg",
            "bio": "Founder & Community Lead",
            "role": "Community Lead",
            "team_slug": "colin-moore-hill",
        },
        "published_date": "2025-10-25T10:00:00Z",
        "last_updated": "2025-10-25T10:00:00Z",
        "featured_image": "/static/images/logo/CyberScallywags.png",
        "emoji": "🌐",
        "tags": ["community", "technology", "civic-tech", "open-source"],
        "category": "community",
        "read_time": "5 min read",
        "status": "published",
        "views": 1250,
        "likes": 42,
        "featured": True,
    },
    {
        "id": 2,
        "title": "The DSF Companion: From Conversations to Connections",
        "slug": "the-dsf-companion",
        "excerpt": (
            "Explore the DSF Companion, a platform designed to foster meaningful conversations "
            "and connections within the data community."
        ),
        "content": """
            <p>The DSF Companion started as a hack-day idea and has grown into one of our flagship community tools. The premise is simple: most useful AI is just structured context wrapped around a sensible model.</p>

            <h3>Why a Companion, Not a Chatbot?</h3>
            <p>Chatbots are reactive. A companion remembers, anticipates, and stays in step with you across days, projects, and conversations. We deliberately designed DSF around long-running context rather than turn-by-turn answers.</p>

            <h3>Under the Hood</h3>
            <ul>
              <li><strong>Graph-backed memory</strong> for relationships between people, projects, and topics.</li>
              <li><strong>Streaming UI</strong> built on FastAPI and Jinja2 for low-latency interaction.</li>
              <li><strong>Pluggable models</strong> so the companion isn't locked to a single provider.</li>
            </ul>

            <h3>What's Next</h3>
            <p>We're rolling out shared workspaces, scheduled summaries, and a public read-only profile so contributors can show off the work they've shipped through the companion.</p>
        """,
        "author": {
            "name": "Kishion Layne",
            "avatar": "/static/images/team/kishion/pic.jpeg",
            "bio": "Python Developer & Educator",
            "role": "Engineering",
            "team_slug": "kishion-layne",
        },
        "published_date": "2025-10-20T14:30:00Z",
        "last_updated": "2025-10-22T09:00:00Z",
        "featured_image": "/static/images/logo/dsf_Companion_logo.png",
        "emoji": "🦾",
        "tags": ["tutorials", "python", "education", "ai"],
        "category": "education",
        "read_time": "8 min read",
        "status": "published",
        "views": 892,
        "likes": 31,
        "featured": False,
    },
    {
        "id": 3,
        "title": "Cyber Scallywags Hackathon 2026: Get ready to innovate!",
        "slug": "hackathon-2026-preview",
        "excerpt": (
            "It will be an incredible weekend! Our annual hackathon brings together 120+ "
            "developers, designers, and innovators. Watch out for the amazing projects and see "
            "who wins."
        ),
        "content": """
            <p>The Cyber Scallywags Hackathon is back for 2026, and we're going bigger and bolder than ever. Three days, four tracks, and one community pulling in the same direction.</p>

            <h3>The Tracks</h3>
            <ul>
              <li><strong>Civic Tech:</strong> Tools that solve real problems for real councils and community groups.</li>
              <li><strong>AI for Good:</strong> Responsible, transparent AI projects with public benefit at their core.</li>
              <li><strong>Graph &amp; Network:</strong> Anything graph-shaped — from social networks to supply chains.</li>
              <li><strong>Wildcard:</strong> Bring your weirdest, most ambitious idea. We'll find a mentor for it.</li>
            </ul>

            <h3>How to Take Part</h3>
            <p>Sign up solo or with a team. We'll match free agents with teams during opening night. Mentors and venue partners will be announced in the coming weeks — keep an eye on the events page.</p>

            <p>Whether you ship a prototype or a polished product, we want to see what the pack can build.</p>
        """,
        "author": {
            "name": "Fran Moore-Hill",
            "avatar": "/static/images/team/HairyCoo.jpeg",
            "bio": "Event Coordinator & UX Designer",
            "role": "Events",
            "team_slug": "fran-moore-hill",
        },
        "published_date": "2025-10-15T09:00:00Z",
        "last_updated": "2025-11-01T12:00:00Z",
        "featured_image": "/static/images/logo/pogo.png",
        "emoji": "🎉",
        "tags": ["events", "community", "innovation", "hackathon"],
        "category": "events",
        "read_time": "6 min read",
        "status": "published",
        "views": 2103,
        "likes": 88,
        "featured": True,
    },
    {
        "id": 4,
        "title": "Working Group, Holborn — Day in the Life",
        "slug": "working-group-holborn-day-in-the-life",
        "excerpt": (
            "Behind the scenes of our first in-person Working Group at UnCommon Holborn. "
            "Hacking, mentoring, and a lot of coffee."
        ),
        "description": """
            <p>We brought a camera to our first in-person Working Group and edited it down into a tight, honest look at what a Cyber Scallywags day actually feels like.</p>

            <p>Expect pair programming, lightning talks, and the inevitable lunchtime debate about tabs vs. spaces. Subtitles available.</p>
        """,
        "author": {
            "name": "Kishion Layne",
            "avatar": "/static/images/team/kishion/pic.jpeg",
            "bio": "Strategy & Operations",
            "role": "CEO",
            "team_slug": "kishion-layne",
        },
        "published_date": "2025-10-08T12:00:00Z",
        "last_updated": "2025-10-08T12:00:00Z",
        "featured_image": "/static/images/logo/CyberScallywags.png",
        "emoji": "🎬",
        "tags": ["events", "community", "behind-the-scenes"],
        "category": "events",
        "read_time": "6 min read",
        "status": "published",
        "views": 482,
        "likes": 21,
        "featured": False,
    }
]


def get_all_blogs() -> dict:
    """Return all blogs wrapped in the standard response shape."""
    # resp = requests.get(f"{API_BASE}/blogs")
    return {"blogs": listings}


def get_blog_by_slug(slug: str):
    """Return a single blog post by slug, or None if not found."""
    for blog in listings:
        if blog.get("slug") == slug:
            return blog
    return None


def get_related_blogs(slug: str, limit: int = 3) -> list[dict]:
    """Return up to `limit` other blog posts, excluding the one with `slug`."""
    return [b for b in listings if b.get("slug") != slug][:limit]


if __name__ == "__main__":
    lst = get_all_blogs()
    print(f"All blogs :: {lst}")
