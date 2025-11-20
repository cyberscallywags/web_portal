from pydantic import BaseModel, Field


class Event(BaseModel):
    id: int = Field(..., description="The unique identifier for the event")
    name: str = Field(..., description="The name of the event")
    date: str = Field(..., description="The date of the event")
    location: str = Field(..., description="The location of the event")
    description: str = Field(..., description="A brief description of the event")
    createdAt: str = Field(..., description="The date and time when the event was created")
    lastUpdated: str = Field(..., description="The date and time when the event was last updated")  
    organiser: str = Field(..., description="The organizer of the event")


class EventListing(BaseModel):
    events: list[Event] = Field(..., description="A list of events")
