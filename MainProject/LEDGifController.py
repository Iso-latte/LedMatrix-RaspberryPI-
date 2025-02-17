import time
import RPi.GPIO as GPIO
from rgbmatrix import RGBMatrix, RGBMatrixOptions
from PIL import Image
from MainProject.GifHander import GifHandler
import os

class MainMatrix:

    def __init__(self):
        self.list= None
        self.options = RGBMatrixOptions()
        self.options.rows=32 #number of rows
        self.options.cols = 32 #number of columns
        self.options.multiplexing = 0
        self.options.chain_length = 1  #number of boards connected
        self.options.parallel=1 #Num of paralel chains
        self.options.hardware_mapping = 'adafruit-hat' #mapping gpio pins to already configured
        self.options.brightness = 100#default 100
        self.options.inverse_colors= False
        self.options.drop_privileges = 0
        self.matrix = RGBMatrix(options = self.options)
        self.keepgoing = False

    def setList(self,List):
        self.list = List
    
    def setKeepGoingTrue(self):
        self.keepgoing = True
    
    def setKeepGoingFalse(self):
        self.keepgoing = False
    
    def simulateLED(self,filename):
        try:
            for x in self.list:
                image = Image.open("./Assets/Pics/"+filename+"Pics/"+x)
                matrixColor = image.convert('RGBA')
                image.thumbnail((image.height,image.width),Image.ANTIALIAS)
                self.matrix.SetImage(matrixColor.convert('RGB'))
                time.sleep(0.10)
        except FileNotFoundError:
            pass
