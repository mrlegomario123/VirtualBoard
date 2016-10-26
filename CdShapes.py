import cv2
import imutils
from CdShape import *

class CdShapes():

    def __init__(self):
        pass

    def shapeDetected(self, allShapes):
        if (len(allShapes) != 0):
            print('arc length = ' + str(allShapes[0].getArcLen()))
            shapeFound = True
        else:
            print('no shape detected')
            shapeFound = False
        return shapeFound

    def findContours(self, image, resultimage, drawcol, mode):

        cnts = cv2.findContours(resultimage.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
        cnts = cnts[0] if imutils.is_cv2() else cnts[1]
        # print "-----------"

        allshapes = []
        for c in cnts:

            oc = c
            al = cv2.arcLength(c, True)
            epsilon = 0.0475 * al
            oc = cv2.approxPolyDP(c, epsilon, True)
            numv = len(oc)

            shape = self.__estimateShape(numv, al, mode)

            if (shape == 'circle' or shape == 'square' or shape == 'triangle'):
                # compute the center of the contour
                M = cv2.moments(oc)
                dv = M["m00"]
                if (dv > 0):
                    cX = int(M["m10"] / dv)
                    cY = int(M["m01"] / dv)
                    # draw the contour and center of the shape on the image
                    cv2.drawContours(image, [oc], -1, drawcol, 2)
                    cv2.circle(image, (cX, cY), 7, drawcol, -1)
                    s = CdShape({'coords' : [cX,cY], 'arclen' : al, 'shape' : shape, 'numv' : numv})
                    allshapes.append(s)
                    '''nu.append([[cX, cY], al, shape, numv])'''

        return allshapes

    '''
    Param   shape                   Instance of CdShape
    Param   shaperequest            String
    '''

    def __estimateShape(self, numv, arclen , mode):
        squareArc = mode[1]
        circleArc = mode[2]
        if (numv == 4 and (squareArc*0.75) < arclen < (squareArc*1.5)):
            return 'square'

        elif (numv == 3 and (circleArc*0.75) < arclen < (circleArc*1.5)):
            return 'triangle'

        else:
            return None

        '''
        elif (4 < numv < 15):
            return 'circle'

        else:
                return None


            else:
                if (numv == 4 and 400 < arclen < 480):
                    return 'square'

            elif (4 < numv < 15 and 255 < arclen < 315):
                return 'circle'

            else:
                return  None
        '''
