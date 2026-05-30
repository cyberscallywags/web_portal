

def get_newsletter_data() -> list[dict]:
    return [
        {
            "id": 1,
            "title": "CSW Newsletter — Happy New Year, Scallywags!",
            "slug": "csw-newsletter-20260101",
            "emoji": "🦾",
            "excerpt": "Wishing a happy New Year to all our fellow CyberScallywags. A look back at 2025 and what's lighting up our roadmap for the year ahead.",
            "content": """
                <p>Welcome to the very first Cyber Scallywags newsletter of 2026. Whether you found us through a workshop, a GitHub thread, or a friend who whispered <em>'these folks build with kindness'</em> — we're glad you're here.</p>

                <h3>2025 in review</h3>
                <p>Last year we ran 14 community workshops, shipped two open-source tools, and welcomed over 200 new members into the pack. Highlights:</p>
                <ul>
                  <li><strong>DSF Companion</strong> went from prototype to production, supporting 15+ community organisations across Wales.</li>
                  <li><strong>Python Code Nanny</strong> entered planning, with a curriculum sprint scheduled for Q1.</li>
                  <li>We hosted our first <strong>Data Mining Wales</strong> meet-up in Merthyr — and yes, the pasties were excellent.</li>
                </ul>

                <h3>What's on for 2026</h3>
                <p>We're focusing on three things this year: <strong>community ownership</strong>, <strong>practical learning</strong>, and <strong>open tooling</strong>. Expect more workshops, a redesigned mentoring track, and a few surprises we're not quite ready to announce.</p>

                <blockquote>Our code isn't just syntax — it's solidarity.</blockquote>

                <p>If there's a topic you'd like us to cover, or a project you'd like to collaborate on, hit reply. We read every message.</p>
            """,
            "tags": ["community", "year-in-review", "roadmap"],
            "author": {
                "name": "Colin Moore-Hill",
                "bio": "Community Lead & Full-stack Developer",
                "team_slug": "colin-moore-hill",
            },
            "featured_image": "images/logo/cyberscallywags.png",
            "published_date": "2026-01-01",
            "read_time": "5 min read",
            "views": 100,
            "status": "Active",
        },
        {
            "id": 2,
            "title": "Python Code Nanny — Curriculum in the Open",
            "slug": "python-code-nanny",
            "emoji": "👨‍🎓",
            "excerpt": "Behind the scenes of Python Code Nanny: how we're designing a beginner-friendly curriculum with peer mentoring and interactive challenges baked in.",
            "content": """
                <p>Python Code Nanny is our answer to a question we kept hearing: <em>'I want to learn to code, but every tutorial assumes I already know the basics.'</em></p>

                <h3>Designing for the absolute beginner</h3>
                <p>We're building the curriculum in public. Every lesson plan, every challenge, every rubric lives on GitHub — open to feedback, contributions, and forks.</p>

                <ul>
                  <li><strong>Challenge-first learning:</strong> small wins early, harder problems later.</li>
                  <li><strong>Peer mentoring:</strong> learners are paired with a buddy from week one.</li>
                  <li><strong>Plain-language explanations:</strong> no jargon walls, no gatekeeping.</li>
                </ul>

                <h3>How to get involved</h3>
                <p>If you've ever taught someone to code, written a tutorial, or just remember what it felt like to be stuck on your first <code>for</code> loop — we'd love your input. Drop into the GitHub repo or reply to this newsletter.</p>
            """,
            "tags": ["python", "education", "open-source"],
            "author": {
                "name": "Kishion Layne",
                "bio": "Curriculum Designer",
                "team_slug": "kishion-layne",
            },
            "featured_image": "images/logo/ppc_logo.png",
            "published_date": "2025-10-28",
            "read_time": "6 min read",
            "views": 78,
            "status": "Active",
        },
        {
            "id": 3,
            "title": "Data Mining Wales — Bringing Tech to the Valleys",
            "slug": "data-mining-wales",
            "emoji": "⛏️",
            "excerpt": "A community-driven project focused on data mining techniques and applications — and on bringing technology to the valleys of Wales.",
            "content": """
                <p>Data Mining Wales started with a simple observation: most of the UK's tech investment lands within the M25, and the valleys get the leftovers. We're trying to change that — one workshop, one dataset, one local collaboration at a time.</p>

                <h3>Why the valleys?</h3>
                <p>Because the talent is here. Because the questions worth asking — about industry, ecology, language, identity — are here. And because data tools should serve the communities they describe, not extract from them.</p>

                <h3>First projects</h3>
                <ul>
                  <li>Mapping community assets across Rhondda Cynon Taf.</li>
                  <li>Open datasets on Welsh-language usage online.</li>
                  <li>Workshops on practical analysis — pandas, SQL, and a healthy scepticism of dashboards.</li>
                </ul>

                <p>If you're based in Wales and curious about data, you're already in the room. Come say hello.</p>
            """,
            "tags": ["data-science", "wales", "community"],
            "author": {
                "name": "Colin Moore-Hill",
                "bio": "Community Lead & Full-stack Developer",
                "team_slug": "colin-moore-hill",
            },
            "featured_image": "images/logo/dataminingwales.png",
            "published_date": "2025-11-15",
            "read_time": "4 min read",
            "views": 52,
            "status": "Active",
        },
        {
            "id": 4,
            "title": "Cyber Scallywags Community — How We Work",
            "slug": "cyber-scallywags-community",
            "emoji": "🤝",
            "excerpt": "An open-source platform for community-driven learning and collaborative projects. Here's how the pack actually works day-to-day.",
            "content": """
                <p>People often ask how the Cyber Scallywags community is structured. The honest answer: lightly. We're a pack, not an org chart.</p>

                <h3>The principles</h3>
                <ul>
                  <li><strong>Show up, don't perform.</strong> Half-finished work shared early beats polished work shared late.</li>
                  <li><strong>Teach what you just learned.</strong> The best teachers are the people one step ahead.</li>
                  <li><strong>Default to open.</strong> If it can be a public repo, a public doc, or a public conversation — make it one.</li>
                </ul>

                <h3>Getting involved</h3>
                <p>You don't need permission to join in. Pick a project that interests you, lurk for a bit, then introduce yourself. We'll find you something to do.</p>
            """,
            "tags": ["community", "culture", "open-source"],
            "author": {
                "name": "Colin Moore-Hill",
                "bio": "Community Lead & Full-stack Developer",
                "team_slug": "colin-moore-hill",
            },
            "featured_image": "images/logo/cyberscallywags.png",
            "published_date": "2025-11-15",
            "read_time": "3 min read",
            "views": 64,
            "status": "Active",
        },
        {
            "id": 5,
            "title": "Practical Pythonista Club — Sharpening the Saw",
            "slug": "practical-pythonista-club",
            "emoji": "🐍",
            "excerpt": "A community-driven space for Python enthusiasts to collaborate, learn, and share knowledge through interactive challenges and projects.",
            "content": """
                <p>The Practical Pythonista Club is for people who already know enough Python to be dangerous, and want to get a bit more dangerous.</p>

                <h3>What we do</h3>
                <ul>
                  <li>Monthly challenges drawn from real-world problems — graph theory, ML pipelines, data cleaning gone wrong.</li>
                  <li>Show-and-tell sessions where members walk through code they're proud of (or stuck on).</li>
                  <li>Reading group on a rotating cast of Python internals topics.</li>
                </ul>

                <h3>This month</h3>
                <p>We're working through a network-analysis challenge using <code>networkx</code>. If that sounds fun, the repo is open and the Discord is warm.</p>
            """,
            "tags": ["python", "ai-ml", "data-science"],
            "author": {
                "name": "Colin Moore-Hill",
                "bio": "Community Lead & Full-stack Developer",
                "team_slug": "colin-moore-hill",
            },
            "featured_image": "images/logo/ppc_logo.png",
            "published_date": "2025-11-15",
            "read_time": "4 min read",
            "views": 41,
            "status": "Active",
        },
    ]


def get_all_newsletter_data() -> list[dict]:
    newsletter_data = get_newsletter_data()
    return newsletter_data


def get_newsletter_data_by_slug(req_slug: str = "cyber-scallywags-community") -> list[dict]:
    newsletter_data = get_newsletter_data()
    return [newsletter for newsletter in newsletter_data if newsletter["slug"] == req_slug]


if __name__ == "__main__":
    all_newsletters = get_all_newsletter_data()
    assert 5 == len(all_newsletters)

    specific_newsletter = get_newsletter_data_by_slug("python-code-nanny")
    assert 1 == len(specific_newsletter)
    assert specific_newsletter[0]["title"].startswith("Python Code Nanny")
    print("All tests passed.")
