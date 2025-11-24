import os
import logfire
import requests

API_BASE = os.getenv("API_BASE", "https://api.cyberscallywags.uk")

projects = [{
                "id": 1,
                "title": "Community Learning Platform",
                "slug": "community-learning-platform",
                "description": "An open-source platform for community-driven learning with interactive coding challenges, peer mentoring, and collaborative projects. Built to democratize access to quality programming education.",
                "emoji": "📚",
                "status": "active",
                "technologies": ["python", "graph", "web-dev"],
                "github_url": "https://github.com/cyberscallywags/learning-platform",
                "demo_url": "https://cyberscallywags.uk",
                "contributors": [
                    {
                        "name": "Colin Moore-Hill",
                        "emoji": ["🐍",  "🧠"],
                        "team_slug": "colin-moore-hill"
                    },
                    {
                        "name": "Kishion Layne",
                        "emoji": ["🧠"],
                        "team_slug": "kishion-layne"
                    }
                ],
                "created_date": "2025-01-15T00:00:00Z",
                "last_updated": "2025-10-28T14:30:00Z"
                },
                {
                    "id": 2,
                    "title": "AI Ethics Toolkit",
                    "slug": "ai-ethics-toolkit",
                    "description": "A comprehensive toolkit for evaluating and implementing ethical AI practices in community projects. Includes guidelines, checklists, and automated testing tools.",
                    "emoji": "🤖",
                    "status": "planned",
                    "technologies": ["python", "ai-ml", "data-science"],
                    "github_url": "https://github.com/cyberscallywags/ai-ethics-toolkit",
                    "demo_url": "https://ethics.cyberscallywags.uk",
                    "contributors": [
                    ],
                    "created_date": "",
                    "last_updated": ""
                },
                {
                    "id": 3,
                    "title": "The DSF Companion",
                    "slug": "dsf-companion",
                    "description": "A digital companion for individuals to connect with a wide array of resources, support, and the community in general.",
                    "emoji": "🦾",
                    "status": "active",
                    "technologies": ["python", "FastAPI", "Jinja2", "Neo4j", "Ionic"],
                    "github_url": "https://github.com/cyberscallywags/business-directory-api",
                    "demo_url": None,
                    "contributors": [
                        {
                            "name": "Colin Moore-Hill",
                            "emoji": ["🦾"],
                            "team_slug": "colin-moore-hill"
                        },
                        {
                            "name": "Dean Foulds",
                            "emoji": ["🎨"],
                            "team_slug": "dean-foulds"
                        },
                        {
                            "name": "Amit ",
                            "emoji": ["🎨"],
                            "team_slug": "amit-foulds"
                        },
                        {
                            "name": "Edward Bensa",
                            "emoji": ["🌐"],
                            "team_slug": "dean-foulds"
                        }
                    ],
                    "created_date": "2024-08-20T00:00:00Z",
                    "last_updated": "2025-02-14T16:45:00Z"
                }
            ]


def get_all_projects():
    """Fetch all projects.

    Returns:
        list: A list of all projects.
    """
    logfire.debug(f"TRIGGER: get_all_projects :: Fetching all projects")
    # resp = requests.get(f"{API_BASE}/projects")
    projectsList = projects
    # return resp.json()['projects']
    return projectsList


def get_projects_by_id(project_id: int = 1):
    """Fetch a project by its ID.

    Args:
        project_id (int, optional): The ID of the project to fetch. Defaults to 1.

    Returns:
        dict: The project with the specified ID, or None if not found.
        _type_: _description_
    """
    logfire.debug(f" Getting project by id :: {project_id}")
    # resp = requests.get(f"{API_BASE}/projects/{project_id}")
    projects = get_all_projects()
    for project in projects:
        if project['id'] == project_id:
            return project
    return None  # Return None if not found  
 

if __name__ == "__main__":

    lst = get_all_projects()
    print(f" A projects in a lst :: {lst}")

    lst = get_projects_by_id(project_id=1)
    print(f"\n A projects in a lst ref :: {lst}")



