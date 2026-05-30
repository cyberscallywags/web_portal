from typing import Optional
from pydantic import BaseModel, Field


class Speaker(BaseModel):
    name: str = Field(..., description="Speaker name")
    role: Optional[str] = Field(None, description="Speaker role or title")
    avatar: Optional[str] = Field(None, description="Emoji or image URL representing the speaker")
    bio: Optional[str] = Field(None, description="Short speaker bio")


class AgendaItem(BaseModel):
    time: str = Field(..., description="Start time of the agenda item, e.g. '09:00'")
    title: str = Field(..., description="Title of the session")
    description: Optional[str] = Field(None, description="Short description of the session")


class Event(BaseModel):
    id: int = Field(..., description="The unique identifier for the event")
    name: str = Field(..., description="The name of the event")
    emoji: Optional[str] = Field(None, description="Display emoji for the event card/hero")
    event_type: Optional[str] = Field(None, description="Workshop, Talk, Conference, etc.")
    status: Optional[str] = Field("upcoming", description="upcoming | past | cancelled")
    description: str = Field(..., description="Short description of the event")
    long_description: Optional[str] = Field(None, description="Longer description shown on the detail page")
    date: str = Field(..., description="Event start datetime (ISO 8601)")
    end_date: Optional[str] = Field(None, description="Event end datetime (ISO 8601)")
    timezone: Optional[str] = Field(None, description="IANA timezone identifier")
    location: str = Field(..., description="Venue name or 'Online'")
    address: Optional[str] = Field(None, description="Full address or streaming note")
    is_online: bool = Field(False, description="Whether the event is virtual")
    meeting_url: Optional[str] = Field(None, description="URL for online events")
    organizer: str = Field(..., description="Event organizer")
    organizer_url: Optional[str] = Field(None, description="Organizer website")
    speakers: list[Speaker] = Field(default_factory=list, description="Speakers/presenters")
    agenda: list[AgendaItem] = Field(default_factory=list, description="Schedule of sessions")
    tags: list[str] = Field(default_factory=list, description="Topics/categories")
    capacity: Optional[int] = Field(None, description="Maximum attendees")
    registered_count: Optional[int] = Field(None, description="Currently registered attendees")
    is_sold_out: bool = Field(False, description="Whether registration is full")
    is_free: bool = Field(True, description="Whether the event is free")
    price: Optional[str] = Field(None, description="Display price if not free")
    image_url: Optional[str] = Field(None, description="Hero image URL")
    registration_url: Optional[str] = Field(None, description="External registration URL")
    prerequisites: list[str] = Field(default_factory=list, description="What attendees should bring/know")
    createdAt: str = Field(..., description="Created timestamp (ISO 8601)")
    lastUpdated: str = Field(..., description="Last updated timestamp (ISO 8601)")


class EventListing(BaseModel):
    events: list[Event] = Field(..., description="A list of events")
