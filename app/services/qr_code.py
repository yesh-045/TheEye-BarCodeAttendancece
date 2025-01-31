import cv2
import numpy as np
from pyzbar.pyzbar import decode
import base64

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
            
            # Decode QR codes
            decoded_objects = decode(frame)
            if decoded_objects:
                return decoded_objects[0].data.decode('utf-8')
            raise ValueError("No QR code detected")
        except Exception as e:
            raise ValueError(f"QR decoding error: {str(e)}")