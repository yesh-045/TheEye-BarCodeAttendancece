from pydantic import BaseModel

class DashboardStats(BaseModel):
    active_events: int
    total_members: int
    todays_attendance: int