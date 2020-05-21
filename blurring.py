import cv2
import os
import numpy as np

img_path=os.path.join(os.getcwd(),"me.jpeg")
image=cv2.imread(img_path)

image= cv2.resize(image,(512,512), interpolation = cv2.INTER_AREA)
cv2.imshow("original",image)
cv2.waitKey(0)
#cv2.destroyAllWindows()
 
#blurred = np.hstack([cv2.blur(image, (3, 3)),cv2.blur(image, (5, 5)),cv2.blur(image, (14,14))])
#cv2.imshow("Averaged", blurred)
#cv2.waitKey(0)




blurred = np.hstack([cv2.GaussianBlur(image, (3, 3),9),cv2.GaussianBlur(image, (5, 5),6),cv2.GaussianBlur(image, (5, 5),0)])
cv2.imshow("Gaussian", blurred)
cv2.waitKey(0)


#blurred=np.hstack([cv2.medianBlur(image,3),cv2.medianBlur(image,5),cv2.medianBlur(image,7)])
#cv2.imshow("median",blurred)
#cv2.waitKey(0)
#
#blurred=np.hstack([cv2.bilateralFilter(image,5,21,21),cv2.bilateralFilter(image,7,31,31),cv2.bilateralFilter(image,9,41,41)])
#cv2.imshow("billateral",blurred)
#cv2.waitKey(0)
#cv2.destroyAllWindows()
#
#cv2.imshow("me good",cv2.bilateralFilter(image,9,51,51))
#cv2.waitKey(0)
cv2.destroyAllWindows()