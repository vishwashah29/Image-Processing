#import cv2
##
##windowname="live video"
##cv2.namedWindow(windowname)\
#def main():
#    cap=cv2.VideoCapture()
#
#    if cap.isOpened():
#        ret,frame=cap.read()
#    
#    else:
#        ret=False
#    
#    while ret:
#        ret,frame=cap.read()
#        cv2.imshow(frame)
#        if cv2.waitKey(1)==27:
#            break
#    
#    cv2.destroyAllWindows()
#    cap.release()
#
#if __name__ == "__main__":
#    main()
import cv2

def main():
    windowName = "Live Video Feed"
    cv2.namedWindow(windowName)
    output="C:\\Users\\VISHWA\\Downloads\\openCV\\python\\output\output.avi"
    cap = cv2.VideoCapture(0)
    
    codec=cv2.VideoWriter_fourcc('W','M','V','2')
    framerate=12
    resolution=(640,480)
    
    VideoFileWriter=cv2.VideoWriter(output,codec,framerate,resolution)
    
    if cap.isOpened():
        ret, frame = cap.read()
    else:
        ret = False
        
    print("width" +str(cap.get(3)))
    print("height" +str(cap.get(4)))
    
#    cap.set(3,720)
#    cap.set(4,720)
#    
#    print("weidth" +str(cap.get(3)))
#    print("heigght" +str(cap.get(4)))
    

    while ret:
    
        ret, frame = cap.read()
        frame=cv2.cvtColor(frame,cv2.COLOR_BGR2RGB)
        VideoFileWriter.write(frame)
        
        #output = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        
        #cv2.imshow("Gray", output)
        cv2.imshow(windowName, frame)
        if cv2.waitKey(1) == 27:
            break

    cv2.destroyAllWindows()  
    VideoFileWriter.release()

    cap.release()

if __name__ == "__main__":
    main()