from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List
from app.schemas.attendance import AttendanceCreate, AttendanceResponse, QRScanRequest
from app.services.attendance import AttendanceService
from app.services.qr_code import QRCodeService
from app.database.session import get_db

router = APIRouter()

@router.post("/scan", response_model=AttendanceResponse)
async def process_qr_scan(scan_data: QRScanRequest, db: Session = Depends(get_db)):
    try:
        # Decode QR code
        decoded_data = QRCodeService.decode_qr(scan_data.image_data)
        
        # Parse roll number from decoded data
        try:
            roll_no = decoded_data.strip()
        except ValueError:
            raise HTTPException(status_code=400, detail="Invalid QR code format")
        
        # Create attendance record
        attendance_data = AttendanceCreate(
            roll_no=roll_no,
            event_id=scan_data.event_id
        )
        
        return AttendanceService.create_attendance(db, attendance_data)
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@router.post("/manual", response_model=AttendanceResponse)
async def mark_manual_attendance(attendance_data: AttendanceCreate, db: Session = Depends(get_db)):
    try:
        return AttendanceService.create_attendance(db, attendance_data)
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))

@router.get("/recent", response_model=List[AttendanceResponse])
async def get_recent_attendance(
    event_id: int = None,
    skip: int = 0,
    limit: int = 10,
    db: Session = Depends(get_db)
):
    return AttendanceService.get_recent_attendance(db, event_id, skip, limit)

@router.get("/event/{event_id}", response_model=List[AttendanceResponse])
async def get_event_attendance(event_id: int, db: Session = Depends(get_db)):
    return AttendanceService.get_attendance_by_event(db, event_id)

@router.get("/member/{roll_no}", response_model=List[AttendanceResponse])
async def get_member_attendance(roll_no: str, db: Session = Depends(get_db)):
    return AttendanceService.get_attendance_by_member(db, roll_no)

# ... rest of the attendance routes ...