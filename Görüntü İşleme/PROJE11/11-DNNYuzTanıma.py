# -*- coding: utf-8 -*-
"""
Created on Mon Aug 11 11:02:29 2025

@author: krono
"""

import cv2
import numpy as np


prototxt_path = "C:/resderp/deploy.prototxt"
model_path = "C:/resderp/res10_300x300_ssd_iter_140000.caffemodel"
net = cv2.dnn.readNetFromCaffe(prototxt_path, model_path)


cap = cv2.VideoCapture(0)

while True:
    ret, frame = cap.read()
    if not ret:
        break

    
    (h, w) = frame.shape[:2]
    blob = cv2.dnn.blobFromImage(
        cv2.resize(frame, (300, 300)), 
        1.0, 
        (300, 300), 
        (104.0, 177.0, 123.0)  # Ortalama değerler  3. Girdi boyutu: 300x300
    )

    # 4. Ağa ver ve tahmin al
    net.setInput(blob)
    detections = net.forward()

    # 5. Sonuçları işle
    for i in range(0, detections.shape[2]):
        confidence = detections[0, 0, i, 2]  # Güven skoru

        if confidence > 0.5:  # %50 üstü algılamalar
            box = detections[0, 0, i, 3:7] * np.array([w, h, w, h])
            (startX, startY, endX, endY) = box.astype("int")

            # Dikdörtgen çiz
            text = f"{confidence*100:.1f}%"
            y = startY - 10 if startY - 10 > 10 else startY + 10
            cv2.rectangle(frame, (startX, startY), (endX, endY), (0, 255, 0), 2)
            cv2.putText(frame, text, (startX, y), 
                        cv2.FONT_HERSHEY_SIMPLEX, 0.45, (0, 255, 0), 2)


    cv2.imshow("DNN Yuz Tespiti", frame)

    if cv2.waitKey(1) & 0xFF == ord("q"):
        break

cap.release()
cv2.destroyAllWindows()
