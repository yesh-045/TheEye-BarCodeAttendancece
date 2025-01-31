from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
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
        
        # Parse member and event IDs from decoded data
        try:
            member_id, event_id = map(int, decoded_data.split(','))
        except ValueError:
            raise HTTPException(status_code=400, detail="Invalid QR code format")
        
        # Create attendance record
        attendance_data = AttendanceCreate(
            member_id=member_id,
            event_id=event_id
        )
        
        return AttendanceService.create_attendance(db, attendance_data)
    
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))

# ... rest of the attendance routes ...