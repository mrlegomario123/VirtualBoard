
class CdColour():
    def __init__(self, _hsv, _bgr, _cstr):
        self.hsv = _hsv
        self.bgr = _bgr
        self.cstr = _cstr

    def getHsv(self):
        return (self.hsv)

    def getBgr(self):
        return (self.bgr)

    def getColStr(self):
        return (self.cstr)

