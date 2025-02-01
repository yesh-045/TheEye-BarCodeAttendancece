from pydantic import BaseModel
from datetime import datetime, date
from app.schemas.enums import RoleType
from typing import Optional

class AttendanceBase(BaseModel):
    roll_no: str
    event_id: int
    role: RoleType = RoleType.PARTICIPANT

class AttendanceCreate(AttendanceBase):
    pass

class QRScanRequest(BaseModel):
    image_data: str
    event_id: int

class AttendanceResponse(AttendanceBase):
    id: int
    timestamp: datetime
    member_name: str
    event_name: str

    class Config:
        orm_mode = True

class AttendanceStats(BaseModel):
    total_attendance: int
    unique_members: int
    attendance_rate: float
    event_name: Optional[str] = None
    event_date: Optional[date] = None