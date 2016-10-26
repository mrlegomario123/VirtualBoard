import numpy as np
import cv2

class CdHSV():

    def __init__(self):
        pass

    def __makeHSVhl(self, a):
        iLowH = a[0][0]
        iLowS = a[1][0]
        iLowV = a[2][0]
        iHighH = a[0][1]
        iHighS = a[1][1]
        iHighV = a[2][1]
        a1 = np.array([iLowH, iLowS, iLowV],dtype = "uint8")
        a2 = np.array([iHighH, iHighS, iHighV], dtype = "uint8")
        return a1,a2

    def hsvthreashimage(self, imgHSV,a):
        a1,a2 = self.__makeHSVhl(a)
        imgThresholded = cv2.inRange(imgHSV, a1, a2)
        kernel = (5, 5)
        imgThresholded = cv2.erode(imgThresholded, cv2.getStructuringElement(cv2.MORPH_ELLIPSE, kernel ))
        imgThresholded = cv2.dilate(imgThresholded, cv2.getStructuringElement(cv2.MORPH_ELLIPSE, kernel))
        imgThresholded = cv2.dilate(imgThresholded, cv2.getStructuringElement(cv2.MORPH_ELLIPSE, kernel))
        imgThresholded = cv2.erode(imgThresholded, cv2.getStructuringElement(cv2.MORPH_ELLIPSE, kernel))
        return imgThresholded