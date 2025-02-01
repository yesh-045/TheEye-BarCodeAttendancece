from pydantic import BaseModel
from app.schemas.enums import RoleType

class MemberBase(BaseModel):
    name: str
    roll_no: str
    role: RoleType = RoleType.PARTICIPANT

class MemberCreate(MemberBase):
    pass

class MemberResponse(MemberBase):
    id: int
    attendance_rate: float
    attendance: int

    class Config:
        orm_mode = True