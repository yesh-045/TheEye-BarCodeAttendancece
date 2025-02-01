from sqlalchemy.orm import Session
from fastapi import HTTPException
from app.models.member import Member
from app.schemas.member import MemberCreate

class MemberService:
    @staticmethod
    def create_member(db: Session, member_data: MemberCreate):
        # Check if member already exists
        if db.query(Member).filter(Member.roll_no == member_data.roll_no).first():
            raise HTTPException(status_code=400, detail="Member already registered")
        
        db_member = Member(**member_data.dict())
        db.add(db_member)
        db.commit()
        db.refresh(db_member)
        return db_member

    @staticmethod
    def get_members(db: Session, skip: int = 0, limit: int = 100):
        return db.query(Member).offset(skip).limit(limit).all()

    @staticmethod
    def get_member(db: Session, roll_no: str):
        member = db.query(Member).filter(Member.roll_no == roll_no).first()
        if not member:
            raise HTTPException(status_code=404, detail="Member not found")
        return member

    @staticmethod
    def delete_member(db: Session, roll_no: str):
        member = MemberService.get_member(db, roll_no)
        db.delete(member)
        db.commit()
        return {"message": "Member deleted successfully"}

    @staticmethod
    def update_member_stats(db: Session, roll_no: str):
        member = MemberService.get_member(db, roll_no)
        total_events = db.query(Event).filter(Event.status != "upcoming").count()
        if total_events > 0:
            member.attendance_rate = (member.attendance / total_events) * 100
            db.commit()