import cv2
from pyzbar.pyzbar import decode
import numpy as np
import base64

def scan_qr_code():
    """
    Scan QR code using the default camera.
    Returns the decoded QR code data or None if no QR code found.
    """
    # Open the camera
    cap = cv2.VideoCapture(0)
    
    # Flag to ensure scanning only happens once
    qr_found = False
    result = None

    while not qr_found:
        # Read a frame from the camera
        ret, frame = cap.read()
        
        if not ret:
            print("Failed to grab frame")
            break

        # Decode QR codes in the frame
        decoded_objects = decode(frame)
        
        if decoded_objects:
            for obj in decoded_objects:
                # Convert bytes to string if needed
                result = obj.data.decode('utf-8') if isinstance(obj.data, bytes) else str(obj.data)
                
                # Draw a rectangle around the QR code
                points = obj.polygon
                if len(points) > 4:
                    hull = cv2.convexHull(np.array([point for point in points], dtype=np.float32))
                    cv2.polylines(frame, [hull], True, (0, 255, 0), 2)
                else:
                    cv2.polylines(frame, [np.array(points, dtype=np.int32)], True, (0, 255, 0), 2)
                
                # Add text to the frame
                cv2.putText(frame, result, (10, 50), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)
                
                qr_found = True
                break

    # Release the camera and close windows
    cap.release()
    
    return result