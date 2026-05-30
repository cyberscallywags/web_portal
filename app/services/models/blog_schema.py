from typing import Optional
from pydantic import BaseModel, Field


class Author(BaseModel):
    name: str = Field(..., description="Author's display name")
    avatar: Optional[str] = Field(None, description="Path or URL to the author's avatar image")
    bio: Optional[str] = Field(None, description="Short author bio")
    role: Optional[str] = Field(None, description="Author role / title")
    team_slug: Optional[str] = Field(None, description="Slug linking to the team page profile")


class RelatedPost(BaseModel):
    title: str = Field(..., description="Title of the related post")
    slug: str = Field(..., description="Slug for the related post URL")
    excerpt: Optional[str] = Field(None, description="Short excerpt")
    read_time: Optional[str] = Field(None, description="Estimated reading time, e.g. '5 min read'")
    emoji: Optional[str] = Field(None, description="Display emoji for the related post card")


class Blog(BaseModel):
    id: int = Field(..., description="Unique identifier for the blog post")
    title: str = Field(..., description="Post title")
    slug: str = Field(..., description="URL-safe slug")
    excerpt: str = Field(..., description="Short excerpt shown on listings and at the top of the post")
    content: str = Field(..., description="Full HTML content of the post")
    author: Author = Field(..., description="Post author")
    published_date: str = Field(..., description="Publication datetime (ISO 8601)")
    last_updated: Optional[str] = Field(None, description="Last updated datetime (ISO 8601)")
    featured_image: Optional[str] = Field(None, description="Hero image URL")
    emoji: Optional[str] = Field(None, description="Fallback emoji shown when no image is available")
    tags: list[str] = Field(default_factory=list, description="Topic tags")
    category: Optional[str] = Field(None, description="Primary category for filtering")
    read_time: str = Field(..., description="Estimated reading time, e.g. '5 min read'")
    status: str = Field("published", description="published | draft | archived")
    views: int = Field(0, description="View count")
    likes: int = Field(0, description="Like count")
    featured: bool = Field(False, description="Whether the post should be featured")


class BlogListing(BaseModel):
    blogs: list[Blog]
