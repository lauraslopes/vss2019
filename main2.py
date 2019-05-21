import cv2
import numpy as np

video = cv2.VideoCapture(0)

_, first_frame = video.read()
x = 0
y = 0
width = 100
height = 100
roi = cv2.imread("bolinha.jpg")
hsv_roi = cv2.cvtColor(roi, cv2.COLOR_BGR2HSV)
roi_hist = cv2.calcHist([hsv_roi], [0], None, [180], [0, 180])
roi_hist = cv2.normalize(roi_hist, roi_hist, 0, 255, cv2.NORM_MINMAX)
term_criteria = (cv2.TERM_CRITERIA_EPS | cv2.TERM_CRITERIA_COUNT, 10, 1)

while True:
    _, frame = video.read()
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    mask = cv2.calcBackProject([hsv], [0], roi_hist, [0, 180], 1)
    _, track_window = cv2.meanShift(mask, (x, y, width, height), term_criteria)

    x, y, w, h = track_window
    print(x+(w/2), y+(h/2))
    cv2.circle(frame, (int(x+(w/2)), int(y+(h/2))), 50, (0, 255, 0), 2)

    cv2.imshow("Roi", roi)
    cv2.imshow("Mask", mask)
    cv2.imshow("Frame", frame)

    key = cv2.waitKey(33)
    if key == 27:
        break

video.release()
cv2.destroyAllWindows()
