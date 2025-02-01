from sqlalchemy.orm import Session
from fastapi import HTTPException
from app.models.event import Event
from app.schemas.event import EventCreate, EventUpdate
from datetime import datetime

class EventService:
    @staticmethod
    def create_event(db: Session, event_data):
        db_event = Event(**event_data.dict())
        db.add(db_event)
        db.commit()
        db.refresh(db_event)
        return db_event

    @staticmethod
    def get_events(db: Session, skip: int = 0, limit: int = 100):
        return db.query(Event).offset(skip).limit(limit).all()

    @staticmethod
    def get_event(db: Session, event_id: int):
        event = db.query(Event).filter(Event.id == event_id).first()
        if not event:
            raise HTTPException(status_code=404, detail="Event not found")
        return event

    @staticmethod
    def update_event(db: Session, event_id: int, event_data: EventUpdate):
        event = EventService.get_event(db, event_id)
        
        update_data = event_data.dict(exclude_unset=True)
        for field, value in update_data.items():
            setattr(event, field, value)

        db.commit()
        db.refresh(event)
        return event

    @staticmethod
    def delete_event(db: Session, event_id: int):
        event = EventService.get_event(db, event_id)
        db.delete(event)
        db.commit()
        return {"message": "Event deleted successfully"}

    @staticmethod
    def get_active_events(db: Session):
        return db.query(Event).filter(Event.status == "active").all()

    @staticmethod
    def get_upcoming_events(db: Session):
        today = datetime.now().date()
        return db.query(Event).filter(
            Event.date >= today,
            Event.status == "upcoming"
        ).all()