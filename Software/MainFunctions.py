from typing import Tuple

import numpy as np
import cv2 as cv
import Variables
import GeneralFunctions as Functs
import time
import copy
import threading
from queue import Queue
import math

term_criteria = (cv.TERM_CRITERIA_EPS | cv.TERM_CRITERIA_COUNT, 10, 1)
last_index = 0
ball_located = [(0, 0), (0, 0)]
robots_located = [[False, False, False], [False, False, False]]

#Thread setup
drawField = threading.Lock()

# Features Matching
index_params = dict(algorithm=0, trees=5)
search_params = dict()
flann = cv.FlannBasedMatcher(index_params, search_params)
sift = cv.xfeatures2d.SIFT_create()


class robot:
    def __init__(self, i):
        self.position = (0, 0)
        self.rotation = 0
        self.image = cv.imread("Robos/robo " + str(i) + ".jpg", cv.IMREAD_GRAYSCALE)
        print("Robos/robo_" + str(i) + ".jpg")
        self.kp_image, self.desc_image = sift.detectAndCompute(self.image, None)
        self.index = i

    def setPos(self, position):
        self.position = position

    def setRotation(self, rotation):
        self.rotation = rotation


robots = (robot(1), robot(2), robot(3))


class instance:
    def __init__(self, image, index):
        start_time = time.time()
        image = cv.undistort(image, Variables.mtx, Variables.dist, None, Variables.newcameramtx)
        image = Functs.rotateImage(image, Variables.rotation)
        image = cv.resize(image, (1275, 975))
        image = Functs.four_point_transform(image, np.asarray([Variables.cornerLT,
                                                               Variables.cornerLB,
                                                               Variables.cornerRT,
                                                               Variables.cornerRB], dtype=np.float32))
        image = cv.resize(image, (1275, 975))
        ball_frame = cv.cvtColor(copy.deepcopy(image), cv.COLOR_RGB2HSV)
        ball_mask = createBallMask(ball_frame)
        grayframe = cv.cvtColor(image, cv.IMREAD_GRAYSCALE)

        cv.imshow('Ball Mask', ball_mask)
        q.put((ball_mask, 1, index, None))
        #q.put((grayframe, 2, index, robots[0]))
        #q.put((grayframe, 2, index, robots[1]))
        #q.put((grayframe, 2, index, robots[2]))
        while ball_located[index] == (0, 0):
            pass
        #while robots_located[index][0] is False:
        #    pass
        #while robots_located[index][1] is False:
        #    pass
        #while robots_located[index][2] is False:
        #    pass
        ball_location = ball_located[index]
        robots_located[index] = [False, False, False]
        ball_located[index] = (0, 0)
        # Comandos para o robozinho

        #
        Variables.lastBallLocation = ball_location
        drawField(image)
        print("TEMPO POR CICLO = ", time.time() - start_time)



def startCapture():
    global cap
    global timer
    global lastTime
    cap = cv.VideoCapture(Variables.capSource)
    global q
    global t
    global framesProcessed
    framesProcessed = 0
    lastTime = time.time()
    q = Queue()
    for x in range(10):
        t = threading.Thread(target=mainThreader)
        t.daemon = True
        t.start()
    timer = threading.Timer(0.1, clockTimer)
    timer.start()
    FPS = threading.Timer(1, calculaFPS)
    FPS.start()


def clockTimer():
    global cap
    global lastTime
    global last_index
    if last_index == 0:
        index = 1
        last_index = 1
    else:
        index = 0
        last_index = 0
    status, image = cap.read()
    if Variables.stopFlag:
        time.sleep(1)
        cv.destroyAllWindows()
        q.join()
    elif status:
        timer = threading.Timer(0.3, clockTimer)
        timer.start()
        q.put((image, 0, index, None))
    else:
        cap = cv.VideoCapture(Variables.capSource)
        timer = threading.Timer(0.3, clockTimer)
        timer.start()
        q.put((image, 0, index, None))


def calculaFPS():
    global framesProcessed
    print("FPS = " + str(framesProcessed) + "\n")
    framesProcessed = 0
    FPS = threading.Timer(1, calculaFPS)
    if Variables.stopFlag is False:
        FPS.start()


def findBall(ball_mask, index):
    global radius
    global ball_located
    cnts = cv.findContours(ball_mask, cv.RETR_EXTERNAL, cv.CHAIN_APPROX_SIMPLE)[-2]
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
            ball_located[index] = (int(x), int(y))
        else:
            ball_located[index] = (1, 1)
    else:
        ball_located[index] = (1, 1)


