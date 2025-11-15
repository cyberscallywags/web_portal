

def get_vlog_data() -> list[dict]:
    return [
        {
            "id": 1,
            "logo": 'images/logo/dsf_Companion_logo.png',
            "title": "DSF Companion",
            "slug": "dsf-companion",
            "description": "A digital companion for individuals to connect with the resources, support, and community in general.",
            "emoji": "🦾",
            "status": "Active",
            "technologies": ["python", "FastAPI", "Jinja2", "TypeScript", "HTML", "SCSS", "Dockerfile", "JavaScript"],
            "github_url": "https://github.com/cyberscallywags/ai-ethics-toolkit",
            "demo_url": "https://dsf.cyberscallywags.uk",
            "contributors": [
                {
                    "name": "Colin Moore-Hill",
                    "emoji": "🌐",
                    "team_slug": "colin-moore-hill"
                },
                {
                    "name": "Dean Foulds",
                    "emoji": "🎨",
                    "team_slug": "dean-foulds"
                },
                {
                    "name": "Amit ",
                    "emoji": "🎨",
                    "team_slug": "dean-foulds"
                },
                {
                    "name": "Edward Bensa",
                    "emoji": "🎨",
                    "team_slug": "dean-foulds"
                }
            ],
            "created_date": "2024-08-20",
            "last_updated": "2025-02-14"
        }, {
            "id": 2,
            "logo": 'images/logo/dsf_Companion_logo.png',
            "title": "Python Code Nanny",
            "slug": "python-code-nanny",
            "description": "An open-source platform for community-driven learning with interactive coding challenges, peer mentoring, and collaborative projects. Built to democratize access to quality programming education.",
            "emoji": "👨‍🎓",
            "status": "Planned",
            "technologies": ["python", "web-dev"],
            "github_url": "https://github.com/cyberscallywags/learning-platform",
            "demo_url": "https://pcn.cyberscallywags.uk",
            "contributors": [
                {
                    "name": "Colin Moore-Hill",
                    "emoji": ["🐍", "👩‍💻","🧠"],
                    "team_slug": "colin-moore-hill"
                },
                {
                    "name": "Kishion Layne",
                    "emoji": ["🧠"],
                    "team_slug": "kishion-layne"
                }
            ],
            "created_date": "2025-01-15",
            "last_updated": "2025-10-28"
        },
        {
            "id": 3,
            "logo": 'images/logo/dsf_Companion_logo.png',
            "title": "Data Mining Wales",
            "slug": "data-mining-wales",
            "description": "A community-driven project focused on data mining techniques and applications. And to bring technology to the valleys of Wales.",
            "emoji": "⛏️",
            "status": "Planned",
            "technologies": ["python", "ai-ml", "data-science"],
            "github_url": "https://github.com/cyberscallywags/",
            "demo_url": "https://data-mining.uk",
            "contributors": [
            ],
            "created_date": "2025-03-01",
            "last_updated": "2025-11-15"
        }, {
            "id": 4,
            "logo": 'images/logo/dsf_Companion_logo.png',
            "title": "Cyber Scallywags Community",
            "slug": "cyber-scallywags-community",
            "description": "An open-source platform for community-driven learning with interactive coding challenges and collaborative projects. Built to democratize access to quality programming education and foster inclusive learning environments.",
            "emoji": "⛏️",
            "status": "Planned",
            "technologies": ["python", "ai-ml", "data-science"],
            "github_url": "https://github.com/cyberscallywags/",
            "contributors": [
            ],
            "created_date": "2025-03-01",
            "last_updated": "2025-11-15"
        }, {
            "id": 5,
            "logo": 'images/logo/dsf_Companion_logo.png',
            "title": "Practical Pythonista Club",
            "slug": "practical-pythonista-club",
            "description": "A community-driven platform for Python enthusiasts to collaborate, learn, and share knowledge through interactive coding challenges and projects.",
            "emoji": "🐍",
            "status": "Planned",
            "technologies": ["python", "AI", "ML", "data-science", "Graph &Network Theory"],
            "github_url": "https://github.com/cyberscallywags/",
            "contributors": [
            ],
            "created_date": "2025-03-01",
            "last_updated": "2025-11-15"
        }
    ]


def get_all_vlog_data() -> list[dict]:
    blog_data = get_vlog_data()
    return blog_data


def get_vlog_data_by_slug(req_slug: str = "cyber-scallywags-community") -> list[dict]:
    vlog_data = get_vlog_data()
    return [vlog for vlog in vlog_data if vlog["slug"] == req_slug]


if __name__ == "__main__":
    # For testing purposes
    all_vlogs = get_all_vlog_data()
    assert 5 == len(all_vlogs)

    specific_vlog = get_vlog_data_by_slug("python-code-nanny")
    assert 1 == len(specific_vlog)
    assert specific_vlog[0]["title"] == "Python Code Nanny"
    print("All tests passed.")