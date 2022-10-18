from typing import Type
from .widget import Widget

class Dot(Widget):
    def __init__(self, id, canvas: Type['EZPZCanvas'], screenLock=False):
        super().__init__(id, canvas, invert = False, screenLock=screenLock)
        self.__color = "#000000"

    def setColor(self, color):
        self.__color = color

    def render(self):
        if self._screenLock:
            loc = self._pos
        else:
            loc = self._canvas._worldToScreen(self._pos)
        (x, y) = (loc.x, loc.y)
        self._canvas.create_oval(x -10, y - 10, x + 10, y + 10, fill=self.__color, tags=self._id)
        #print(f"{self._id}: {self._id}")