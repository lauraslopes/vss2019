import cv2
import numpy as np
WIDTH = 1360
HEIGHT = 1040
ix, iy = 0, 0
# mouse callback function
def draw_circle(event,x,y,flags,param):
    global ix,iy
    ix = x
    iy = y

# Create a black image, a window and bind the function to window
img = cv2.imread("frame2.jpg")
cv2.namedWindow('image')
cv2.setMouseCallback('image',draw_circle)
font = cv2.FONT_HERSHEY_SIMPLEX

while(1):
    img = cv2.imread("frame2.jpg")
    cv2.circle(img, (ix, iy), 50, (0, 255, 0), 2)
    cv2.line(img, (320, 0), (320, 480), (255, 255, 255), 2)
    cv2.circle(img, (320, 240), 50, (255, 255, 255), 2)
    cv2.putText(img,str(ix) + ', ' + str(iy),(ix - 38,iy - 5), font, .5, (200,255,155), 1, cv2.LINE_AA)
    cv2.imshow('image', img)
    k = cv2.waitKey(17)
    if k == 27:
        break
cv2.destroyAllWindows()