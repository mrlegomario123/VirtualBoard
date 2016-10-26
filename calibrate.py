import numpy as np
import imutils

import time

import cv2

from CdColour import *
from CdShape import *
from CdCamera import *
from CdHSV import *
from CdShapes import *
from CdCalibrate import *


def findObject(imgHSV, image, col, mode):
    HSVimage = CdHSV()
    resultimage = HSVimage.hsvthreashimage(imgHSV, col.getHsv())
    allShapes = shapeController.findContours(image, resultimage, col.getBgr(), mode)
    return resultimage,allShapes


def mainSequence(mode, shape, colourStr, col_boundary):

    #print "Place " + counterColour + " counter"
    RunCode = True
    counter = 0
    squareArc = 0

    if(mode[0] == 'calibrate'):
        calibrator = CdCalibrate()
    else:
        calibrator = None

    while(RunCode):

        if(calibrator):
            col_boundary = calibrator.getColourBoundary(counter, colourStr)

        # Captures the image from the camera and converts it to hsv

        image = camera.captureImageBGR()
        imgHSV = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)

        timg,allShapes = findObject(imgHSV, image, col_boundary, mode)

        cv2.imshow("Thresholded Image " + col_boundary.getColStr(), timg)
        cv2.imshow("Original Image " , image)


        shapeFound = shapeController.shapeDetected(allShapes)
        #if(detectShape and mode[0] == 'calibrate'):

        if(calibrator):
            RunCode, col_boundary = calibrator.docalibrate(shapeController, allShapes, counter, colourStr, col_boundary, shape)
            squareArc = calibrator.getSquareArc()

        if (cv2.waitKey(10) == 27):
            RunCode = 'no'

        counter +=1
        print('')

    return(squareArc, col_boundary)

# ======================================== MAIN ============================================pooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooo

# col_blue = CdColour([[94,130],[115,255],[0,255]],(255,0,0), "blue")
# col_blue_lenient = CdColour([[54,180],[115,255],[0,255]],(255,0,0), "lenient blue")
col_blue_init = CdColour([[94,130],[115,255],[0,255]],(255,0,0), "blue")

camera = CdCamera()
camera.calibrateCamera(False)
shapeController = CdShapes()

squareArc, col_blue = mainSequence(['calibrate', 400, 0], 'square', 'blue', col_blue_init)
print('============== POOP =================')
mainSequence(['normal', squareArc, 275], 'all', 'blue', col_blue)


