from sqlalchemy import Column, Integer, DateTime, ForeignKey
from sqlalchemy.orm import relationship
from app.database.base import Base

class Attendance(Base):
    __tablename__ = "attendance"

    id = Column(Integer, primary_key=True, index=True)
    member_id = Column(Integer, ForeignKey("members.id"))
    event_id = Column(Integer, ForeignKey("events.id"))
    timestamp = Column(DateTime)

    member = relationship("Member", back_populates="attendance")
    event = relationship("Event", back_populates="attendance")