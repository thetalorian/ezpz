import tkinter as tk
import uuid

from .canvas import Canvas

class Window(tk.Tk):
    def __init__(self):
        super().__init__()
        self._canvas = Canvas(self, width=500, height=500)
        self.grid_columnconfigure(0, weight=1)
        self.grid_rowconfigure(0, weight=1)
        self._canvas.grid(row=0, column=0, sticky=tk.NSEW)


    def start(self):
        self.mainloop()

if __name__=="__main__":
    Window()