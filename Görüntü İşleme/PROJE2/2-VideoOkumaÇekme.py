# -*- coding: utf-8 -*-
"""
Created on Thu Aug  7 12:55:31 2025

@author: krono
"""
#VİDEO KAYDETME KAMERADAN
import cv2 



cam = cv2.VideoCapture(1)

fourrc = cv2.VideoWriter_fourcc(*'XVID')

out = cv2.VideoWriter("videoad.avi",fourrc,30.0,(640,480))

while cam.isOpened():
    
    ret, frame = cam.read()
    
    if not ret:
        print("görüntü yok")
        break
    
    out.write(frame)
    
    cv2.imshow("kamera",frame)
    
    if cv2.waitKey(1) == ord("q"):
        print("q tuşu ile çıktınız")
        break
    
cam.release()
out.release()
cv2.destroyAllWindows()



















# VİDEO OKUMA KISMI 
# cam = cv2.VideoCapture("video_yolu")

# while cam.isOpened():
#     ret,frame = cam.read()
    
#     if not ret:
#         print("görüntü yok")
#         break
    
#     cv2.imshow("görüntü",frame)
    
#     if cv2.waitKey(1) & 0xFF == ord("q"):
#         print("Video kapatıldı")
#         break

# cam.release()
# cv2.destroyAllWindows()    
