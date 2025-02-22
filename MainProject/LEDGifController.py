import time
import RPi.GPIO as GPIO
from rgbmatrix import RGBMatrix, RGBMatrixOptions
from PIL import Image
from MainProject.GifHander import GifHandler
import threading


class MainMatrix:

    def __init__(self):
        self.options = RGBMatrixOptions()
        self.options.rows=32 #number of rows
        self.options.cols = 32 #number of columns
        self.options.multiplexing = 0
        self.options.chain_length = 1  #number of boards connected
        self.options.parallel=1 #Num of paralel chains
        self.options.hardware_mapping = 'adafruit-hat' #mapping gpio pins to already configured
        self.options.brightness = 100#default 100
        self.options.gpio_slowdown = 2
        self.options.inverse_colors= False
        self.options.drop_privileges = 0
        self.matrix = RGBMatrix(options = self.options)
        self.animation_thread = None
        self.stop_event = threading.Event()

    def simulateLED(self, filename):
        gif = Image.open("./Assets/Gifs/"+filename+".gif")
        num_frames = gif.n_frames
        canvases = []
        for frame_index in range(0,num_frames):
            gif.seek(frame_index)
            frame = gif.copy()
            frame = frame.resize((self.options.cols, self.options.rows), Image.ANTIALIAS)
            canvas = self.matrix.CreateFrameCanvas()
            canvas.SetImage(frame.convert("RGB"))
            canvases.append(canvas)
        gif.close()

        def display_frames():
            frame = 0
            boolean = True
            while not self.stop_event.is_set():
                self.matrix.SwapOnVSync(canvases[frame])
                time.sleep(0.1)
                if frame == num_frames-1:
                    frame = 0
                else:
                    frame +=1
            self.matrix.Clear()

        self.animation_thread = threading.Thread(target=display_frames)
        self.animation_thread.start()

    def stop_animation(self):
        self.stop_event.set()  # Trigger the stop event to stop the animation