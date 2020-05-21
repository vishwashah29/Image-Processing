
import cv2
import numpy as np


canvas = np.zeros((512,512,3),dtype="uint8")
#
#cv2.line(canvas,(0,0),(512,512),(0,0,225),2)
#cv2.imshow("canvas",canvas)
#cv2.waitKey(0)
#
#cv2.line(canvas,(0,512),(512,0),(0,225,0),2)
#cv2.imshow("canvas",canvas)
#cv2.waitKey(0)
#
#cv2.rectangle(canvas, (10, 10), (60, 60),(255,0,0)) 
#cv2.imshow("Canvas", canvas)
#cv2.waitKey(0)
#
#cv2.rectangle(canvas, (50, 200), (200, 225),(67,45,24), 5)
#cv2.imshow("Canvas", canvas)
#cv2.waitKey(0)
#
#cv2.rectangle(canvas, (200, 50), (225, 125),(78,172,172), -1) 
#cv2.imshow("Canvas", canvas)
#cv2.waitKey(0) 
#
#
#(centerX, centerY) = (canvas.shape[1] / 2, canvas.shape[0] / 2)
#white = (255, 255, 255)
#for r in range(0, 175, 25):
#    cv2.circle(canvas,(np.float32(centerX),np.float32(centerY)),r,white)
#cv2.imshow("Canvas", canvas)
#cv2.waitKey(0)


for i in range(0, 25):
    radius = np.random.randint(5, high = 200)
    color = np.random.randint(0, high = 256, size = (3,)).tolist ()
    pt = np.random.randint(0, high = 512, size = (2,))
    cv2.circle(canvas, tuple(pt), radius, color, -1)
cv2.imshow("Canvas", canvas)
cv2.waitKey(0)
cv2.destroyAllWindows()  