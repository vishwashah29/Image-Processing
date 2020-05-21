import cv2
import numpy as np

img=np.zeros((512,512,3),np.uint8)
window="drawing shapes"
cv2.namedWindow(window)

# true if mouse is pressed
drawing="False"

#if true then draw a rectangle. mode changes when you press m key on the keyboard
mode="True"
(ix,iy)=(-1,-1)

def draw_shapes(event,x,y,flag,pram):
    global ix,iy,drawing,mode
    
    if event == cv2.EVENT_LBUTTONDOWN:
        drawing = True
        (ix, iy) = x,y

    elif event == cv2.EVENT_MOUSEMOVE:
        if drawing == True:
            if mode == True:
                cv2.rectangle(img, (ix, iy), (x, y), (0, 255, 0), -1)
            else:
                cv2.circle(img, (x, y), 5, (0, 0, 255), -1)

    elif event == cv2.EVENT_LBUTTONUP:
        drawing = False
        if mode == True:
            cv2.rectangle(img, (ix, iy), (x, y), (255, 0 , 0), -1)
        else:
            cv2.circle(img, (x, y), 5, (0, 255, 255), -1)

cv2.setMouseCallback(window,draw_shapes)

def main():
    global mode
    
    while(True):
        cv2.imshow(window,img)
        
        k = cv2.waitKey(1)
        if k == ord('m') or k == ord('M'):
            mode = not mode
        elif k == 27:
                break

    cv2.destroyAllWindows()

if __name__ == "__main__":
    main()