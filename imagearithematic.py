import cv2
import os
import numpy as np
import  argparse

#ap=argparse.ArgumentParser()
#ap.add_argument("-i","--image",required="True",help="path to an image")
#args=vars(ap.parse_args())
#imag=cv2.imread(args["image"])
#cv2.imshow("original image",imag)

img_path = os.path.join(os.getcwd(), 'lena.tif')  #print(img_path)
image = cv2.imread(img_path,1)

cv2.imshow("Original", image)

print ("max of 255: {}".format(str(cv2.add(np.uint8([200]), np.uint8 ([100])))))
print ("min of 0: {}".format(str(cv2.subtract(np.uint8([50]), np.uint8 ([100])))))
print ("wrap around: {} ".format(str(np.uint8([200]) + np.uint8([100]))))
print ("wrap around: {}".format(str(np.uint8([50]) - np.uint8([100]))))

M=np.ones(image.shape,np.uint8)*100
added=cv2.add(image,M)
cv2.imshow("Added",added)

M=np.ones(image.shape,np.uint8)*50
subtracted=cv2.subtract(image,M)
cv2.imshow("Subtracted",subtracted)

mask = np.zeros(image.shape[:2], np.uint8)

#TypeError: an integer is required (got type tuple)
#(cX, cY) = (np.float32(image.shape[1] / 2), np.float32(image.shape[0] / 2))
#cv2.rectangle(mask,np.float32((cX - 75, cY - 75)),np.float32((cX + 75 , cY + 75)), (255,255,255),-1)

cv2.rectangle(mask,(50,50),(300,300), (255,255,255),-1)
cv2.imshow("Mask", mask)
masked = cv2.bitwise_and(image, image, mask = mask)
cv2.imshow("Mask Applied to Image 1", masked)

mask2 = np.zeros(image.shape[:2], np.uint8)
cv2.circle(mask2,(258,258),150,(255,255,255),-1)
cv2.imshow("Mask2", mask2)
masked2 = cv2.bitwise_and(image, image, mask = mask2)
cv2.imshow("Mask Applied to Image 2", masked2)

cv2.waitKey(0)
cv2.destroyAllWindows()

(B,G,R)=cv2.split(image)
cv2.imshow("red",R)
cv2.imshow("green",G)
cv2.imshow("blue",B)

merged=cv2.merge([B,G,R])
cv2.imshow("merged",merged)


cv2.waitKey(0)
cv2.destroyAllWindows()
#
#zeros = np.zeros(image.shape[:2], dtype = "uint8")
#cv2.imshow("Red", cv2.merge([zeros, zeros, R]))
#cv2.imshow("Green", cv2.merge([zeros, G, zeros]))
#cv2.imshow("Blue", cv2.merge([B, zeros, zeros])) 

zeros=np.zeros(image.shape[:2],np.uint8)
cv2.imshow("red channel", cv2.merge([zeros,zeros,R]))
cv2.imshow("blue channel", cv2.merge([B,zeros,zeros])) 
cv2.imshow("green channel", cv2.merge([zeros,G,zeros])) 
cv2.waitKey(0)
cv2.destroyAllWindows()


#COLOR SPACES
gray=cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)
cv2.imshow("gray",gray)
HSV=cv2.cvtColor(image,cv2.COLOR_BGR2HSV)
cv2.imshow("HSV",HSV)
LAB=cv2.cvtColor(image,cv2.COLOR_BGR2LAB)
cv2.imshow("L*A*B",LAB)
cv2.waitKey(0)
cv2.destroyAllWindows()