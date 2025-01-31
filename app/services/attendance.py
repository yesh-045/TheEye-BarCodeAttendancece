from datetime import datetime
from sqlalchemy.orm import Session
from app.models.attendance import Attendance
from app.models.event import Event

class AttendanceService:
    @staticmethod
    def create_attendance(db: Session, attendance_data):
        db_attendance = Attendance(
            **attendance_data.dict(),
            timestamp=datetime.now()
        )
        db.add(db_attendance)
        
        # Update event attendees count
        event = db.query(Event).filter(Event.id == attendance_data.event_id).first()
        if event:
            event.attendees += 1
            db.commit()
        
        db.commit()
        db.refresh(db_attendance)
        return db_attendance

    @staticmethod
    def get_recent_attendance(db: Session, limit: int = 10):
        return db.query(Attendance).order_by(Attendance.timestamp.desc()).limit(limit).all()