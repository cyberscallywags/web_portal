from pydantic import BaseModel
from contributor_schema import ContributorList
from datetime import date


class ProjectHeader(BaseModel):
    "id": int
    "logo": str
    "title": str
    "slug": str
    "description": str
    "emoji": str
    "status": str
    "technologies": list[str],
    "github_url": str
    "demo_url": str
    "contributors": ContributorList
    "created_date": date
    "last_updated": date

class ProjectDetails(BaseModel):
    "id": int
    "logoSqr": str,
    "title": str,
    "slug": str,
    "description": str,
    "emoji": str,
    "status": str,
    "technologies": list[str],
    "github_url": str,
    "demo_url": str,
    "contributors": ContributorList,
    "created_date": date,
    "last_updated": date

class ProjectDetails(BaseModel):
    "id": int
    "logoSqr": str,
    "title": str,
    "slug": str,
    "description": str,
    "emoji": str,
    "status": str,
    "technologies": list[str],
    "github_url": str,
    "demo_url": str,
    "contributors": ContributorList,
    "created_date": date,
    "last_updated": date

class ProjectDetails(BaseModel):
    "id": int
    "logoSqr": str,
    "title": str,
    "slug": str,
    "description": str,
    "emoji": str,
    "status": str,
    "technologies": list[str],
    "github_url": str,
    "demo_url": str,
    "contributors": ContributorList,
    "created_date": date,
    "last_updated": date
    "created_date": "2025-01-15",
    "last_updated": "2025-10-28",
    "release_date": date,
    "features": list[str],
    "future_plans": list[str],
    "installation": list[str]
},