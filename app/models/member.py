from sqlalchemy import Column, Integer, String, Float, Enum
from sqlalchemy.orm import relationship
from app.database.base import Base
from app.schemas.enums import RoleType

class Member(Base):
    __tablename__ = "members"

    roll_no = Column(Integer, primary_key=True, index=True,autoincrement=False)
    name = Column(String)
    attendance_rate = Column(Float, default=0.0)
    attendance = Column(Integer, default=0)  
    role = Column(Enum(RoleType), default=RoleType.PARTICIPANT)