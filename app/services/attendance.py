from datetime import datetime
from sqlalchemy.orm import Session
from sqlalchemy import and_
from app.models.attendance import Attendance
from app.models.event import Event
from app.models.member import Member
from fastapi import HTTPException
from typing import Optional
from app.schemas.attendance import AttendanceStats

class AttendanceService:
    @staticmethod
    def create_attendance(db: Session, attendance_data):
        # Check if member exists
        member = db.query(Member).filter(Member.roll_no == attendance_data.roll_no).first()
        if not member:
            raise HTTPException(status_code=404, detail="Member not found")

        # Check if event exists and is active
        event = db.query(Event).filter(Event.id == attendance_data.event_id).first()
        if not event:
            raise HTTPException(status_code=404, detail="Event not found")
        if event.status != "active":
            raise HTTPException(status_code=400, detail="Event is not active")

        # Check if attendance already exists
        existing_attendance = db.query(Attendance).filter(
            and_(
                Attendance.roll_no == attendance_data.roll_no,
                Attendance.event_id == attendance_data.event_id
            )
        ).first()
        if existing_attendance:
            raise HTTPException(status_code=400, detail="Attendance already marked")

        # Create attendance record
        db_attendance = Attendance(
            roll_no=attendance_data.roll_no,
            event_id=attendance_data.event_id,
            role=attendance_data.role,
            timestamp=datetime.utcnow()
        )
        db.add(db_attendance)
        
        # Update event attendance count
        event.attendance += 1
        
        # Update member attendance count and rate
        member.attendance += 1
        total_events = db.query(Event).filter(Event.status != "upcoming").count()
        if total_events > 0:
            member.attendance_rate = (member.attendance / total_events) * 100

        db.commit()
        db.refresh(db_attendance)
        return db_attendance

    @staticmethod
    def get_recent_attendance(db: Session, event_id: int = None, skip: int = 0, limit: int = 10):
        query = db.query(Attendance).order_by(Attendance.timestamp.desc())
        if event_id:
            query = query.filter(Attendance.event_id == event_id)
        return query.offset(skip).limit(limit).all()

    @staticmethod
    def get_attendance_by_event(db: Session, event_id: int):
        return db.query(Attendance).filter(Attendance.event_id == event_id).all()

    @staticmethod
    def get_attendance_by_member(db: Session, roll_no: str):
        return db.query(Attendance).filter(Attendance.roll_no == roll_no).all()

    @staticmethod
    def get_stats(db: Session, event_id: Optional[int] = None):
        query = db.query(Attendance)
        if event_id:
            event = db.query(Event).filter(Event.id == event_id).first()
            if not event:
                raise HTTPException(status_code=404, detail="Event not found")
            
            query = query.filter(Attendance.event_id == event_id)
            total_attendance = query.count()
            unique_members = query.distinct(Attendance.roll_no).count()
            
            return AttendanceStats(
                total_attendance=total_attendance,
                unique_members=unique_members,
                attendance_rate=round((unique_members / total_attendance) * 100, 2) if total_attendance > 0 else 0,
                event_name=event.name,
                event_date=event.date
            )
        else:
            total_attendance = query.count()
            unique_members = query.distinct(Attendance.roll_no).count()
            total_events = db.query(Event).filter(Event.status != "upcoming").count()
            
            return AttendanceStats(
                total_attendance=total_attendance,
                unique_members=unique_members,
                attendance_rate=round((total_attendance / (total_events * unique_members)) * 100, 2) 
                if total_events > 0 and unique_members > 0 else 0
            )