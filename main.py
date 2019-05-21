import cv2
import numpy as np
import imutils
import math

WIDTH = 900
HEIGHT = 780

actualSet = 0

origemPlano = (0, 0)
xPlano = (0, 0)
yPlano = (0, 0)
rotation = 0
actualShow = 0
xTop = (0, 0)
xBot = (0, 0)
ix, iy = 0, 0
dPos = (0, 0)
prop = 1
corrected = False
# mouse callback function
def draw_circle(event,x,y,flags,param):
    global ix,iy
    global origemPlano
    global functions
    ix = x
    iy = y
    if event == cv2.EVENT_LBUTTONDOWN:
        functionsBasic[actualSet]()
        print(origemPlano, rotation)


def defineXTop():
    global xTop
    global actualSet
    xTop = (ix, iy)
    actualSet += 1


def defineXBot():
    global xTop
    global xBot
    global rotation
    global actualSet
    global actualShow
    global origemPlano
    global xPlano
    global yPlano
    xBot = (ix, iy)
    rotation = np.degrees(-(math.atan((xBot[0] - xTop[0]) / (xBot[1] - xTop[1]))))
    xBot = rotateAroundCenter(xBot)
    xTop = rotateAroundCenter(xTop)
    print(rotation)
    actualSet += 1
    actualShow += 1


def drawing():
    global dPos
    dPos = (int((ix-origemPlano[0])*prop), int((iy-origemPlano[1])*prop))
    print("ROTACIONADO")


def rotateImage(image, angle):
    image_center = (0, 0)
    rot_mat = cv2.getRotationMatrix2D(image_center, angle, 1.0)
    result = cv2.warpAffine(image, rot_mat, image.shape[1::-1], flags=cv2.INTER_LINEAR)
    return result


def rotateAroundCenter(node):
    aux = (int(node[0]*math.cos(np.radians(-rotation))-node[1]*math.sin((np.radians(-rotation)))),
           int(node[0]*math.sin(np.radians(-rotation))+node[1]*math.cos((np.radians(-rotation)))))
    return aux


def initialization():
    dst = cv2.Canny(img, 50, 200, None, 3)
    cdst = cv2.cvtColor(dst, cv2.COLOR_GRAY2BGR)
    linesP = cv2.HoughLinesP(dst, 1, np.pi / 180, 50, None, 50, 10)
    if linesP is not None:
        for i in range(0, len(linesP)):
            l = linesP[i][0]
            cv2.line(cdst, (l[0], l[1]), (l[2], l[3]), (0, 0, 255), 3, cv2.LINE_AA)
    cv2.imshow('JANELA', cdst)


def initialization2():
    src = rotateImage(img, rotation)
    dst = cv2.Canny(src, 50, 200, None, 3)
    cdst = cv2.cvtColor(dst, cv2.COLOR_GRAY2BGR)
    linesP = cv2.HoughLinesP(dst, 1, np.pi / 180, 50, None, 50, 10)
    if linesP is not None:
        for i in range(0, len(linesP)):
            l = linesP[i][0]
            cv2.line(cdst, (l[0], l[1]), (l[2], l[3]), (0, 0, 255), 3, cv2.LINE_AA)
    cv2.line(cdst, xTop, xBot, (255, 255, 255), 2)
    cv2.imshow('JANELA', cdst)


def running():
    rotated = rotateImage(img, rotation)
    cv2.line(rotated, origemPlano, xPlano, (255, 0, 0), 2)
    cv2.line(rotated, origemPlano, yPlano, (255, 0, 0), 2)
    cv2.line(rotated, xPlano, (xPlano[0], yPlano[1]), (255, 0, 0), 2)
    cv2.line(rotated, yPlano, (xPlano[0], yPlano[1]), (255, 0, 0), 2)
    crop_img = img[origemPlano[1]:origemPlano[1] + (yPlano[1] - origemPlano[1]),
                   origemPlano[0]:origemPlano[0] + (xPlano[0] - origemPlano[0])]
    cv2.line(crop_img, (int((xPlano[0] - origemPlano[0])/2), 0), (int((xPlano[0] - origemPlano[0])/2), int(yPlano[1] - origemPlano[1])), (255, 255, 255), 2)
    cv2.imshow('JANELA', crop_img)


functionsBasic = [defineXTop, defineXBot, drawing]
functionsShowing = [initialization, initialization2, running]
cap = cv2.VideoCapture(0)
_, img = cap.read()
cv2.imshow("JANELA", img)
cv2.setMouseCallback('JANELA',draw_circle)
while(1):
    _, img = cap.read()
    functionsShowing[actualShow]()

    k = cv2.waitKey(17)
    if k == 27:
        break
cv2.destroyAllWindows()
