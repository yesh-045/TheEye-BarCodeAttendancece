from pydantic import BaseModel
from datetime import datetime

class AttendanceBase(BaseModel):
    member_id: int
    event_id: int

class AttendanceCreate(AttendanceBase):
    pass

class AttendanceResponse(AttendanceBase):
    id: int
    timestamp: datetime

    class Config:
        orm_mode = True

class QRScanRequest(BaseModel):
    image_data: str  # Base64 encoded image data