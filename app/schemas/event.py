from pydantic import BaseModel
from datetime import date, time

class EventBase(BaseModel):
    name: str
    date: date
    time: time
    location: str
    category: str
    max_attendees: int
    status: str = "upcoming"

class EventCreate(EventBase):
    pass

class EventUpdate(EventBase):
    pass

class EventResponse(EventBase):
    id: int
    attendees: int

    class Config:
        orm_mode = True