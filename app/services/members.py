from sqlalchemy.orm import Session
from app.models.member import Member

class MemberService:
    @staticmethod
    def create_member(db: Session, member_data):
        db_member = Member(**member_data.dict())
        db.add(db_member)
        db.commit()
        db.refresh(db_member)
        return db_member

    @staticmethod
    def get_members(db: Session, skip: int = 0, limit: int = 100):
        return db.query(Member).offset(skip).limit(limit).all()

    @staticmethod
    def update_attendance_rate(db: Session, member_id: int):
        member = db.query(Member).filter(Member.id == member_id).first()
        if member:
            # Calculate attendance rate logic
            pass
        return member