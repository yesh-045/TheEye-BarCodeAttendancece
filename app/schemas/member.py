from pydantic import BaseModel
from datetime import date

class MemberBase(BaseModel):
    name: str
    email: str
    join_date: date
    status: str = "active"

class MemberCreate(MemberBase):
    pass

class MemberResponse(MemberBase):
    id: int
    attendance_rate: float

    class Config:
        orm_mode = True