# -*- coding: utf-8 -*-
"""
Created on Thu Aug  7 12:07:32 2025

@author: krono
"""

import cv2
#import numpy as np
#sifir = np.zeros([300,300])
#bir = np.ones([300,300])
#cv2.namedWindow("sifir",cv2.WINDOW_NORMAL)
#cv2.namedWindow("bir",cv2.WINDOW_NORMAL)
#cv2.imshow("sifir",sifir)
#cv2.imshow("bir",bir)
#cv2.waitKey(0)
#cv2.destroyAllWindows()

#cam.get(1,2,3,....) ile kamera özelliklerine ulaşabiliyoruz 
cam = cv2.VideoCapture(0)

print(cam.get(3)) 
print(cam.get(4)) 

cam.set(3,320)  # kamera boyutunu değiştirme 3 ve 4. parametreler en ve boy
cam.set(4,240) 


if not cam.isOpened(): #kamera kontrol
    print("kamera tanınmadı")
    exit()
    
    

while True:
    ret, frame = cam.read()#ret t/f gönderiyo frame resim cerceve
    
    frame = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
    
    if not ret:
        print("kamera çekemiyor")
        break
    
    cv2.imshow("kamera",frame)
    
    if cv2.waitKey(1) & 0xFF == ord("q"):
        print("görüntü sonlandırıldı")
        break

cam.release()    
cv2.destroyAllWindows()       
