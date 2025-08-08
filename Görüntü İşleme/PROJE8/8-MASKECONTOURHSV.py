# -*- coding: utf-8 -*-
"""
Created on Fri Aug  8 13:01:25 2025

@author: krono
"""

import cv2
import os
import numpy as np



imgorg = cv2.imread("D:/ornekresim/tennisball.jpg")
img = cv2.imread("D:/ornekresim/tennisball.jpg")
hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV) #hsv ye çevirme hsv = hue saturation value

lower = np.array([20,100,100])
upper = np.array([70,255,255]) #opencv 180 e göre 2 ye bölüyoruz değerleri
mask = cv2.inRange(hsv, lower, upper)
#res = cv2.bitwise_and(img, img, mask=mask)

contours, _ = cv2.findContours(mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

save_path = "D:/ornekresim/konturlar1"


for i, contour in enumerate(contours):
    x, y, w, h = cv2.boundingRect(contour)

    boyut = max(w, h)
    x_centered = x + w // 2 - boyut // 2
    y_centered = y + h // 2 - boyut // 2

    x_start = max(0, x_centered)
    y_start = max(0, y_centered)
    x_end = min(img.shape[1], x_start + boyut)
    y_end = min(img.shape[0], y_start + boyut)


    cv2.rectangle(img, (x_start, y_start), (x_end, y_end), (0, 255, 0), 2)

    
    crop = img[y_start:y_end, x_start:x_end]
    filename = os.path.join(save_path, f"contour_{i+1}.jpg")
    cv2.imwrite(filename, crop)
    print(f"{filename} kaydedildi.")
    
cv2.imshow("orjinal", imgorg)
cv2.imshow("konturlu",img) #KONTURLU
cv2.imshow("hsv",hsv) #HSV RENKLER FORMATI RESİ
cv2.imshow("mask", mask)
#cv2.imshow("res",res)


cv2.waitKey(0)
cv2.destroyAllWindows()
