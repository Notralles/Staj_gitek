# -*- coding: utf-8 -*-
"""
Created on Mon Aug 11 10:47:21 2025

@author: krono
"""

import cv2


face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + "haarcascade_frontalface_default.xml") #haarcascadeyükleme


cap = cv2.VideoCapture(0)  # 0 varsayılan kameradan görüntü al

while True:
    ret, frame = cap.read()
    if not ret:
        break


    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY) #grayscale

    # 4. Yüzleri tespit et
    faces = face_cascade.detectMultiScale(
        gray,
        scaleFactor=1.1,  # görüntü ölçekleme
        minNeighbors=5,   # algılama hassasiyeti
        minSize=(30, 30)  # minimum yüz boyutu
    )

    # 5. Yüzlerin etrafına dikdörtgen çiz
    for (x, y, w, h) in faces:
        cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 0), 2)


    cv2.imshow("Yuz Tespiti", frame)


    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
