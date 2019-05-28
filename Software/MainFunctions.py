import numpy as np
import cv2 as cv
import Variables
import math
import GeneralFunctions as Functs
import time
import copy
import GUI

term_criteria = (cv.TERM_CRITERIA_EPS | cv.TERM_CRITERIA_COUNT, 10, 1)


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


def wait():
    a = 0



def startCapture():
    cap = cv.VideoCapture(0)
    _, Variables.std_frame = cap.read()
    Variables.std_frame = cv.resize(Variables.std_frame, (850, 650))
    cv.imshow("System Vision", Variables.std_frame)

    cv.setMouseCallback('System Vision', Functs.setMousePosition)
    while(True):

        status, Variables.std_frame = cap.read()

        if status:
            h, w = Variables.std_frame.shape[:2]
            newcameramtx, roi = cv.getOptimalNewCameraMatrix(Variables.mtx, Variables.dist, (w, h), 1, (w, h))
            Variables.std_frame = cv.undistort(Variables.std_frame, Variables.mtx, Variables.dist, None, newcameramtx)
            Variables.std_frame = Functs.rotateImage(Variables.std_frame, Variables.rotation)
            Variables.std_frame = cv.resize(Variables.std_frame, (850, 650))
            if Variables.cornersDefined:
                Variables.std_frame = Functs.four_point_transform(Variables.std_frame, np.asarray([Variables.cornerLT,
                                                                                                   Variables.cornerLB,
                                                                                                   Variables.cornerRT,
                                                                                                   Variables.cornerRB], dtype=np.float32))
                Variables.std_frame = cv.resize(Variables.std_frame, (850, 650))
                Variables.ball_frame = cv.cvtColor(copy.deepcopy(Variables.std_frame), cv.COLOR_RGB2HSV)
                lower_color = np.array([Variables.l_h, Variables.l_s, Variables.l_v])
                upper_color = np.array([Variables.u_h, Variables.u_s, Variables.u_v])
                mask = cv.inRange(Variables.ball_frame, lower_color, upper_color)
                cv.imshow('mask', mask)
                Variables.ballMask = mask
                cnts = cv.findContours(mask.copy(), cv.RETR_EXTERNAL, cv.CHAIN_APPROX_SIMPLE)[-2]
                center = None
                if len(cnts) > 0:
                    # find the largest contour in the mask, then use
                    # it to compute the minimum enclosing circle and
                    # centroid
                    c = max(cnts, key=cv.contourArea)
                    ((x, y), radius) = cv.minEnclosingCircle(c)
                    M = cv.moments(c)
                    if M["m10"] != 0 or M["m00"] != 0 or M["m01"] != 0:
                        center = (int(M["m10"] / M["m00"]), int(M["m01"] / M["m00"]))

                    # only proceed if the radius meets a minimum size
                    if radius > 5:
                        Variables.ball_center = (int(x), int(y))
                        cv.circle(Variables.std_frame, Variables.ball_center, int(radius), (0, 255, 255), 2)
                # Drawing
                cv.circle(Variables.std_frame, (425, 325), 100, (255, 255, 255), 3)
                cv.line(Variables.std_frame, (50, 150), (125, 150), (255, 255, 255), 3)
                cv.line(Variables.std_frame, (50, 500), (125, 500), (255, 255, 255), 3)
                cv.line(Variables.std_frame, (125, 150), (125, 500), (255, 255, 255), 3)
                cv.line(Variables.std_frame, (725, 150), (800, 150), (255, 255, 255), 3)
                cv.line(Variables.std_frame, (725, 500), (800, 500), (255, 255, 255), 3)
                cv.line(Variables.std_frame, (725, 500), (725, 150), (255, 255, 255), 3)
                cv.circle(Variables.std_frame, (237, 125), 10, (255, 255, 255), 3)
                cv.circle(Variables.std_frame, (237, 325), 10, (255, 255, 255), 3)
                cv.circle(Variables.std_frame, (237, 525), 10, (255, 255, 255), 3)
                cv.circle(Variables.std_frame, (613, 125), 10, (255, 255, 255), 3)
                cv.circle(Variables.std_frame, (613, 325), 10, (255, 255, 255), 3)
                cv.circle(Variables.std_frame, (613, 525), 10, (255, 255, 255), 3)
                cv.line(Variables.std_frame, (425, 0), (425, 650), (255, 255, 255), 3)
            else:
                if Variables.actualPoint == 2:
                    cv.line(Variables.std_frame, tuple(Variables.cornerLT), tuple(Variables.cornerLB), (255, 0, 0), 2)
                elif Variables.actualPoint == 3:
                    cv.line(Variables.std_frame, tuple(Variables.cornerLT), tuple(Variables.cornerLB), (255, 0, 0), 2)
                    cv.line(Variables.std_frame, tuple(Variables.cornerLB), tuple(Variables.cornerRB), (255, 0, 0), 2)
            cv.imshow("System Vision", Variables.std_frame)
            functions[Variables.actualFunction]()
            cv.waitKey(10)
        else:
            cap = cv.VideoCapture('bolinha.avi')


def startMain():
    global functions
    global views
    functions = [setPositions, configureField, configurePerspective, wait]
