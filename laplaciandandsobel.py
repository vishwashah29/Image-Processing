import cv2
import  numpy as np
import os

img_path=os.path.join(os.getcwd(),"lena.tif")
img=cv2.imread(img_path)
#cv2.imshow(img)
img=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
cv2.imshow("original image",img)

lap=cv2.Laplacian(img,cv2.CV_64F)
lap=np.uint8(np.absolute(lap))
cv2.imshow("laplacian",lap)

sobelx=cv2.Sobel(img,cv2.CV_64F,1,0)
sobely=cv2.Sobel(img,cv2.CV_64F,0,1)
sobelx=np.uint8(np.absolute(sobelx))
sobely=np.uint8(np.absolute(sobely))

sobel=np.bitwise_or(sobelx,sobely)

cv2.imshow("sobelx",sobelx)
cv2.imshow("sobely",sobely)
cv2.imshow("sobel combinedd",sobel)

#CANNY EDGE DETECTOR

blurred=cv2.GaussianBlur(img,(5,5),0)
cv2.imshow("gaussian  blur",blurred)

canny=cv2.Canny(blurred,35,150)
cv2.imshow("canny edge detector",canny)


cv2.waitKey(0)
cv2.destroyAllWindows()