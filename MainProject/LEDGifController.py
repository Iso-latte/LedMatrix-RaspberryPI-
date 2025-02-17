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
        self.options.drop_privileges =1
        self.matrix = RGBMatrix(options = self.options)
        self.keepgoing = False


  #  def getprivileges(self):
   #     print(self.options.__runtime_options.drop_privileges)
    
    def setList(self,List):
        self.list = List
    
    def setKeepGoingTrue(self):
        self.keepgoing = True
    
    def setKeepGoingFalse(self):
        self.keepgoing = False
    
    def simulateLED(self,filename):
        try:
            for x in self.list:
                image = Image.open("/home/pi/Documents/GifControllerV_02/Pics/"+filename+"Pics/"+x)
                matrixColor = image.convert('RGBA')
                image.thumbnail((image.height,image.width),Image.ANTIALIAS)
                self.matrix.SetImage(matrixColor.convert('RGB'))
                time.sleep(0.21)
        except FileNotFoundError:
            pass

matrix =MainMatrix()
#atrix.simulateLED('heart')

#m=RGBMatrixOptions()
#m.__get__()

##listOfPics =[]
#for x in os.listdir('/home/pi/Documents/GifControllerV_02/Pics/cityPics'):
 #   listOfPics.append(x)
  #  image = Image.open(x)
#print(listOfPics)
#image = Image.open(x)
#matrix.setList(listOfPics)
#for x in range(0,1):
#    matrix.simulateLED()