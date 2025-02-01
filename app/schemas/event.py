from pydantic import BaseModel
from datetime import date, time
from typing import Optional

class EventBase(BaseModel):
    name: str
    date: date
    location: str
    time: Optional[time]
    status: str = "upcoming"

class EventCreate(EventBase):
    pass

class EventUpdate(BaseModel):
    name: Optional[str] = None
    date: Optional[date] = None
    location: Optional[str] = None
    time: Optional[time] = None
    status: Optional[str] = None

class EventResponse(EventBase):
    id: int
    attendance: int

    class Config:
        orm_mode = True