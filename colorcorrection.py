import cv2
import numpy as np
import subprocess

def func(i):
	return i


cap = cv2.VideoCapture(0)
cv2.namedWindow("Color Correction")

cv2.createTrackbar("Red", "Color Correction", 150, 250, func)
cv2.createTrackbar("Blue", "Color Correction", 140, 250, func)
cv2.createTrackbar("Gain", "Color Correction", 160, 255, func)
cv2.createTrackbar("Exposure", "Color Correction", 60, 625, func)

while True:
	_, frame = cap.read()
	RED = cv2.getTrackbarPos("Red", "Color Correction")
	BLUE = cv2.getTrackbarPos("Blue", "Color Correction")
	GAIN = cv2.getTrackbarPos("Gain", "Color Correction")
	EXPOSURE = cv2.getTrackbarPos("Exposure", "Color Correction")
	if EXPOSURE > 0:	
		bashCommand = f"v4l2-ctl -d /dev/video0 -c white_balance_red_component={RED} -c white_balance_blue_component={BLUE} -c gain={GAIN} -c exposure_absolute={EXPOSURE}"	
		process = subprocess.Popen(bashCommand.split(), stdout=subprocess.PIPE)
		output, error = process.communicate()
	cv2.imshow("Capture", frame)	
	k = cv2.waitKey(100)
	if k == 27:
		break
