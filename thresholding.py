import numpy as np
import cv2
import os
import mahotas


img_path1=os.path.join(os.getcwd(),"lena.tif")
img=cv2.imread(img_path1)
img=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
blurred = cv2.GaussianBlur(img, (5, 5), 0)
cv2.imshow("Image", img)
cv2.imshow("Gaussian blur", blurred)

#SIMPLE THRESHHOLDING

(T, thresh) = cv2.threshold(blurred, 155, 255, cv2.THRESH_BINARY)
cv2.imshow("Threshold Binary", thresh)
(T, threshInv) = cv2.threshold(blurred, 155, 255, cv2.THRESH_BINARY_INV)
cv2.imshow("Threshold Binary Inverse", threshInv)
cv2.imshow("lena", cv2.bitwise_and(img, img, mask = threshInv))

#GAUSSIAN THRESHOLDING

thresh=cv2.adaptiveThreshold(blurred,255,cv2.ADAPTIVE_THRESH_MEAN_C,cv2.THRESH_BINARY_INV,11,4)
cv2.imshow("Thresh mean",thresh)

thresh=cv2.adaptiveThreshold(blurred,255,cv2.ADAPTIVE_THRESH_GAUSSIAN_C,cv2.THRESH_BINARY_INV,11,4)
#cv2.imshow("Thresh Gaussian",thresh)

#OTSU THRESHOLDING

T=mahotas.thresholding.otsu(blurred)
print("otsu threshold",(T))

thresh=img.copy()
thresh[thresh>T]=255
thresh[thresh<255]=0 
thresh = cv2.bitwise_not(thresh)
cv2.imshow("Otsu", thresh) 

T=mahotas.thresholding.rc(blurred)
print("Riddler Calvard threshold",(T))

thresh=img.copy()
thresh[thresh>T]=255
thresh[thresh<255]=0
thresh = cv2.bitwise_not(thresh)
cv2.imshow("Riddler Calvard threshold", thresh) 


cv2.waitKey(0) 
cv2.destroyAllWindows()