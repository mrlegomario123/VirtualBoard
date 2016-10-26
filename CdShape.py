class CdShape():
    def __init__(self, attributes):
        self.name = ''
        self.colour = ''
        self.coords = attributes['coords']
        self.shape = attributes['shape']
        self.arclen = attributes['arclen']
        self.numv = attributes['numv']

    def setCoords(self, coords):
        self.coords = coords

    def setShape(self, shape):
        self.shape = shape

    def setColour(self, colour):
        self.colour = colour

    def setName(self, name):
        self.name = name

    def setArcLength(self, arclength):
        self.arclen = arclength

    def getCoords(self):
        return self.coords

    def getShape(self):
        return self.shape

    def getColour(self):
        return self.colour

    def getName(self):
        return self.name

    def getArcLen(self):
        return self.arclen

    def displayStats(self):
        print('coords = ' + str(self.coords) + ' shape = ' + self.shape)
        print('colour = ' + self.name + ' arclength = ' + str(self.arclen))
        if (self.name != ''):
            print('name = ' + self.name)
        print('\n')



