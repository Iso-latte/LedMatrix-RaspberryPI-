
from MainProject.GifHander import GifHandler
from tkinter import *
from tkinter import filedialog
from MainProject.LEDGifController import MainMatrix
import os

matrix = MainMatrix()


def deleteGif(root):
    root.filename = filedialog.askopenfilename(title="select a gif", filetypes=[("Gif Files","*.gif")])#
    Gif = GifHandler(root.filename)
    Gif.deleteGif(root.filename)
    return root.filename

def firstGif(filename):
    listOfPics =[]
    os.chdir('/home/')
    for x in os.listdir('/home/pi/Documents/GifControllerV_02/Pics/'+filename+'Pics'):
        listOfPics.append(x)
    #print(listOfPics)
    matrix.setList(listOfPics)
    for x in range(0,1):
        matrix.simulateLED(filename)
        matrix.matrix.Clear()

def makeGifs(root):

    root.filename = filedialog.askopenfilenames(title="select a gif", filetypes=[("Gif Files","*.gif")])#
    list = []
    list.append(root.filename)
    print(list)


def makeGif(root):

    root.filename = filedialog.askopenfilename(title="select a gif", filetypes=[("Gif Files","*.gif")])#
    Gif = GifHandler(root.filename)
    Gif.setUpGif()
    
def changeGif(filename):
    listOfPics =[]
    for x in os.listdir('/home/pi/Documents/GifControllerV_02/Pics/'+filename+'Pics'):
        listOfPics.append(x)
    #print(listOfPics)
    matrix.setList(listOfPics)
    for x in range(0,1):
        matrix.simulateLED(filename)
        matrix.matrix.Clear()
    #pass 


    
def getFileNamesWithoutEx():
    listOfNames=[]
    for names in os.listdir('/home/pi/Documents/GifControllerV_02/Gifs'):
        nameOfGif = names.replace('.gif',"")
        listOfNames.append(nameOfGif)
    return listOfNames


def getFileNamesWithEx():
    listOfNames=[]
    for names in os.listdir('/home/pi/Documents/GifControllerV_02/Gifs'):
        nameOfGif = names
        listOfNames.append(nameOfGif)
    return listOfNames


