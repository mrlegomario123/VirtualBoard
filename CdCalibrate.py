from CdColour import *

class CdCalibrate():

    def __init__(self):
        self.__multiplier = None
        self.__shapeDetected = 0
        self.__allArcLength = []
        self.__squareArc = None

    def getColourBoundary(self, counter, colourStr):
        self.__multiplier = int(counter/5)
        boundary = self.increaseRange(self.__multiplier)
        col_boundary = CdColour(boundary,(255,0,0),colourStr)
        return col_boundary


    def docalibrate(self, shapeController, allShapes, counter, colourStr, col_boundary, shape):

        RunCode = True

        shapeFound = shapeController.shapeDetected(allShapes)

        # shapeFound = shapeController.detectShape(allShapes[0], shape)
        if (shapeFound == True):
            if allShapes[0].getShape() == shape:
                self.__shapeDetected += 1
                print('shape detected = ' + str(self.__shapeDetected))
                self.__allArcLength.append(allShapes[0].getArcLen())
                if (self.__shapeDetected > 5):
                    totalArcLength = 0
                    for i in self.__allArcLength:
                        totalArcLength += i
                    averageArcLength = totalArcLength / len(self.__allArcLength)
                    print('average arc length = ' + str(averageArcLength))
                    print('Max = ' + str(averageArcLength * 1.1))
                    print('Min = ' + str(averageArcLength * 0.9))
                    arcLengthValid = True
                    for i in self.__allArcLength:
                        print(i)
                        if ((averageArcLength * 0.9) < i < (averageArcLength * 1.1)):
                            print('pass')
                        else:
                            arcLengthValid = False
                            print('fail')
                    if (arcLengthValid):
                        self.__squareArc = averageArcLength
                        print('wawa = ' + str(self.__squareArc))
                        if (counter > 4):
                            boundary = self.increaseRange(1.5 + self.__multiplier)
                            col_boundary = CdColour(boundary, (255, 0, 0), colourStr)
                        tempColRange = col_boundary.getHsv()
                        print('weba = ' + str(tempColRange))
                        RunCode = False
                    else:
                        self.__shapeDetected = 0
                        self.__allArcLength = []
            else:
                self.__shapeDetected = 0
                self.__allArcLength = []
        else:
            self.__shapeDetected = 0
            self.__allArcLength = []

        return  RunCode, col_boundary

        # Need to find a counter / shape


    def getSquareArc(self):
        return  self.__squareArc




    def increaseRange(self, multiplier):
        Hmin = (99 * (0.95 ** multiplier))
        Hmax =  (123 * (1.05 ** multiplier))
        Vmin =  (121 * (0.95 ** multiplier))
        if (Hmin < 0):
            Hmin = 0
        if (Hmax > 180):
            Hmax = 180
        if (Vmin < 0):
            Vmin = 0
        boundary = [[Hmin, Hmax], [Vmin, 255], [0, 255]]
        return boundary