def drawField(image):
    cv.circle(image, Variables.lastBallLocation, int(radius), (0, 255, 255), 2)
    cv.circle(image, (int(85*Variables.proportion), int(65*Variables.proportion)), int(20*Variables.proportion), (255, 255, 255), 3)
    cv.line(image, (int(10*Variables.proportion), int(30*Variables.proportion)), (int(25*Variables.proportion), int(30*Variables.proportion)), (255, 255, 255), 3)
    cv.line(image, (int(10*Variables.proportion), int(100*Variables.proportion)), (int(25*Variables.proportion), int(100*Variables.proportion)), (255, 255, 255), 3)
    cv.line(image, (int(25*Variables.proportion), int(30*Variables.proportion)), (int(25*Variables.proportion), int(100*Variables.proportion)), (255, 255, 255), 3)
    cv.line(image, (int(145*Variables.proportion), int(30*Variables.proportion)), (int(160*Variables.proportion), int(30*Variables.proportion)), (255, 255, 255), 3)
    cv.line(image, (int(145*Variables.proportion), int(100*Variables.proportion)), (int(160*Variables.proportion), int(100*Variables.proportion)), (255, 255, 255), 3)
    cv.line(image, (int(145*Variables.proportion), int(100*Variables.proportion)), (int(145*Variables.proportion), int(30*Variables.proportion)), (255, 255, 255), 3)
    cv.circle(image, (int(47.5*Variables.proportion), int(25*Variables.proportion)), 10, (255, 255, 255), 3)
    cv.circle(image, (int(47.5*Variables.proportion), int(65*Variables.proportion)), 10, (255, 255, 255), 3)
    cv.circle(image, (int(47.5*Variables.proportion), int(105*Variables.proportion)), 10, (255, 255, 255), 3)
    cv.circle(image, (int(122.5*Variables.proportion), int(25*Variables.proportion)), 10, (255, 255, 255), 3)
    cv.circle(image, (int(122.5*Variables.proportion), int(65*Variables.proportion)), 10, (255, 255, 255), 3)
    cv.circle(image, (int(122.5*Variables.proportion), int(105*Variables.proportion)), 10, (255, 255, 255), 3)
    cv.line(image, (int(85*Variables.proportion), 0), (int(85*Variables.proportion), int(130*Variables.proportion)), (255, 255, 255), 3)
    cv.imshow("System Vision", image)
    global framesProcessed
    framesProcessed += 1


def createBallMask(ball_frame):
    lower_color = np.array([Variables.l_h, Variables.l_s, Variables.l_v])
    upper_color = np.array([Variables.u_h, Variables.u_s, Variables.u_v])
    return cv.inRange(ball_frame, lower_color, upper_color)


def findRobot(grayframe, index, robot):
    start_time = time.time()
    kp_grayframe, desc_grayframe = sift.detectAndCompute(grayframe, None)
    matches = flann.knnMatch(robot.desc_image, desc_grayframe, k=2)
    good_points = []
    for m, n in matches:
        if m.distance < 0.6 * n.distance:
            good_points.append(m)
    if len(good_points) > 10:
        query_pts = np.float32([robot.kp_image[m.queryIdx].pt for m in good_points]).reshape(-1, 1, 2)
        train_pts = np.float32([kp_grayframe[m.trainIdx].pt for m in good_points]).reshape(-1, 1, 2)
        matrix, mask = cv.findHomography(query_pts, train_pts, cv.RANSAC, 5.0)
        matches_mask = mask.ravel().tolist()
        # Perspective transform
        h, w = robot.image.shape
        pts = np.float32([[0, 0], [0, h], [w, h], [w, 0]]).reshape(-1, 1, 2)
        dst = cv.perspectiveTransform(pts, matrix)
        midLeft = (int((dst[0][0][0] + dst[1][0][0]) / 2), int((dst[0][0][1] + dst[1][0][1]) / 2))
        midRight = (int((dst[2][0][0] + dst[3][0][0]) / 2), int((dst[2][0][1] + dst[3][0][1]) / 2))
        robot.position = (int((midLeft[0] + midRight[0]) / 2), int((midLeft[1] + midRight[1]) / 2))
        x1 = 100
        x2 = midRight[0] - robot.position[0]
        y1 = 0
        y2 = midRight[1] - robot.position[1]
        cos = (x1 * x2 + y1 * y2)
        bot = math.sqrt(math.pow(x1, 2) + math.pow(y1, 2)) * math.sqrt(math.pow(x2, 2) + math.pow(y2, 2))
        cos = cos / bot
        angle = np.degrees(math.acos(cos))
        if midRight[1] < robot.position[1]:
            angle *= -1
    global robots_located
    if robot.index == 1:
        robots_located[index] = [True, robots_located[index][1], robots_located[index][2]]
    elif robot.index == 2:
        robots_located[index] = [robots_located[index][0], True, robots_located[index][2]]
    else:
        robots_located[index] = [robots_located[index][0], robots_located[index][1], True]
    print("TEMPO LEVADO: " + str(time.time() - start_time))



def mainThreader():
    while True:
        (image, op, index, robot) = q.get()
        if op == 0:
            instance(image, index)
        elif op == 1:
            findBall(image, index)
        elif op == 2:
            findRobot(image, index, robot)
        q.task_done()
