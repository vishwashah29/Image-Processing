import cv2
import numpy as np
import pytesseract
from PIL import Image

path="C:\\Users\\VISHWA\\Downloads\\openCV\\python\\allen.png"

img=cv2.imread(path)
img=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

kernel=np.ones((1,1),np.uint8)

img=cv2.dilate(img,kernel,iterations=1)
img=cv2.erode(img,kernel,iterations=1)

cv2.imwrite("C:\\Users\\VISHWA\\Downloads\\openCV\\python\\removednoise.png",img)
img = cv2.adaptiveThreshold(img, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 31, 2)
cv2.imwrite("C:\\Users\\VISHWA\\Downloads\\openCV\\python\\thresh.png",img)
result = pytesseract.image_to_string(Image.open("C:\\Users\\VISHWA\\Downloads\\openCV\\python\\thresh.png"))

print(result)