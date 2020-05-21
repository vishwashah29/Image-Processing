import matplotlib.pyplot as plt
import os
import cv2


img_path = os.path.join(os.getcwd(), 'lena.tif')
img=cv2.imread(img_path,0)

plt.imshow(img,cmap='gray')
plt.title("gray scale image")
plt.xticks([])
plt.yticks([])
plt.show()

img1=cv2.imread(img_path,1)
plt.imshow(img1)
plt.title("color BGR image with default colormap")
plt.xticks([])
plt.yticks([])
plt.show()

img2=cv2.cvtColor(img1,cv2.COLOR_BGR2RGB)
plt.imshow(img2)
plt.title("color RGB image with default colormap")
plt.xticks([])
plt.yticks([])
plt.show()

j=0
for filename in dir(cv2):
    if filename.startswith("COLOR_"):
        print(filename)
        j=j+1
        
print("there are" + str((j+1)) +"color conversion flags in open cv")