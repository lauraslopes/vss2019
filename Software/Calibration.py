import cv2 as cv
import numpy as np
import glob
import Variables
import GeneralFunctions as Functs
import math


def configureCalibration():
    global functions
    global views
    functions = [setPositions, configureField, configurePerspective, None]


def setPositions():
    if Variables.topMidLane == (0, 0):
        if (Variables.ix, Variables.iy) != (0, 0):
            Variables.topMidLane = (Variables.ix, Variables.iy)
            Variables.ix, Variables.iy = 0, 0
    else:
        if (Variables.ix, Variables.iy) != (0, 0):
            Variables.botMidLane = (Variables.ix, Variables.iy)
            Variables.ix, Variables.iy = 0, 0
            Variables.actualFunction += 1


def configureField():
    Variables.rotation = np.degrees(-(math.atan((Variables.botMidLane[0] - Variables.topMidLane[0]) / (Variables.botMidLane[1] - Variables.topMidLane[1]))))
    Variables.topMidLane = Functs.rotateAroundCenter(Variables.topMidLane)
    Variables.botMidLane = Functs.rotateAroundCenter(Variables.botMidLane)
    Variables.matrixHeight = Variables.botMidLane[1] - Variables.topMidLane[1]
    Variables.matrixWidth = int((Variables.matrixHeight*170)/130)
    Variables.matrixOrigin = (Variables.botMidLane[0]-int(Variables.matrixWidth/2), Variables.topMidLane[1])
    Variables.definedField = True
    Variables.actualFunction += 1


def configurePerspective():
    if Variables.cornerLT == [0, 0]:
        if (Variables.ix, Variables.iy) != (0, 0):
            Variables.cornerLT = [Variables.ix, Variables.iy]
            Variables.ix, Variables.iy = 0, 0
            Variables.actualPoint = 1
    elif Variables.cornerLB == [0, 0]:
        if (Variables.ix, Variables.iy) != (0, 0):
            Variables.cornerLB = [Variables.ix, Variables.iy]
            Variables.ix, Variables.iy = 0, 0
            Variables.actualPoint = 2
    elif Variables.cornerRB == [0, 0]:
        if (Variables.ix, Variables.iy) != (0, 0):
            Variables.cornerRB = [Variables.ix, Variables.iy]
            Variables.ix, Variables.iy = 0, 0
            Variables.actualPoint = 3
    elif Variables.cornerRT == [0, 0]:
        if (Variables.ix, Variables.iy) != (0, 0):
            Variables.cornerRT = [Variables.ix, Variables.iy]
            Variables.ix, Variables.iy = 0, 0
            Variables.cornersDefined = True
            Variables.actualFunction += 1


def CalibrarCamera():
    criteria = (cv.TERM_CRITERIA_EPS + cv.TERM_CRITERIA_MAX_ITER, 30, 0.001)

    # prepare object points, like (0,0,0), (1,0,0), (2,0,0) ....,(6,5,0)
    objp = np.zeros((4 * 9, 3), np.float32)
    objp[:, :2] = np.mgrid[0:9, 0:4].T.reshape(-1, 2)

    # Arrays to store object points and image points from all the images.
    objpoints = []  # 3d point in real world space
    imgpoints = []  # 2d points in image plane.

    images = glob.glob('CalibrationFrames/*.jpg')
    grayshape = 0
    for fname in images:
        img = cv.imread(fname)
        gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
        grayshape = gray.shape[::-1]
        # Find the chess board corners
        ret, corners = cv.findChessboardCorners(gray, (9, 4), None)

        # If found, add object points, image points (after refining them)
        if ret == True:
            objpoints.append(objp)

            corners2 = cv.cornerSubPix(gray, corners, (11, 11), (-1, -1), criteria)
            imgpoints.append(corners2)

            # Draw and display the corners
            img = cv.drawChessboardCorners(img, (7, 6), corners2, ret)
            cv.imshow('img', img)
            cv.waitKey(50)
    ret, Variables.mtx, Variables.dist, rvecs, tvecs = cv.calibrateCamera(objpoints, imgpoints, grayshape, None, None)

    cap = cv.VideoCapture(Variables.capSource)
    _, Variables.std_frame = cap.read()
    Variables.std_frame = cv.resize(Variables.std_frame, (850, 650))
    cv.imshow("System Vision", Variables.std_frame)

    cv.setMouseCallback('System Vision', Functs.setMousePosition)
    while (True):

        status, std_frame = cap.read()
        if status:
            h, w = std_frame.shape[:2]
            Variables.newcameramtx, _ = cv.getOptimalNewCameraMatrix(Variables.mtx, Variables.dist, (w, h), 1, (w, h))
            std_frame = cv.undistort(std_frame, Variables.mtx, Variables.dist, None, Variables.newcameramtx)
            std_frame = Functs.rotateImage(std_frame, Variables.rotation)
            std_frame = cv.resize(std_frame, (850, 650))
            if Variables.cornersDefined:
                cv.destroyAllWindows()
                break
            else:
                if Variables.actualPoint == 2:
                    cv.line(std_frame, tuple(Variables.cornerLT), tuple(Variables.cornerLB), (255, 0, 0), 2)
                elif Variables.actualPoint == 3:
                    cv.line(std_frame, tuple(Variables.cornerLT), tuple(Variables.cornerLB), (255, 0, 0), 2)
                    cv.line(std_frame, tuple(Variables.cornerLB), tuple(Variables.cornerRB), (255, 0, 0), 2)
            cv.imshow("System Vision", std_frame)
            functions[Variables.actualFunction]()
            cv.waitKey(10)
        else:
            cap = cv.VideoCapture(Variables.capSource)
    Variables.actualFunction = 0
    Variables.ui.setStartDisabled(False)
    cv.destroyAllWindows()
