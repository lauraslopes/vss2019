import cv2 as cv
import numpy as np
import math
import Variables


# Correcao de perspectiva (funções prontas)
def order_points(pts):
    rect = np.zeros((4, 2), dtype="float32")
    s = pts.sum(axis=1)
    rect[0] = pts[np.argmin(s)]
    rect[2] = pts[np.argmax(s)]
    diff = np.diff(pts, axis=1)
    rect[1] = pts[np.argmin(diff)]
    rect[3] = pts[np.argmax(diff)]
    return rect


def four_point_transform(image, pts):
    rect = order_points(pts)
    (tl, tr, br, bl) = rect
    widthA = np.sqrt(((br[0] - bl[0]) ** 2) + ((br[1] - bl[1]) ** 2))
    widthB = np.sqrt(((tr[0] - tl[0]) ** 2) + ((tr[1] - tl[1]) ** 2))
    maxWidth = max(int(widthA), int(widthB))
    heightA = np.sqrt(((tr[0] - br[0]) ** 2) + ((tr[1] - br[1]) ** 2))
    heightB = np.sqrt(((tl[0] - bl[0]) ** 2) + ((tl[1] - bl[1]) ** 2))
    maxHeight = max(int(heightA), int(heightB))
    dst = np.array([
        [0, 0],
        [maxWidth - 1, 0],
        [maxWidth - 1, maxHeight - 1],
        [0, maxHeight - 1]], dtype="float32")
    M = cv.getPerspectiveTransform(rect, dst)
    warped = cv.warpPerspective(image, M, (maxWidth, maxHeight))
    return warped


# Funções gerais
def rotateAroundCenter(node):
    aux = (int(node[0]*math.cos(np.radians(-Variables.rotation))-node[1]*math.sin((np.radians(-Variables.rotation)))),
           int(node[0]*math.sin(np.radians(-Variables.rotation))+node[1]*math.cos((np.radians(-Variables.rotation)))))
    return aux


def rotateImage(image, angle):
    image_center = (0, 0)
    rot_mat = cv.getRotationMatrix2D(image_center, angle, 1.0)
    result = cv.warpAffine(image, rot_mat, image.shape[1::-1], flags=cv.INTER_LINEAR)
    return result


# Mouse Event
def setMousePosition(event, x, y, flags, param):
    global drawCoordinates
    drawCoordinates = (Variables.ix, Variables.iy)
    if event == cv.EVENT_LBUTTONDOWN:
        Variables.ix = x
        Variables.iy = y