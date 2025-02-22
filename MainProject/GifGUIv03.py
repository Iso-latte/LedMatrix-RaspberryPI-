from MainProject.GifHander import GifHandler
from tkinter import *
from tkinter import filedialog
from MainProject.LEDGifController import MainMatrix
import os
import sys

matrix = MainMatrix()
root = Tk()

def deleteGif(root):
    root.filename = filedialog.askopenfilename(title="select a gif", filetypes=[("Gif Files","*.gif")], initialdir="./Assets/Gifs")#
    Gif = GifHandler(root.filename)
    Gif.deleteGif(root.filename)
    return root.filename

def makeGifs(root):
    root.filename = filedialog.askopenfilenames(title="select a gif", filetypes=[("Gif Files","*.gif")])#
    list = []
    list.append(root.filename)
    print(list)


def makeGif(root):
    root.filename = filedialog.askopenfilename(title="select a gif", filetypes=[("Gif Files","*.gif")],initialdir="./Assets/Gifs")#
    Gif = GifHandler(root.filename)
    Gif.setUpGif()
    
def changeGif(filename):
    matrix.stop_event.set()
    if matrix.animation_thread and matrix.animation_thread.is_alive():
        matrix.animation_thread.join()  # Wait for the current animation to stop.
    matrix.stop_event.clear()
    matrix.simulateLED(filename)
        
def getFileNamesWithoutEx():
    listOfNames=[]
    for names in os.listdir('./Assets/Gifs'):
        nameOfGif = names.replace('.gif',"")
        listOfNames.append(nameOfGif)
    return listOfNames


def getFileNamesWithEx():
    listOfNames=[]
    for names in os.listdir('./Assets/Gifs'):
        nameOfGif = names
        listOfNames.append(nameOfGif)
    return listOfNames

def on_closing():
    matrix.stop_animation()  # Stop any running animation
    sys.exit(0)  # Exit the program cleanly

def main():

    fileNames = getFileNamesWithoutEx()
    row = 5

    gifButtonPady = 25
    gifButtonPadx = 100
    gifButtonHeight = 4
    gifButtonWidth = 15
    root.title("Gif GUI")
    root.minsize(width=1050,height=600)
    root.maxsize(width=1050,height=600)
    root.resizable(False,False)


    TitleLable=Label(root, text='Pick A Gif You Want To Use:\nExtra commands for setting up gifs are at the button\n Note: app requires restart after adding gifs')
    TitleLable.grid(row=0,column=10,columnspan=10)

    deleteGifButton=Button(root,text='     Delete Gif     ',command=lambda: deleteGif(root))
    deleteGifButton.grid(row=125,column=10,columnspan=10,padx=100,pady=100)

    for i, fileName in enumerate(fileNames):
        row, col = divmod(i, 5)  # Arrange buttons in rows of 5
        Button(root, height=gifButtonHeight, width=gifButtonWidth, text=fileName,
            command=lambda fn=fileName: changeGif(fn)).grid(row=row + 5, column=col * 5,
                                                            columnspan=10, padx=gifButtonPadx, pady=gifButtonPady)
    
    root.protocol("WM_DELETE_WINDOW", on_closing)
    root.mainloop()
