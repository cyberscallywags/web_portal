from typing import Optional
from pydantic import BaseModel, Field


class Creator(BaseModel):
    name: str = Field(..., description="Creator's display name")
    avatar: Optional[str] = Field(None, description="Path or URL to the creator's avatar image")
    bio: Optional[str] = Field(None, description="Short creator bio")
    role: Optional[str] = Field(None, description="Creator role / title")
    channel_url: Optional[str] = Field(None, description="Link to the creator's channel")
    team_slug: Optional[str] = Field(None, description="Slug linking to the team page profile")


class Chapter(BaseModel):
    timestamp: str = Field(..., description="Chapter start time, e.g. '00:00' or '12:34'")
    title: str = Field(..., description="Chapter title")
    description: Optional[str] = Field(None, description="Optional chapter description")


class RelatedVlog(BaseModel):
    title: str = Field(..., description="Title of the related vlog")
    slug: str = Field(..., description="Slug for the related vlog URL")
    excerpt: Optional[str] = Field(None, description="Short excerpt")
    duration: Optional[str] = Field(None, description="Video duration, e.g. '12:34'")
    thumbnail: Optional[str] = Field(None, description="Thumbnail image URL")
    emoji: Optional[str] = Field(None, description="Display emoji used as a fallback")


class Vlog(BaseModel):
    id: int = Field(..., description="Unique identifier for the vlog")
    title: str = Field(..., description="Vlog title")
    slug: str = Field(..., description="URL-safe slug")
    excerpt: str = Field(..., description="Short excerpt shown on listings and at the top of the page")
    description: str = Field(..., description="Full HTML description / show notes")
    creator: Creator = Field(..., description="Video creator")
    published_date: str = Field(..., description="Publication datetime (ISO 8601)")
    last_updated: Optional[str] = Field(None, description="Last updated datetime (ISO 8601)")
    thumbnail: Optional[str] = Field(None, description="Thumbnail image URL")
    video_url: Optional[str] = Field(None, description="Direct video URL or YouTube watch URL")
    youtube_id: Optional[str] = Field(None, description="YouTube video ID for embedding")
    emoji: Optional[str] = Field(None, description="Fallback emoji shown when no thumbnail is available")
    duration: str = Field(..., description="Video duration, e.g. '12:34'")
    chapters: list[Chapter] = Field(default_factory=list, description="Chapter / timestamp markers")
    tags: list[str] = Field(default_factory=list, description="Topic tags")
    category: Optional[str] = Field(None, description="Primary category for filtering")
    status: str = Field("published", description="published | draft | archived")
    views: int = Field(0, description="View count")
    likes: int = Field(0, description="Like count")
    featured: bool = Field(False, description="Whether the vlog should be featured")


class VlogListing(BaseModel):
    vlogs: list[Vlog]
