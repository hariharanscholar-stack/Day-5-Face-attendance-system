# 📸 AI Face-Based Attendance System

A real-time face detection–based attendance system that records user presence using computer vision and structured data logging.

This project demonstrates a complete pipeline combining detection, spatial validation, temporal consistency, and data persistence.

---

## 🚀 Overview
This system captures live video input, detects faces using a Haar Cascade classifier, and validates user presence before marking attendance.

Attendance is recorded only when the face is:
- Properly aligned within a defined region
- Stable for a fixed duration

This reduces noise, prevents false positives, and ensures reliable logging.

---

## 🧠 System Pipeline

1. **Frame Acquisition**
   - Capture real-time video using OpenCV

2. **Preprocessing**
   - Convert frames to grayscale for efficient computation

3. **Face Detection**
   - Detect faces using Haar Cascade classifier

4. **Spatial Validation**
   - Verify if the detected face lies fully within a predefined Region of Interest (ROI)

5. **Temporal Validation**
   - Ensure the face remains stable within the ROI for a threshold duration

6. **Data Persistence**
   - Store attendance (Name, Date, Time) using pandas in a CSV file

---

## ⚙️ Tech Stack
- Python  
- OpenCV  
- Pandas  
- Haar Cascade Classifier  

---

## 🎯 Features
- Real-time face detection  
- ROI-based alignment checking  
- Time-based validation to prevent false triggers  
- Automatic attendance logging (CSV)  
- Visual feedback (bounding box, progress bar, status messages)  

---

## 🎮 How It Works
- User positions face inside the on-screen frame  
- System detects and validates alignment  
- Timer ensures stability (anti-false trigger mechanism)  
- Attendance is marked automatically  
- Data is saved with timestamp  

---

## 📦 Installation
```bash
pip install opencv-python pandas
```

---

## ▶️ Run the Project
```bash
python main.py
```

---

## 📁 Output
- `attendance.csv` → Stores:
  - Name  
  - Date  
  - Time  

---

## 📌 Requirements
- Webcam  
- Python 3.8+  

---

## 🌟 Future Improvements
- Face recognition (multi-user identification)  
- Database integration (Firebase / SQL)  
- Anti-spoofing (liveness detection)  
- UI enhancements  

---

## 🤝 Contributing
Feel free to fork and improve this project.

---

## 📢 Note
This project focuses on detection + validation pipeline. It can be extended into a full biometric attendance system with identity recognition.

---

## 🚀 Tagline
> Touchless attendance using AI-powered face detection.
