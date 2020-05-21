import cv2
import os
import numpy as np

img_path = os.path.join(os.getcwd(), 'lena.tif')  #print(img_path)
image = cv2.imread(img_path,1)

cv2.imshow("Original", image)

M = np.float32([[1, 0, 25], [0, 1, 50]])
shifted = cv2.warpAffine(image, M, (image.shape[1], image.shape [0]))
cv2.imshow("Shifted Down and Right", shifted)

M = np.float32([[1, 0, -50], [0, 1, -90]])
shifted = cv2.warpAffine(image, M, (image.shape[1], image.shape [0]))
cv2.imshow("Shifted Up and Left", shifted)

(h,w)=image.shape[:2]
center=(w/2,h/2)
M=cv2.getRotationMatrix2D(center,-90,0.2)
rotated=cv2.warpAffine(image,M,(w,h))
cv2.imshow("rotated by 45 degree",rotated)


r=1000.0/image.shape[1]
dim=(1000,int(image.shape[0]*r))
resized=cv2.resize(image,dim,interpolation=cv2.INTER_LINEAR)
cv2.imshow("resized image",resized)

flipped=cv2.flip(image,0)
cv2.imshow("flipped vertically",flipped)

cropped=image[0:200,40:500]
cv2.imshow("cropped image",cropped)

cv2.waitKey(0)
cv2.destroyAllWindows()
