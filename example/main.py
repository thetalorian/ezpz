import tkinter as tk
import uuid
from appWindow import AppWindow

class app:
    def __init__(self):
        window = AppWindow()
        imgpath = "test.jpg"
        print("App base")
        window.showDots()
        #window.showThumbs()
        #window.showFrameWindow()
        #window.setImage(imgpath)
        window.start()

if __name__=="__main__":
    app()
