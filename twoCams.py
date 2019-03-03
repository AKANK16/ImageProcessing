
import threading
import cv2
import numpy as np



class camThread(threading.Thread):
    def __init__(self, previewName, camID):
        threading.Thread.__init__(self)
        self.previewName = previewName
        self.camID = camID
    def run(self):
        print("Starting " + self.previewName)
        camPreview(self.previewName, self.camID)

def camPreview(previewName, camID):

    semaphore =1
    cv2.namedWindow(previewName)
    cam = cv2.VideoCapture(camID)
    width = cam.get(cv2.CAP_PROP_FRAME_WIDTH)  # float
    height = cam.get(cv2.CAP_PROP_FRAME_HEIGHT)  # float
    TP = width * height
    print(height)
    print(width)
    kernel = np.ones((19, 19), np.uint8)

    if cam.isOpened():
        rval, frame = cam.read()
    else:
        rval = False

    while rval:

        # Our operations on the frame come here
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

        ret, thresh = cv2.threshold(gray, 100, 255, 0)
        #cv2.erosion = cv2.erode(thresh, kernel, iterations=10)

        roads1 = thresh[282:450, 200:302]

        black = cv2.countNonZero(thresh)

        #print(black)

        total = thresh.size
        veh_density = (total - black) / total
        print(veh_density)

        # cv2.imshow("Keypoints", gray)
        #cv2.imshow("Keypoints", thresh)
        cv2.imshow("cropped", roads1)

        #cv2.imshow(previewName, frame)
        rval, frame = cam.read()
        key = cv2.waitKey(20)
        if key == 27:  # exit on ESC
            break
    cv2.destroyWindow(previewName)

# Create threads as follows
thread1 = camThread("Camera 1", 0)
thread2 = camThread("Camera 2", 2)

thread1.start()
thread2.start()

print()
print("Active threads", threading.activeCount())