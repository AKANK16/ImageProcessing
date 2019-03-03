import cv2

min_contour_width=35
min_contour_height=35
matches = []


cap = cv2.VideoCapture(0)
while(True):
    # Capture frame-by-frame
    ret, frame = cap.read()

    # Our operations on the frame come here
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    ret,thresh = cv2.threshold(gray,127,255,0)
    im2, contours, hierarchy = cv2.findContours(thresh,cv2.RETR_TREE,cv2.CV_CHAIN_APPROX_TC89_L1)
##    im2, contours, hierarchy = cv2.findContours(thresh,cv2.RETR_TREE,cv2.CHAIN_APPROX_NONE)
    
     #filtering by with, height
    for (i, contour) in enumerate(contours):
        (x, y, w, h) = cv2.boundingRect(contour)
        contour_valid = (w >= min_contour_width) and (
            h >= min_contour_height)

        if not contour_valid:
            continue
        
        # getting center of the bounding box
        centroid = get_centroid(x, y, w, h)

        matches.append(((x, y, w, h), centroid))


    #centroid
    x1 = int(w / 2)
    y1 = int(h / 2)

    cx = x + x1
    cy = y + y1



 # Display the resulting frame
    cv2.imshow('frame',gray)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
