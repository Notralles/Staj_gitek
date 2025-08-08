# -*- coding: utf-8 -*-
"""
Created on Thu Aug  7 14:09:25 2025

@author: krono
"""

import cv2
import numpy as np

img = np.zeros((512,512,3),np.int8)#3 renk uzayına sahip 



# cv2.line(img,(0,0),(511,511),(255,0,0),5)
# cv2.line(img,(250,260),(250,200),(255,255,0),5) #ÇİZGİLER

# cv2.rectangle(img,(50,50),(300,300),(0,231,123),5) 
# cv2.rectangle(img,(350,350),(511,511),(0,231,123),-1) #DİKDÖRTGENLER ,son parametreye -1 verirsek içi dolu olur

# cv2.circle(img,(255,255),60,(120,120,120),2)  
# cv2.circle(img,(100,100),90,(355,12,60),-1) #DAİRELER

# cv2.ellipse(img,(256,256),(100,50),0,0,180,(255,100,0),3)
# cv2.ellipse(img,(100,100),(100,50),0,0,180,(255,100,0),-1) #ELİPSLER

# pts = np.array([[20,30],[100,120],[255,255],[10,400]],np.int32)
# pts2 = pts.reshape(-1,1,2)

# cv2.polylines(img,[pts],True,(255,255,255),10) #ÇOKGEN 

font = cv2.FONT_HERSHEY_TRIPLEX
cv2.putText(img,'Selam',(10,100),font,4,(255,63,31),2,cv2.LINE_AA) #YAZI YAZMA




cv2.imshow("resim", img)
cv2.waitKey(0)
cv2.destroyAllWindows()
