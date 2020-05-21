import cv2
import numpy as np

def emptyfunc():
    pass

def main():
    canvas=np.zeros((512,512,3),dtype="uint8")
    image="BGR colour pallate and trackbar"
    cv2.namedWindow(image)
    
    cv2.createTrackbar('B',image,0,255,emptyfunc)
    cv2.createTrackbar('G',image,0,255,emptyfunc)
    cv2.createTrackbar('R',image,0,255,emptyfunc)
    
    
    while(True):
        cv2.imshow(image,canvas)
        
        if cv2.waitKey(1)==27: #if escape key is pressed program ends
            break
        
        blue=cv2.getTrackbarPos('B',image)
        green=cv2.getTrackbarPos('G',image)
        red=cv2.getTrackbarPos('R',image)
        
        canvas[:]=[blue,green,red]     #displays the canvas in BGR 

cv2.waitKey(0)
cv2.destroyAllWindows()  

    
if __name__=="__main__":
    main()