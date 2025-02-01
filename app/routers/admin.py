from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from typing import List
from datetime import timedelta
from app.database.session import get_db
from app.schemas.admin import AdminCreate, AdminResponse, AdminLogin, Token
from app.services.admin import AdminService
from app.services.auth import AuthService, ACCESS_TOKEN_EXPIRE_MINUTES
from app.models.admin import Admin
from app.schemas.event import EventCreate, EventUpdate, EventResponse
from app.schemas.member import MemberCreate, MemberResponse
from app.schemas.attendance import AttendanceStats
from app.services.event import EventService
from app.services.member import MemberService
from app.services.attendance import AttendanceService

router = APIRouter()

@router.post("/register", response_model=AdminResponse)
async def register_admin(
    admin_data: AdminCreate,
    db: Session = Depends(get_db),
    current_admin: Admin = Depends(AuthService.get_current_superuser)
):
    return AdminService.create_admin(db, admin_data)

@router.post("/login", response_model=Token)
async def login_admin(admin_data: AdminLogin, db: Session = Depends(get_db)):
    admin = AdminService.authenticate_admin(db, admin_data.email, admin_data.password)
    if not admin:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect email or password",
            headers={"WWW-Authenticate": "Bearer"},
        )
    
    access_token_expires = timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    access_token = AuthService.create_access_token(
        data={"sub": admin.email, "is_superuser": admin.is_superuser},
        expires_delta=access_token_expires
    )
    return {"access_token": access_token, "token_type": "bearer"}

@router.get("/me", response_model=AdminResponse)
async def read_admin_me(current_admin: Admin = Depends(AuthService.get_current_admin)):
    return current_admin

@router.get("/all", response_model=List[AdminResponse])
async def read_all_admins(
    skip: int = 0,
    limit: int = 100,
    db: Session = Depends(get_db),
    current_admin: Admin = Depends(AuthService.get_current_superuser)
):
    return AdminService.get_all_admins(db, skip, limit)

# Admin management endpoints
@router.post("/events/create", response_model=EventResponse)
async def create_event(
    event_data: EventCreate,
    db: Session = Depends(get_db),
    current_admin: Admin = Depends(AuthService.get_current_admin)
):
    return EventService.create_event(db, event_data)

@router.put("/events/{event_id}", response_model=EventResponse)
async def update_event(
    event_id: int,
    event_data: EventUpdate,
    db: Session = Depends(get_db),
    current_admin: Admin = Depends(AuthService.get_current_admin)
):
    return EventService.update_event(db, event_id, event_data)

@router.delete("/events/{event_id}")
async def delete_event(
    event_id: int,
    db: Session = Depends(get_db),
    current_admin: Admin = Depends(AuthService.get_current_admin)
):
    return EventService.delete_event(db, event_id)

@router.get("/attendance/stats", response_model=AttendanceStats)
async def get_attendance_stats(
    event_id: int = None,
    db: Session = Depends(get_db),
    current_admin: Admin = Depends(AuthService.get_current_admin)
):
    return AttendanceService.get_stats(db, event_id)

@router.post("/members/create", response_model=MemberResponse)
async def create_member(
    member_data: MemberCreate,
    db: Session = Depends(get_db),
    current_admin: Admin = Depends(AuthService.get_current_admin)
):
    return MemberService.create_member(db, member_data)

@router.delete("/members/{roll_no}")
async def delete_member(
    roll_no: str,
    db: Session = Depends(get_db),
    current_admin: Admin = Depends(AuthService.get_current_admin)
):
    return MemberService.delete_member(db, roll_no) 