import cv2
import numpy as np

 
cap = cv2.VideoCapture(1)

width = cap.get(cv2.CAP_PROP_FRAME_WIDTH)   # float
height = cap.get(cv2.CAP_PROP_FRAME_HEIGHT) # float
TP= width * height
print(height)
print(width)

kernel = np.ones((19,19),np.uint8)


while(True):
    # Capture frame-by-frame
    ret, frame = cap.read()
   

    
    # Our operations on the frame come here
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    ret,thresh = cv2.threshold(gray,80,255,0)
    closing = cv2.morphologyEx(thresh, cv2.MORPH_CLOSE, kernel)
    

    roads1 = thresh[282:450 ,200 :302]
    
    
    black=cv2.countNonZero(thresh)
    
    print(black)



        
     
    # Show keypoints
    #cv2.imshow("Keypoints", gray)
    cv2.imshow("Keypoints", thresh)
    cv2.imshow("cropped",roads1)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
