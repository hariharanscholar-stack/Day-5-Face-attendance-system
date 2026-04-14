import cv2
import pandas as pd
from datetime import datetime
import time

name = "Hari haran"

face_cascade = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")

cap = cv2.VideoCapture(0)

start_time = None
attendance_marked = False
message = "Place your face inside the box"

while True:
    ret, frame = cap.read()
    if not ret:
        break

    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray, 1.3, 5)

    h, w, _ = frame.shape

    
    box_x1, box_y1 = int(w * 0.1), int(h * 0.1)
    box_x2, box_y2 = int(w * 0.9), int(h * 0.9)


    corner_len = 40
    color = (255, 255, 255)  
    
    if len(faces) == 0:
        start_time = None
        message = "Align face inside the frame"
        attendance_marked = False 
    else:
        message = "Face detected"

    for (x, y, fw, fh) in faces:
        
        is_centered = x > box_x1 and y > box_y1 and x+fw < box_x2 and y+fh < box_y2

        if is_centered:
            if start_time is None:
                start_time = time.time()
            
            elapsed = time.time() - start_time
            
            if not attendance_marked:
                progress = min(elapsed / 0.5, 1.0) 
                color = (0, 255, 255) 
                message = "Marking Attendance..."
                
                
                bar_width = int((box_x2 - box_x1) * progress)
                cv2.rectangle(frame, (box_x1, box_y2 + 10), (box_x1 + bar_width, box_y2 + 20), (0, 255, 0), -1)

                if elapsed >= 0.5:
                    now = datetime.now()
                    date = now.strftime("%d-%m-%Y")
                    time_now = now.strftime("%H:%M:%S")

                    new_row = pd.DataFrame([[name, date, time_now]], columns=["Name", "Date", "Time"])
                    try:
                        df = pd.read_csv("attendance.csv")
                        df = pd.concat([df, new_row], ignore_index=True)
                    except:
                        df = new_row
                    df.to_csv("attendance.csv", index=False)
                    
                    attendance_marked = True
            else:
                color = (0, 255, 0) 
                message = "Attendance Marked Successfully!"
        else:
            start_time = None
            color = (0, 0, 255)
            message = "Move closer to center"


    cv2.line(frame, (box_x1, box_y1), (box_x1 + corner_len, box_y1), color, 4)
    cv2.line(frame, (box_x1, box_y1), (box_x1, box_y1 + corner_len), color, 4)
    cv2.line(frame, (box_x2, box_y1), (box_x2 - corner_len, box_y1), color, 4)
    cv2.line(frame, (box_x2, box_y1), (box_x2, box_y1 + corner_len), color, 4)
    cv2.line(frame, (box_x1, box_y2), (box_x1 + corner_len, box_y2), color, 4)
    cv2.line(frame, (box_x1, box_y2), (box_x1, box_y2 - corner_len), color, 4)
    cv2.line(frame, (box_x2, box_y2), (box_x2 - corner_len, box_y2), color, 4)
    cv2.line(frame, (box_x2, box_y2), (box_x2, box_y2 - corner_len), color, 4)

    
    cv2.rectangle(frame, (0, 0), (w, 60), (0, 0, 0), -1)
    cv2.putText(frame, "AI ATTENDANCE SYSTEM", (20, 40), cv2.FONT_HERSHEY_SIMPLEX, 0.8, (255, 255, 255), 2)
    cv2.putText(frame, message, (20, h - 30), cv2.FONT_HERSHEY_SIMPLEX, 0.7, color, 2)

    cv2.imshow("Face Attendance System", frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()