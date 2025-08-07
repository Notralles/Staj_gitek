# -*- coding: utf-8 -*-
"""
Created on Thu Aug  7 11:09:25 2025

@author: krono
"""

import cv2 #cv2 kütüphanesini importlar.
from matplotlib import pyplot as plt

resim = cv2.imread("C:/ornekresim/AE86.jpeg") #resimi okuma kısmı "'dan sonra,0 koyarsak sb oluyor

cv2.namedWindow("resim",cv2.WINDOW_NORMAL)#yeni pencerede açabiliyorz boyutu değiştirebiliyrz.
cv2.imshow("resim",resim) #resimi gösterme
cv2.imshow("Resim Penceresi",resim)


plt.imshow(resim,cmap="gray")
plt.show()


k = cv2.waitKey(0) #bir tuşa basana kadar göster

if k == 27:
    print("ESC tuşuna basıldı!")   #cv2.waitKey k değişkeninide tutuyor!!

elif k ==ord("q"):
    print("q tuşuna basıldı ve resim kaydedildi")#direkt ord ile de yapabiliyoruz
    cv2.imwrite("AE86gri.jpg", resim)
    

cv2.destroyWindow("Resim Penceresi") #pencereyi kapatma