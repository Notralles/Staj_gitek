# -*- coding: utf-8 -*-
"""
Created on Fri Aug  8 11:02:24 2025

@author: krono
"""
import cv2
import numpy as np
from matplotlib import pyplot as plt


#RESMİN ARKAPLANI BEYAZ OLDUĞU İÇİN BAZI ÇERÇEVELER TAM GÖZÜKMÜYOR BAŞKA RESİMLE DENEYEBİLİRSİNİZ!!



BLUE = [255,0,0]

img1 = cv2.imread("C:/ornekresim/CV2.png")

replicate = cv2.copyMakeBorder(img1, 10, 10, 10, 10, cv2.BORDER_REPLICATE)
reflect = cv2.copyMakeBorder(img1, 10, 10, 10, 10, cv2.BORDER_REFLECT)
reflect101 = cv2.copyMakeBorder(img1, 10, 10, 10, 10, cv2.BORDER_REFLECT_101)
wrap = cv2.copyMakeBorder(img1, 10, 10, 10, 10, cv2.BORDER_WRAP)
constant = cv2.copyMakeBorder(img1, 10, 10, 10, 10, cv2.BORDER_CONSTANT,value = BLUE)

plt.subplot(231),plt.imshow(img1,'gray'),plt.title('ORIGINAL')
plt.subplot(232),plt.imshow(replicate,'gray'),plt.title('REPLICATE')
plt.subplot(233),plt.imshow(reflect,'gray'),plt.title('REFLECT')
plt.subplot(234),plt.imshow(reflect101,'gray'),plt.title('REFLECT_101')
plt.subplot(235),plt.imshow(wrap,'gray'),plt.title('WRAP')
plt.subplot(236),plt.imshow(constant,'gray'),plt.title('CONSTANT')

plt.show



cv2.waitKey(1)



#ROI KISMI
# resim = cv2.imread("C:\\ornekresim\\RX7FC.jpg")

# kirp = resim[500:800,500:800]


# #resim[400:700,2200:2500] = kirp


# plt.subplot(121)
# plt.imshow(resim)
# plt.subplot(122)
# plt.imshow(kirp)
# plt.show




# cv2.waitKey(1)
