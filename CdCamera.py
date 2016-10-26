from picamera.array import PiRGBArray
from picamera import PiCamera
import time

class CdCamera():

    def __init__(self):
        self.camera = PiCamera()

    def calibrateCamera(self, autooff):
        '''camera = PiCamera()'''
        if(autooff==True):
            self.camera.iso = 100
            time.sleep(2)
            self.camera.shutter_speed = self.camera.exposure_speed
            self.camera.exposure_mode = 'off'
            g = self.camera.awb_gains
            self.camera.awb_gains = g
            self.camera.awb_mode = 'off'
            time.sleep(0.1)

    def captureImageBGR(self):
        # Capture an image from the camera
        self.camera.resolution = (1024, 768)
        rawCapture = PiRGBArray(self.camera)
        self.camera.capture(rawCapture, format="bgr")
        return rawCapture.array

