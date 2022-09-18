# Open CV
import cv2
import sys

cameraDeviceIndex = 0
if len(sys.argv) > 1:
    cameraDeviceIndex = sys.argv[1]

# Object of Video Capture for default index
source = cv2.VideoCapture(cameraDeviceIndex)

windowName = 'Camera Preview'
cv2.namedWindow(windowName, cv2.WINDOW_NORMAL)

# 27 is Escape, paused only when escape is pressed
while cv2.waitKey(1) != 27:
    hasFrame, frame = source.read()
    # if there is a problem in receiving video, hasFrame will be false
    if not hasFrame:
        break
    cv2.imshow(windowName, frame)

source.release()
cv2.destroyWindow(windowName)
