import cv2
import face_recognition
import os
import numpy as np

known_encodings = []
known_names = []

path = "known_faces"
for filename in os.listdir(path):
    img = face_recognition.load_image_file(os.path.join(path, filename))
    enc = face_recognition.face_encodings(img)
    if len(enc) > 0:
        known_encodings.append(enc[0])
        known_names.append(os.path.splitext(filename)[0])

face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + "haarcascade_frontalface_default.xml")

video = cv2.VideoCapture(0)

while True:
    ret, frame = video.read()
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray, 1.2, 5)

    rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    encodings = face_recognition.face_encodings(rgb_frame)

    for (x, y, w, h), encoding in zip(faces, encodings):
        matches = face_recognition.compare_faces(known_encodings, encoding)
        name = "Unknown"
        if True in matches:
            idx = matches.index(True)
            name = known_names[idx]
        cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 0), 2)
        cv2.putText(frame, name, (x, y-10), cv2.FONT_HERSHEY_SIMPLEX, 0.9, (0,255,0), 2)

    cv2.imshow("Face Detection & Recognition", frame)
    if cv2.waitKey(1) == ord('q'):
        break

video.release()
cv2.destroyAllWindows()
