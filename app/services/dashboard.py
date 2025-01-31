from sqlalchemy.orm import Session
from datetime import date, timedelta
from app.models import Event, Member, Attendance

class DashboardService:
    @staticmethod
    def get_stats(db: Session):
        today = date.today()
        month_ago = today - timedelta(days=30)
        
        return {
            "active_events": db.query(Event).filter(
                Event.date >= today,
                Event.status == "active"
            ).count(),
            "total_members": db.query(Member).count(),
            "todays_attendance": db.query(Attendance).filter(
                Attendance.timestamp >= today
            ).count(),
            "monthly_growth": DashboardService.calculate_growth(db, month_ago)
        }

    @staticmethod
    def calculate_growth(db: Session, start_date):
        # Implement growth calculation logic
        return 12.0  # Placeholder