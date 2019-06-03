import numpy as np


def setFrame(actualTurn, dest, source):
    if actualTurn == 0:
        dest = (source, dest[1])
    else:
        dest = (dest[0], source)


def Global():
    # Detecção da bolinha
    global l_h
    l_h = 0
    global l_s
    l_s = 0
    global l_v
    l_v = 0
    global u_h
    u_h = 179
    global u_s
    u_s = 255
    global u_v
    u_v = 255
    global lastBallLocation
    lastBallLocation = (0, 0)

    # Camera Calibration
    global cornerLT
    cornerLT = [0, 0]
    global cornerLB
    cornerLB = [0, 0]
    global cornerRT
    cornerRT = [0, 0]
    global cornerRB
    cornerRB = [0, 0]
    global actualFunction
    actualFunction = 0
    global topMidLane
    topMidLane = (0, 0)
    global botMidLane
    botMidLane = (0, 0)
    global ix, iy
    ix, iy = 0, 0
    global rotation
    rotation = 0
    global matrixOrigin
    matrixOrigin = (0, 0)
    global matrixWidth
    matrixWidth = (0, 0)
    global matrixHeight
    matrixHeight = (0, 0)
    global definedField
    definedField = False
    global actualPoint
    actualPoint = 0
    global cornersDefined
    cornersDefined = False
    global drawCoordinates
    drawCoordinates = (0, 0)
    global newcameramtx
    global mtx
    global dist
    global ui
    global actualImage
    actualImage = 0
    global stopFlag
    stopFlag = True
    global capSource
    capSource = "bolinha.avi"