# -*- coding: utf-8 -*-
"""
Created on Fri Mar  1 07:17:20 2019

@author: User
"""
import cv2

fgbg = cv2.bgsegm.createBackgroundSubtractorMOG()

i=0
minArea=1

cap = cv2.VideoCapture()
while(True):
    # Capture frame-by-frame
    ret, frame = cap.read()


    fgmask=fgbg.apply(frame,None, 0.01)
   # fgmask=backsub.apply(frame,None, 0.01)
    #fgmask = backsub.apply(frame, None, 0.01)
    #erode=cv2.erode(frame,None,iterations=3)     #erosion to erase unwanted small contours

    print(fgmask)

    # Our operations on the frame come here
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)


 # Display the resulting frame
    cv2.imshow('frame',gray)
 #   cv2.imshow('mask',fgmask)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break