def main():

    fileNames = getFileNamesWithoutEx()
    numberOfFiles = len(fileNames)
    column=0
    row = 5
    n=0

    gifButtonPady = 25
    gifButtonPadx =0
    gifButtonHeight = 4
    gifButtonWidth = 15

    root = Tk()
    root.title("MATRIX GOALS")
    root.maxsize(width=1050,height=600)
    root.resizable(False,False)

    #Slider= Scale(root, from_=200, to=10000,tickinterval=50, #orien=HORIZONTAL)
    #Slider.place(relx=0.15,rely=0.06,relwidth=10)
    #Slider.grid(row=1, column=0, columnspan=10)

    TitleLable=Label(root, text='Pick A Gif You Want To Use:\nExtra commands for setting up gifs are at the button\n Note: app requires restart after adding gifs')
    TitleLable.grid(row=0,column=10,columnspan=10)

    openGifButton=Button(root,text='     Set A Up Gif     ',command=lambda: makeGif(root))
    openGifButton.grid(row=125,column=0,columnspan=10,padx=100,pady=100)

    deleteGifButton=Button(root,text='     Delete Gif     ',command=lambda: deleteGif(root))
    deleteGifButton.grid(row=125,column=20,columnspan=10,padx=100,pady=100)

    #openMultiGifButton=Button(root,text='     Set Up Multiple Gifs     ',command=lambda: makeGifs(root))
    #openMultiGifButton.grid(row=125,column=20,columnspan=10,padx=100,pady=100)


    Button1=Button(root,height=gifButtonHeight, width = gifButtonWidth, text=fileNames[numberOfFiles-(numberOfFiles-1)],command=lambda: changeGif(fileNames[numberOfFiles-(numberOfFiles-1)]))
    Button1.grid(row=row,column=column,columnspan=10,padx=gifButtonPadx, pady=gifButtonPady)
    column+=5
    
    Button2=Button(root,height=gifButtonHeight, width = gifButtonWidth, text=fileNames[numberOfFiles-(numberOfFiles)],command=lambda: changeGif(fileNames[numberOfFiles-(numberOfFiles)]))
    Button2.grid(row=row,column=column,columnspan=10,padx=gifButtonPadx,pady=gifButtonPady)
    column+=5
 

    Button3=Button(root,height=gifButtonHeight, width = gifButtonWidth,text=fileNames[numberOfFiles-(numberOfFiles+1)],command=lambda: changeGif(fileNames[numberOfFiles-(numberOfFiles+1)]))
    Button3.grid(row=row,column=column,columnspan=10,padx=gifButtonPadx,pady=gifButtonPady)
    column+=5
 
    if numberOfFiles >3:

        Button4=Button(root,height=gifButtonHeight, width = gifButtonWidth, text=fileNames[numberOfFiles-(numberOfFiles+2)],command=lambda: changeGif(fileNames[numberOfFiles-(numberOfFiles+2)]))

        Button4.grid(row=row,column=column,columnspan=10,padx=gifButtonPadx, pady=gifButtonPady)

        column+=5

    if numberOfFiles >4:
        Button5=Button(root,height=gifButtonHeight, width = gifButtonWidth, text=fileNames[numberOfFiles-(numberOfFiles+3)],command=lambda: changeGif(fileNames[numberOfFiles-(numberOfFiles+3)]))
        Button5.grid(row=row,column=column,columnspan=10,padx=gifButtonPadx,pady=gifButtonPady)
        column+=5
    
    if numberOfFiles >5:
        column = 0
        row = 10
        Button6=Button(root,height=gifButtonHeight, width = gifButtonWidth,text=fileNames[numberOfFiles-(numberOfFiles+4)],command=lambda: changeGif(fileNames[numberOfFiles-(numberOfFiles+4)]))
        Button6.grid(row=row,column=column,columnspan=10,padx=gifButtonPadx,pady=gifButtonPady)
        column+=5

    if numberOfFiles>6:
        Button7=Button(root,height=gifButtonHeight, width = gifButtonWidth,text=fileNames[numberOfFiles-(numberOfFiles+5)],command=lambda: changeGif(fileNames[numberOfFiles-(numberOfFiles+5)]))
        Button7.grid(row=row,column=column,columnspan=10,padx=gifButtonPadx,pady=gifButtonPady)
        column+=5

    if numberOfFiles>7:
        Button8=Button(root,height=gifButtonHeight, width = gifButtonWidth,text=fileNames[numberOfFiles-(numberOfFiles+6)],command=lambda: changeGif(fileNames[numberOfFiles-(numberOfFiles+6)]))
        Button8.grid(row=row,column=column,columnspan=10,padx=gifButtonPadx,pady=gifButtonPady)
        column+=5

    if numberOfFiles>8:
        Button9=Button(root,height=gifButtonHeight, width = gifButtonWidth,text=fileNames[numberOfFiles-(numberOfFiles+7)],command=lambda: changeGif(fileNames[numberOfFiles-(numberOfFiles+7)]))
        Button9.grid(row=row,column=column,columnspan=10,padx=gifButtonPadx,pady=gifButtonPady)
        column+=5

    if numberOfFiles>9:
        Button10=Button(root,height=gifButtonHeight, width = gifButtonWidth,text=fileNames[numberOfFiles-(numberOfFiles+8)],command=lambda: changeGif(fileNames[numberOfFiles-(numberOfFiles+8)]))
        Button10.grid(row=row,column=column,columnspan=10,padx=gifButtonPadx,pady=gifButtonPady)
        column+=5
    

    if numberOfFiles>10:
        column = 0
        row = 15
        Button11=Button(root,height=gifButtonHeight, width = gifButtonWidth,text=fileNames[numberOfFiles-(numberOfFiles+9)],command=lambda: changeGif(fileNames[numberOfFiles-(numberOfFiles+9)]))
        Button11.grid(row=row,column=column,columnspan=10,padx=gifButtonPadx,pady=gifButtonPady)
        column+=5
    
    if numberOfFiles>11:
        Button12=Button(root,height=gifButtonHeight, width = gifButtonWidth,text=fileNames[numberOfFiles-(numberOfFiles+10)],command=lambda: changeGif(fileNames[numberOfFiles-(numberOfFiles+10)]))
        Button12.grid(row=row,column=column,columnspan=10,padx=gifButtonPadx,pady=gifButtonPady)
        column+=5

    if numberOfFiles>12:
        Button12=Button(root,height=gifButtonHeight, width = gifButtonWidth,text=fileNames[numberOfFiles-(numberOfFiles+11)],command=lambda: changeGif(fileNames[numberOfFiles-(numberOfFiles+11)]))
        Button12.grid(row=row,column=column,columnspan=10,padx=gifButtonPadx,pady=gifButtonPady)
        column+=5

    if numberOfFiles>13:
        Button12=Button(root,height=gifButtonHeight, width = gifButtonWidth,text=fileNames[numberOfFiles-(numberOfFiles+12)],command=lambda: changeGif(fileNames[numberOfFiles-(numberOfFiles+12)]))
        Button12.grid(row=row,column=column,columnspan=10,padx=gifButtonPadx,pady=gifButtonPady)
        column+=5

    if numberOfFiles>14:
        Button12=Button(root,height=gifButtonHeight, width = gifButtonWidth,text=fileNames[numberOfFiles-(numberOfFiles+13)],command=lambda: changeGif(fileNames[numberOfFiles-(numberOfFiles+13)]))
        Button12.grid(row=row,column=column,columnspan=10,padx=gifButtonPadx,pady=gifButtonPady)
        column+=5
    
    

    root.mainloop()
    



main()