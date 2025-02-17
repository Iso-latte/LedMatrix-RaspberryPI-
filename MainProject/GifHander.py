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
    
    def makeDirectory(self):
        #This method makes the directory to add all the frames of the gif to
        pics_dir = os.path.join(".","Assets","Pics")
        new_folder = os.path.join(pics_dir, self.fileNameWithoutEx+"Pics")
        try:
            os.mkdir(new_folder) #making directory for pics
        except FileExistsError:
            print('It there bruh')
        
    def addFrames(self):
        pics_folder = os.path.join(".", "Assets", "Pics", self.fileNameWithoutEx + 'Pics')
        imageObject = Image.open(self.pathOfGif)
        try:
            for frame in range(imageObject.n_frames):
                imageObject.seek(frame)
                frame_path = os.path.join(pics_folder, f"{self.counterOne}_{self.fileNameWithoutEx}.png")
                imageObject.save(frame_path)
                self.counterOne += 1

            for filename in os.listdir(pics_folder):
                print(filename)
                file_path = os.path.join(pics_folder, filename)
                imageObject2 = Image.open(file_path)
                imageObject2 = imageObject2.resize((32, 32), Image.ANTIALIAS)
                new_file_path = os.path.join(pics_folder, f"{self.counterTwo}_{self.fileNameWithoutEx}.png")
                imageObject2.save(new_file_path)
                self.counterTwo += 1
        except FileNotFoundError:
            print('whoopse IDK why i get this error so i overrided it')

    def setUpGif(self):
        self.setPathOfGif()
        self.setFileName()
        self.makeDirectory()
        self.addFrames()
    
    def deleteGif(self, gifpath):
        print(os.getcwd())
        # Extract just the filename, e.g., "ghost.gif"
        base = os.path.basename(gifpath)
        # Remove the extension, e.g., "ghost"
        file_without_ext = os.path.splitext(base)[0]
        # Construct the path to the folder where the frames are stored
        pics_folder = os.path.join(".", "Assets", "Pics", file_without_ext + "Pics")
        # Remove the directory containing the frames
        shutil.rmtree(pics_folder)
        # Remove the GIF file itself
        os.remove(gifpath)

    def listForLED(self):
        for filename in os.listdir('./Assets/Pics/'+self.fileNameWithoutEx+'Pics'):
            self.listOfPics.append(filename)
        return self.listOfPics