
from pydantic import BaseModel
from typing import List, Optional


# Add these models for the projects API
class ProjectContributor(BaseModel):
    name: str
    emoji: str | List[str]
    team_slug: str


class Project(BaseModel):
    id: int
    title: str
    slug: str
    description: str
    emoji: str
    status: str
    technologies: List[str]
    github_url: str
    demo_url: Optional[str] = None
    contributors: List[ProjectContributor]
    created_date: str
    last_updated: str


class ProjectsResponse(BaseModel):
    projects: List[Project]
    pagination: dict
