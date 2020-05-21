# -*- coding: utf-8 -*-
"""
Created on Mon Jun 17 15:53:38 2019

@author: VISHWA
"""

import cv2
#print(cv2.__version__)
import os
import argparse


#img_path = os.path.join(os.getcwd(), 'lena.tif')
##print(img_path)
#img = cv2.imread(img_path,1)
##
#print(img)
#print(type(img))
#print(img.shape)
#print(img.dtype)
#print(img.ndim)
#
#outpath="C:\\Users\\VISHWA\\Downloads\\openCV\\python\\output\\lena.jpg"
#imgpath="C:\\Users\\VISHWA\\Downloads\\openCV\standard_test_images\\lena_color_512.jpeg"
#img=cv2.imread('C:\\Users\\VISHWA\\Desktop\\lena.jpg')


#while(cap.isOpened()):
#
#    ret, img = cap.read()
#    print (img)
#    if img==None:   #termino los frames?
#        break   #si, entonces terminar programa
#    #gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
#    
#cv2.namedWindow('image',cv2.WINDOW_AUTOSIZE)
#cv2.imshow("image",img)
#cv2.imwrite(outpath,img)
#cv2.waitKey(0)
#cv2.destroyWindow('image')



 
 ap = argparse.ArgumentParser() 
 ap.add_argument("-i","--image", required = True,  help = "Path to the image")
 args = vars(ap.parse_args())
 
 image = cv2.imread(args["image"]) 
 print ("width: %d pixels {}".format(image.shape[1]) )
 print( "height: %d pixels {}".format(image.shape[0]))
 print ("channels: %d {}".format(image.shape[2]))

(b,g,r)=img[0,0]
print("the image colour value: red{}, blue{} , green{}" . format(r,b,g))


cv2.imshow(" original Image", img) 
cv2.waitKey(0)

img[0:100,0:50]=(255,255,255)
print("the image colour value: red{}, blue{} , green{}" . format(r,b,g))


cv2.imshow(" modified Image", img) 
cv2.waitKey(0)

cv2.destroyAllWindows()  
