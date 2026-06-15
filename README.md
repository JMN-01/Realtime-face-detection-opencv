# Real-Time Face Detection with OpenCV

## Overview
A `real-time` face detection application that utilizes OpenCV's Haar Cascade classifier alongside a webcam stream to dynamically identify and locate human faces

## Requirements
- Python 3
- OpenCV

## Setup & Installation

Follow these steps to clone the repository, install the necessary dependencies, and execute the live application on your machine:

1. Clone the repository** to download a full copy of the project files:

  ```sh
   git clone https://github.com/JMN-01/realtime-face-detection-opencv.git
   cd realtime-face-detection-opencv
```
2. Change your directory to step inside the projects root workspace folder:
   
```sh
 cd realtime-face-detection-opencv
```
3. Install dependencies using pip (ensure Python 3 is installed globally):

```sh
pip install opencv-python
```
4. Launch the application to initialize the webcam and begin real-time detection:

```sh
python face_detection_system.py
```
## Example


![Face Detection System Output Preview](Face%20detection%20system%20test%201.png)


## Code Explanation

```Python
# Pip install opencv-python and install the OpenCV library to run this code
import cv2
```

```Python
# This loads the pre-trained Haar Cascade classifier for face detection
# This file is included with OpenCV automatically
face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')
```

```Python
# This initializes the webcam (0 is usually the built-in Mac camera)
cap = cv2.VideoCapture(1)

print("Starting camera... Press 's' to quit and capture.")

while True:
```
```Python
 # This captures frame-by-frame
    ret, frame = cap.read()
    if not ret:
        break
```
```Python

# This converts the frame to grayscale (Face detection works better/faster in gray)
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
```

```Python
# This detects faces in the grayscale frame
    faces = face_cascade.detectMultiScale(
        gray, 
        scaleFactor=1.1, 
        minNeighbors=5, 
        minSize=(30, 30)
    )
```

```Python
 # This draws a rectangle around each detected face 
    for (x, y, w, h) in faces:
        cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 225, 0), 2)
```

```Python
  # This display the resulting frame
    cv2.imshow('AAI202 Face Detector', frame)
```

```Python
 # This is the exit route for the loop, when 's' is pressed it closes the webcam screen and releases the camera
    if cv2.waitKey(1) & 0xFF == ord('s'):
        break
```

```Python
# This releases the camera and closes the opencv windows
cap.release()
cv2.destroyAllWindows()
```


