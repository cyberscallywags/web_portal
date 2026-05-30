from pydantic import BaseModel

class Contributor(BaseModel):
    id: int
    name: str
    emoji: str
    team_slug: str

class ContributorList(BaseModel):
    __root__: list[Contributor]

