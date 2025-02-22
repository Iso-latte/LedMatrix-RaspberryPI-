from PIL import Image
import shutil
import os

#Gif handler class
#This class is used to take the path of a gif
#Move it into the gif folder
class GifHandler:

    def __init__(self,gifPath):
        self.fileNameWithEx = None #this will be set later(Holds gif name)
        self.fileNameWithoutEx=None #file name without the .gif
        self.pathOfGif = gifPath #path to the gif
    
    def setPathOfGif(self):
        #This will move the gif into the gif folder
        try:
            locationForApp = shutil.copy(self.pathOfGif,'./Assets/Gifs') #Moves from whereever in computer to gif folder
            self.pathOfGif = locationForApp #sets the path to the gif folder
            print('\n\n\n'+self.pathOfGif)
        except shutil.Error:
            print('It exists bruh')
    
    def setFileName(self):
        #This method sets the file name to the name of the file and not the path
        name = self.pathOfGif.replace('./Assets/Gifs/',"") #shortens the name to tjust the *.gif file
        name = os.path.basename(self.pathOfGif)
        self.fileNameWithEx = name #sets the name to the .gif file
        self.fileNameWithoutEx = os.path.splitext(name)[0]
        print(self.fileNameWithEx)
        print(self.fileNameWithoutEx)

    def setUpGif(self):
        self.setPathOfGif()
        self.setFileName()
    
    def deleteGif(self, gifpath):
        print(os.getcwd())
        # Extract just the filename, e.g., "ghost.gif"
        base = os.path.basename(gifpath)
        # Remove the extension, e.g., "ghost"
        file_without_ext = os.path.splitext(base)[0]
        os.remove(gifpath)

