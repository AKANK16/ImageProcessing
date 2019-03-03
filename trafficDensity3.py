import cv2
import numpy as np

 
cap = cv2.VideoCapture(0)

width = cap.get(cv2.CAP_PROP_FRAME_WIDTH)   # float
height = cap.get(cv2.CAP_PROP_FRAME_HEIGHT) # float
TP= width * height

while(True):
    # Capture frame-by-frame
    ret, frame = cap.read()
   

    
    # Our operations on the frame come here
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    ret,thresh = cv2.threshold(gray,80,255,0)

    white= TP - cv2.countNonZero(thresh)
    print("Dimensions:", frame.size, "Total pixels:", TP, "White", white)
    density=white/TP*100
    print(density)
    
        
     
        # Show keypoints
    cv2.imshow("Keypoints", gray)
    cv2.imshow("Keypoints", thresh)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
