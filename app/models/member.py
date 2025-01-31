from sqlalchemy import Column, Integer, String, Date, Float
from sqlalchemy.orm import relationship
from app.database.base import Base

class Member(Base):
    __tablename__ = "members"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)
    email = Column(String, unique=True, index=True)
    join_date = Column(Date)
    attendance_rate = Column(Float, default=0.0)
    status = Column(String, default="active")
    
    attendance = relationship("Attendance", back_populates="member")