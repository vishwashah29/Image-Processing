import cv2
import numpy as np

#def main():
#    events=[i for i in dir(cv2) if 'EVENT' in i ]
#    print(events)
#    
#if __name__=="__main__":
#    main()

img=np.zeros((512,512,3),np.uint8)
window="drawing shapes"
cv2.namedWindow(window)

def draw_shapes(event,x,y,flag,param):
    if event == cv2.EVENT_LBUTTONDOWN:
        cv2.circle(img,(x,y),30,(0,0,255),-1)
        
cv2.setMouseCallback(window,draw_shapes)

def main():
    
     events=[i for i in dir(cv2) if 'EVENT' in i ]
     print(events)
     while(True):
         cv2.imshow(window,img)
         if cv2.waitKey(20) == 27:
             break
             
     cv2.destroyAllWindows()
    
if __name__=="__main__":
    main()
        

#import cv2
#import numpy as np
#
## Create a black image and a window
#windowName = 'Drawing'
#img = np.zeros((512, 512, 3), np.uint8)
#cv2.namedWindow(windowName)
#
## mouse callback function
#def draw_circle(event, x, y, flags, param):
#    if event == cv2.EVENT_LBUTTONDBLCLK:
#        cv2.circle(img, (x, y), 40, (0, 255, 0), -1)
#    if event == cv2.EVENT_MBUTTONDOWN:
#        cv2.circle(img, (x, y), 20, (0, 0, 255), -1)
#    if event == cv2.EVENT_LBUTTONDOWN:
#        cv2.circle(img, (x, y), 30, (255, 0, ), -1)
#
## bind the callback function to window
#cv2.setMouseCallback(windowName, draw_circle)
#
#def main():
#    
#    while(True):
#        cv2.imshow(windowName, img)
#        if cv2.waitKey(20) == 27:
#            break
#        
#    cv2.destroyAllWindows()
#        
#if __name__ == "__main__":
#    main()