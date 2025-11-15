
from pydantic import BaseModel


class Blog(BaseModel):
    id: int
    title: str
    slug: str
    excerpt: str
    content: str
    author: dict
    published_date: str
    featured_image: str
    tags: list[str]
    read_time: str
    status: str
    views: int
    featured: bool


class BlogListing(BaseModel):
    blogs: list[Blog]
