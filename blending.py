import numpy as np
import os
import matplotlib.pyplot as plt
import cv2
import time

img_path1=os.path.join(os.getcwd(),"lena.tif")
image1=cv2.imread(img_path1)
img_path2=os.path.join(os.getcwd(),"mandril.tif")
image2=cv2.imread(img_path2)

for i  in np.linspace(0,1,50):
    alpha=i
    beta=1-alpha
    output=cv2.addWeighted(image1,alpha,image2,beta,0)
    cv2.imshow("transition",output)
    time.sleep(0.05)
    if cv2.waitKey(1)==27:
        break
    
cv2.destroyAllWindows()
