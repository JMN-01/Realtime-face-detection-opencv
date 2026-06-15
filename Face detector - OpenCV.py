
# Facial detection system using OpenCV in Python
# pip install opencv-python to create a virtual environment and install the OpenCV library to run this code
import cv2

# This loads the pre-trained Haar Cascade classifier for face detection
# This file is included with OpenCV automatically
face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')

# This initializes the webcam (0 is usually the built-in Mac camera)
cap = cv2.VideoCapture(1)

print("Starting camera... Press 's' to quit and capture.")

while True:
    # This captures frame-by-frame
    ret, frame = cap.read()
    if not ret:
        break

    # This converts the frame to grayscale (Face detection works better/faster in gray)
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # This detects faces in the grayscale frame
    faces = face_cascade.detectMultiScale(
        gray, 
        scaleFactor=1.1, 
        minNeighbors=5, 
        minSize=(30, 30)
    )

    # This draws a rectangle around each detected face 
    for (x, y, w, h) in faces:
        cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 225, 0), 2)

    # This display the resulting frame
    cv2.imshow('AAI202 Face Detector', frame)

    # This is the exit route for the loop, when 's' is pressed it closes the webcam screen and releases the camera
    if cv2.waitKey(1) & 0xFF == ord('s'):
        break

# This releases the camera and closes the opencv windows
cap.release()
cv2.destroyAllWindows()