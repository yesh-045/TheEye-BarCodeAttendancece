from sqlalchemy import Column, Integer, String, ForeignKey, Enum, DateTime
from sqlalchemy.orm import relationship
from datetime import datetime
from app.database.base import Base
from app.schemas.enums import RoleType

class Attendance(Base):
    __tablename__ = "attendance"

    id = Column(Integer, primary_key=True, index=True)
    roll_no = Column(String, ForeignKey("members.roll_no"))
    event_id = Column(Integer, ForeignKey("events.id"))
    role = Column(Enum(RoleType), default=RoleType.PARTICIPANT)
    timestamp = Column(DateTime, default=datetime.utcnow)

    # Relationships
    member = relationship("Member", back_populates="attendance_records")
    event = relationship("Event", back_populates="attendance_records")