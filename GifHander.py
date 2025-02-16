from PIL import Image
import shutil
import os

#Gif handler class
#This class is used to take the path of a gif
#Move it into the gif folder
class GifHandler:

    def __init__(self,gifPath):
        
        self.listOfPics = [] #Holds the list of frams from gif
        self.counterOne = 0 #Gives each frame a unique name
        self.counterTwo = 0 #resizes all frames
        self.fileNameWithEx = None #this will be set later(Holds gif name)
        self.fileNameWithoutEx=None #file name without the .gif
        self.pathOfGif = gifPath #path to the gif
        self.picPaths = None #This will be set later
        self.folderForFrames= None #Folder name where pics will be 
    
    def setPathOfGif(self):
        #This will move the gif into the gif folder
        try:
            locationForApp = shutil.copy(self.pathOfGif,'/home/pi/Documents/GifControllerV_02/Gifs') #Moves from whereever in computer to gif folder
            self.pathOfGif = locationForApp #sets the path to the gif folder
            print('\n\n\n'+self.pathOfGif)
        except shutil.Error:
            print('It exists bruh')
    
    def setFileName(self):
        #This method sets the file name to the name of the file and not the path
        name = self.pathOfGif.replace('/home/pi/Documents/GifControllerV_02/Gifs/',"") #shortens the name to tjust the *.gif file
        self.fileNameWithEx = name #sets the name to the .gif file
        self.fileNameWithoutEx = self.fileNameWithEx.replace('.gif','')#FileNameWithout the extention of .gif
        print(self.fileNameWithEx)
        print(self.fileNameWithoutEx)
    
    def makeDirectory(self):
        #This method makes the directory to add all the frames of the gif to
        try:
            os.mkdir('/home/pi/Documents/GifControllerV_02/Pics/'+self.fileNameWithoutEx+'Pics') #making directory for pics
        except FileExistsError:
            print('It there bruh')
    
    def addFrames(self):
        imageObject = Image.open(self.pathOfGif) #Creates an image object that opens the gif
        try:
            for frame in range(0, imageObject.n_frames):
                imageObject.seek(frame) #getting a frame from gif
                imageObject.save('/home/pi/Documents/GifControllerV_02/Pics/'+self.fileNameWithoutEx+'Pics/'+str(self.counterOne)+'_'+self.fileNameWithoutEx+'.png')
                self.counterOne +=1

            for filename in os.listdir('/home/pi/Documents/GifControllerV_02/Pics/'+self.fileNameWithoutEx+'Pics'):
                print(filename)
                imageObject2 = Image.open('/home/pi/Documents/GifControllerV_02/Pics/'+self.fileNameWithoutEx+'Pics/'+filename)
                imageObject2 = imageObject2.resize((32,32), Image.ANTIALIAS)
                imageObject2.save('/home/pi/Documents/GifControllerV_02/Pics/'+self.fileNameWithoutEx+'Pics'+'/'+str(self.counterTwo)+'_'+self.fileNameWithoutEx + '.png')
                self.counterTwo+=1
        except FileNotFoundError:
            print('whoopse IDK why i get this error so i overrided it')

    def setUpGif(self):
        self.setPathOfGif()
        self.setFileName()
        self.makeDirectory()
        self.addFrames()
    
    def deleteGif(self, gifpath):
        try:
            gifPath2 = gifpath.replace('/home/pi/Documents/GifControllerV_02/Gifs/','')
            shutil.rmtree(r'/home/pi/Documents/GifControllerV_02/Pics/'+gifPath2.replace('.gif','')+'Pics')
            os.remove(gifpath)            
        except FileNotFoundError:
            print('File aint here bruh')
            pass

    def listForLED(self):
        for filename in os.listdir('/home/pi/Documents/GifControllerV_02/Pics/'+self.fileNameWithoutEx+'Pics'):
            self.listOfPics.append(filename)
            #print(filename)
        return self.listOfPics

    


#newGif = GifHandler('/home/pi/Documents/GifController/gifs/poop.gif')
#newGif.setUpGif()
#list = newGif.listForLED()
#print(list[0])
#newGif.deleteGif('/home/pi/Documents/GifControllerV_02/Gifs/poop.gif')

