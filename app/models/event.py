from sqlalchemy import Column, Integer, String, Date, Time
from sqlalchemy.orm import relationship
from app.database.base import Base

class Event(Base):
    __tablename__ = "events"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)
    date = Column(Date)
    location = Column(String)
    time = Column(Time)
    status = Column(String, default="upcoming")
    attendance = Column(Integer, default=0)  