import cv2 as cv
import time

def setMousePosition(event, x, y, flags, param):
    if event == cv.EVENT_LBUTTONDOWN:
        cv.imwrite("frame%d.jpg" % int(time.time()), frame)

cap = cv.VideoCapture(0)
_, frame = cap.read()
cv.imshow('img', frame)
cv.setMouseCallback('img', setMousePosition)
while(True):
	_, frame = cap.read()
	cv.imshow('img', frame)
	k = cv.waitKey(34)
	if k == 27:
		break;
