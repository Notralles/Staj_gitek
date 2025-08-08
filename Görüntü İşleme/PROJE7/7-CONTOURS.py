# -*- coding: utf-8 -*-
"""
Created on Fri Aug  8 11:42:13 2025

@author: krono
"""
import os
import cv2
import numpy as np
import random


output_dir = "D:/ornekresim/konturlar"
random_thresh = 90     #TAM OLARAK BULAMADIĞI İÇİN HSV LİYE GEÇTİM 

img = cv2.imread("D:/ornekresim/tennisball.jpg") #GÖRÜNTÜYÜ OKUMA
cv2.imshow("ORIGINAL", img)

gri_top = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY) #GRAYSCALE
_, thresh_img = cv2.threshold(gri_top, random_thresh, 255, cv2.THRESH_BINARY)#THRESHOLD

konturlar,_ = cv2.findContours(thresh_img, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
cv2.drawContours(img, konturlar, -1, (0,255,0),2)


cv2.imshow("THRESHOLD {random_thresh}", thresh_img)
cv2.imshow("GRAYSCALE",gri_top)
cv2.imshow("KONTURLU", img)

for i, contour in enumerate(konturlar):
    x, y, w, h = cv2.boundingRect(contour)  # Konturun etrafına dikdörtgen
    crop = img[y:y+h, x:x+w]


    path = os.path.join(output_dir, f"parca_{i+1}.jpg")  # kayıt yolu
    cv2.imwrite(path, crop)
    print(f"{path} kaydedildi.")







cv2.waitKey(0)
cv2.destroyAllWindows()