# 📸 AI Face-Based Attendance System (Real-Time)

A real-time face detection–based attendance system built using OpenCV that automatically records attendance using spatial and temporal validation.

> Control attendance without touch — powered by AI.

---

## 🚀 Overview

This project implements a lightweight computer vision pipeline to automate attendance marking using a webcam.

Unlike basic detection systems, this implementation ensures:
- Proper face alignment (spatial validation)
- Stability over time (temporal validation)
- Reliable logging (data persistence)

This reduces false positives and improves system robustness.

---

## 🧠 System Architecture

### 1. Frame Acquisition
- Capture real-time video stream using OpenCV

### 2. Preprocessing
- Convert frames to grayscale for computational efficiency

### 3. Face Detection
- Use Haar Cascade classifier to detect faces in each frame

### 4. Spatial Validation
- Check if the detected face bounding box lies fully inside a defined ROI (Region of Interest)

### 5. Temporal Validation
- Start a timer when face is aligned  
- Attendance is marked only if the face remains stable for a threshold duration

### 6. Data Persistence
- Store attendance using pandas  
- Log Name, Date, and Time into a CSV file (`attendance.csv`)

---

## ⚙️ Tech Stack

- Python  
- OpenCV  
- Pandas  
- Haar Cascade Classifier  

---

## 🎯 Key Features

- Real-time face detection  
- ROI-based alignment checking  
- Time-based validation (anti false trigger)  
- Automatic attendance logging  
- CSV-based structured data storage  
- Visual feedback:
  - Bounding box indicators  
  - Progress bar  
  - Dynamic system messages  

---

## 🎮 Workflow

1. Start webcam  
2. Align face inside the defined frame  
3. System validates position and stability  
4. Progress indicator confirms detection  
5. Attendance is automatically recorded  
6. Data is saved in CSV format  

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

`attendance.csv` will contain:

| Name | Date | Time |
|------|------|------|

---

## 📌 Requirements

- Webcam  
- Python 3.8+  

---

## 🧪 Design Considerations

- **Grayscale conversion** reduces computation cost  
- **Bounding box validation** ensures correct positioning  
- **Temporal thresholding** avoids noisy detections  
- **State flags** prevent duplicate attendance entries  

---

## 🌟 Future Improvements

- Face recognition (multi-user identification)  
- Liveness detection (anti-spoofing)  
- Database integration (Firebase / SQL)  
- Multi-face attendance support  

---

## 🤝 Contributing

Feel free to fork and extend this project.

---

## 🚀 Tagline

> A simple yet robust pipeline combining detection, validation, and data logging for real-world AI systems.
