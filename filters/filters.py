import cv2
import sys

PREVIEW = 0  # Preview Mode
BLUR = 1  # Blurring Filter
EDGE = 2  # Edge Detector

feature_params = dict(maxCorners=500,
                      qualityLevel=0.2,
                      minDistance=15,
                      blockSize=9)

# Setting device index for camera
cameraDeviceIndex = 0
if len(sys.argv) > 1:
    cameraDeviceIndex = sys.argv[1]

imageFilter = PREVIEW
alive = True

# Create output window for screen results
windowName = 'Camera Filters'
cv2.namedWindow(windowName, cv2.WINDOW_NORMAL)
result = None

# Video capture object so we can process the video
source = cv2.VideoCapture(cameraDeviceIndex)

while alive:
    # Check if the frame is not empty
    hasFrame, frame = source.read()
    if not hasFrame:
        break

    frame = cv2.flip(frame, 1)

    # Set filters
    if imageFilter == PREVIEW:
        result = frame
    elif imageFilter == EDGE:
        result = cv2.Canny(frame, 80, 150)
    elif imageFilter == BLUR:
        result = cv2.blur(frame, (13, 13))

    # Show filters
    cv2.imshow(windowName, result)

    key = cv2.waitKey(1)
    if key == ord('Q') or key == ord('q') or key == 27:
        alive = False
    elif key == ord('C') or key == ord('c'):
        imageFilter = EDGE
    elif key == ord('B') or key == ord('b'):
        imageFilter = BLUR
    elif key == ord('P') or key == ord('p'):
        imageFilter = PREVIEW

source.release()
cv2.destroyWindow(windowName)
