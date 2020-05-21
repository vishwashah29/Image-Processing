import cv2
import  numpy as np
import os

img_path=os.path.join(os.getcwd(),"chocolates.jpg")
img=cv2.imread(img_path)
img=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
cv2.imshow("original image",img)

blurred=cv2.GaussianBlur(img,(11,11),0)
canny=cv2.Canny(blurred,35,150)
cv2.imshow("canny edge",canny)

(cnts,_)=cv2.findContours(canny.copy(),cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_SIMPLE)
print("I have ",(len(cnts)),"chocolates")

coins=img.copy()
cv2.drawContours(coins,cnts,-1,(0,255,0),2)
cv2.imshow("coins with counyour",coins)


for (i, c) in enumerate(cnts):
    (x, y, w, h) = cv2.boundingRect(c) 
    print( "Coin ", (i + 1))
    coin = img[y:y + h, x:x + w] 
    cv2.imshow("Coin", coin) 
    mask = np.zeros(img.shape[:2], dtype = "uint8")
    ((centerX, centerY), radius) = cv2.minEnclosingCircle(c)
    cv2.circle(mask, (int(centerX), int(centerY)), int(radius), 255, -1)
    mask = mask[y:y + h, x:x + w]
    cv2.imshow("Masked Coin", cv2.bitwise_and(coin, coin, mask = mask))

cv2.waitKey(0)
cv2.destroyAllWindows()
