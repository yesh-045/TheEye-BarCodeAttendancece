import cv2
import numpy as np
from pyzbar.pyzbar import decode
import base64
from fastapi import HTTPException

class QRCodeService:
    @staticmethod
    def decode_qr(base64_image: str) -> str:
        try:
            # Remove the data URL prefix if present
            if base64_image.startswith('data:image'):
                base64_image = base64_image.split(',')[1]
            
            # Decode base64 image
            img_data = base64.b64decode(base64_image)
            nparr = np.frombuffer(img_data, np.uint8)
            frame = cv2.imdecode(nparr, cv2.IMREAD_COLOR)
            
            if frame is None:
                raise HTTPException(status_code=400, detail="Invalid image data")
            
            # Decode QR codes
            decoded_objects = decode(frame)
            if not decoded_objects:
                raise HTTPException(status_code=400, detail="No QR code detected")
            
            return decoded_objects[0].data.decode('utf-8')
        except base64.binascii.Error:
            raise HTTPException(status_code=400, detail="Invalid base64 image data")
        except Exception as e:
            raise HTTPException(status_code=500, detail=f"QR decoding error: {str(e)}")