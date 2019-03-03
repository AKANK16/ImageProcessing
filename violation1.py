import cv2
import numpy as np

 
cap = cv2.VideoCapture(1)


fgbg = cv2.bgsegm.createBackgroundSubtractorMOG()

while(1):
    ret, frame = cap.read()
    fgmask = fgbg.apply(frame,None, 0.01)
    cv2.imshow('frame',fgmask)
    
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
    
cap.release()
cv2.destroyAllWindows()



