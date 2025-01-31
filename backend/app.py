from flask import Flask, request, jsonify, render_template
import cv2
import numpy as np
from pyzbar.pyzbar import decode
import base64
import re
import sqlite3

app = Flask(__name__)

# Database setup function
def init_db():
    conn = sqlite3.connect('attendance.db')
    cursor = conn.cursor()
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS attendance (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        roll_number TEXT UNIQUE NOT NULL
    )
    ''')
    conn.commit()
    conn.close()

# Validate the Roll Number format (2 numbers, 1 letter, 3 numbers)
def validate_roll_number(roll_number):
    pattern = r'^\d{2}[a-zA-Z]\d{3}$'
    return bool(re.match(pattern, roll_number))

# Store Roll Number in the Database
def store_roll_number(roll_number):
    conn = sqlite3.connect('attendance.db')
    cursor = conn.cursor()

    try:
        cursor.execute('INSERT INTO attendance (roll_number) VALUES (?)', (roll_number,))
        conn.commit()
    except sqlite3.IntegrityError:
        # If the roll number already exists, skip insertion
        print(f"Roll number {roll_number} already exists in the database.")
    
    conn.close()

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/process_frame', methods=['POST'])
def process_frame():
    """
    Receive a base64-encoded frame from the frontend,
    decode it, and process it for QR codes.
    """
    try:
        data = request.json['frame']
        # Decode the base64-encoded frame
        img_data = base64.b64decode(data.split(',')[1])
        nparr = np.frombuffer(img_data, np.uint8)
        frame = cv2.imdecode(nparr, cv2.IMREAD_COLOR)

        # Process frame with pyzbar
        decoded_objects = decode(frame)
        roll_numbers_detected = []

        for obj in decoded_objects:
            roll_number = obj.data.decode('utf-8')
            print(f"Scanned roll number: {roll_number}")

            # Validate the roll number format
            if validate_roll_number(roll_number):
                store_roll_number(roll_number)
                


            return jsonify({'status': 'success', 'qr_code': roll_number})
        else:
            return jsonify({'status': 'failure', 'message': 'No valid QR code detected'})
    
    except Exception as e:
        return jsonify({'error': str(e)})

if __name__ == "__main__":
    # Initialize database before running the application
    init_db()
    
    app.run(host="0.0.0.0", port=5000, debug=True)
