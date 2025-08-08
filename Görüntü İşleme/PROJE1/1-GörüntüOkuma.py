# -*- coding: utf-8 -*-
"""
Created on Thu Aug  7 11:09:25 2025

@author: krono
"""

import cv2 #cv2 kütüphanesini importlar.
from matplotlib import pyplot as plt
import os

resim = cv2.imread("C:/ornekresim/AE86.jpeg") #resimi okuma kısmı "'dan sonra,0 koyarsak sb oluyor
gri_resim = cv2.cvtColor(resim, cv2.COLOR_BGR2GRAY)
_, esiklenmis_resim = cv2.threshold(gri_resim, 127, 255, cv2.THRESH_BINARY)


cv2.imshow("Orijinal", resim)
cv2.imshow("Gri Tonlama", gri_resim)
cv2.imshow("Eşiklenmiş", esiklenmis_resim)

plt.imshow(gri_resim, cmap="gray")
plt.title("Matplotlib ile Gri")
plt.show()


cv2.namedWindow("resim",cv2.WINDOW_NORMAL)#yeni pencerede açabiliyorz boyutu değiştirebiliyrz.
cv2.imshow("resim",resim) #resimi gösterme
cv2.imshow("Resim Penceresi",resim)


# plt.imshow(resim,cmap="gray")
# plt.show()


k = cv2.waitKey(0) #bir tuşa basana kadar göster

if k == 27:
    print("ESC tuşuna basıldı!")   #cv2.waitKey k değişkeninide tutuyor!!

elif k ==ord("q"):
    print("q tuşuna basıldı ve resim kaydedildi")#direkt ord ile de yapabiliyoruz
    output_klasoru = "outputs"
    if not os.path.exists(output_klasoru):
        os.makedirs(output_klasoru)
        print(f"'{output_klasoru}' klasörü oluşturuldu.")
    cv2.imwrite(os.path.join(output_klasoru, "AE86_gri.jpg"), gri_resim)
    cv2.imwrite(os.path.join(output_klasoru, "AE86_esiklenmis.jpg"), esiklenmis_resim)
    print("Gri ve eşiklenmiş resimler 'outputs' klasörüne kaydedildi!")
    


cv2.destroyWindow("Resim Penceresi") #pencereyi kapatma
