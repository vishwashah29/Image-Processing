import matplotlib.pyplot as plt
import cv2
import os
import numpy as np 

img_path = os.path.join(os.getcwd(), 'lena.tif') 
image=cv2.imread(img_path)
image2=cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)
cv2.imshow("Gray image",image2)

hist=cv2.calcHist([image2],[0],None,[256],[0,255])
plt.figure()
plt.title("grayscale histogram")
plt.xlabel("bins")
plt.ylabel("pixel in that bin")
plt.plot(hist)
plt.xlim([0,256])
plt.show()
cv2.waitKey(0)
cv2.destroyAllWindows()


cv2.imshow("coloured imafge",image)
chans=cv2.split(image)
colors=('b','g','r')
plt.figure()
plt.title("flattened colour histogram")
plt.xlabel("bins")
plt.ylabel("pixel in that bin")
for (chan,colour) in zip(chans,colors):
    hist=cv2.calcHist([chan],[0],None,[256],[0,255])
    plt.plot(hist,colour)
    plt.xlim([0,256])
plt.show()
cv2.waitKey(0)
cv2.destroyAllWindows()


# 2D histograms
fig2=plt.figure()
ax=fig2.add_subplot(131)
hist=cv2.calcHist([chans[0],chans[1]],[0,1],None,[32,32],[0,256,0,256])
p = ax.imshow(hist, interpolation = "nearest")
ax.set_title("2D Color Histogram for B and G")
plt.colorbar(p)

ax=fig2.add_subplot(132)
hist=cv2.calcHist([chans[1],chans[2]],[0,1],None,[32,32],[0,256,0,256])
p = ax.imshow(hist, interpolation = "nearest")
ax.set_title("2D Color Histogram for G and R")
plt.colorbar(p)

ax=fig2.add_subplot(133)
hist=cv2.calcHist([chans[0],chans[2]],[0,1],None,[32,32],[0,256,0,256])
p = ax.imshow(hist, interpolation = "nearest")
ax.set_title("2D Color Histogram for R and B")
plt.colorbar(p)

#fig3=plt.figure()
#hist = cv2.calcHist([image], [0, 1, 2],None, [8, 8, 8], [0, 256, 0, 256, 0, 256])
#print("3D histogram shape: {}, with {} values".format(hist.shape, hist.flatten().shape[0]))
#plt.show()


#cv2.waitKey(0)
#cv2.destroyAllWindows()

print("2D histogram shape: {}, with {} values".format(hist.shape, hist.flatten().shape[0]))



## Histogram equalization

img_path2 = os.path.join(os.getcwd(), 'lena.tif')
image3=cv2.imread(img_path2)
cv2.imshow("original",image3)
image4=cv2.cvtColor(image3,cv2.COLOR_BGR2GRAY)
cv2.imshow("grayscale image before equalization",image4)
eq=cv2.equalizeHist(image4)

cv2.imshow("Equalizing Histograms",np.hstack([image4,eq]))
#cv2.imshow("coloured imafge",image)

chans=cv2.split(image3)
colors=('b','g','r')
plt.figure()
plt.title("flattened colour histogram of original kashmir image")
plt.xlabel("bins")
plt.ylabel("pixel in that bin")
for (chan,colour) in zip(chans,colors):
    hist=cv2.calcHist([chan],[0],None,[256],[0,255])
    plt.plot(hist,colour)
    plt.xlim([0,256])
plt.show()
cv2.waitKey(0)
cv2.destroyAllWindows()


chans=cv2.split(eq)
colors=('b','g','r')
plt.figure()
plt.title("flattened colour histogram")
plt.xlabel("bins")
plt.ylabel("pixel in that bin")
for (chan,colour) in zip(chans,colors):
    hist=cv2.calcHist([chan],[0],None,[256],[0,255])
    plt.plot(hist,colour)
    plt.xlim([0,256])
plt.show()
cv2.waitKey(0)
cv2.destroyAllWindows()


###histogram with masks
def plot_histogram(image5,title,mask=None):
    chan=cv2.split(image5)
    color=('b','g','r')
    plt.figure()
    plt.title(title)
    plt.xlabel("bins")
    plt.ylabel("# of colors")
    for (chans,colors) in zip(chan,color):
        hist=cv2.calcHist([chans],[0],mask,[256],[0,256])
        plt.plot(hist,colors)
        plt.xlim([0,256])

mask = np.zeros(image.shape[:2], dtype = "uint8")
cv2.rectangle(mask, (15, 15), (130, 100), 255, -1)
cv2.imshow("Mask", mask)
masked = cv2.bitwise_and(image, image, mask = mask)
cv2.imshow("Applying the Mask", masked)
plot_histogram(masked, "Histogram for Masked Image", mask = mask)
plt.show()




