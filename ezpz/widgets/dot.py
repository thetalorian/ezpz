from typing import Type
from .widget import Widget

class Dot(Widget):
    def __init__(self, id, canvas: Type['EZPZCanvas'], screenLock=False):
        super().__init__(id, canvas, invert = False, screenLock=screenLock)
        self.__color = "#000000"

    def setColor(self, color):
        self.__color = color

    def render(self):
        loc = self._canvas.toScreen(self._pos, self.context)
        (x, y) = (loc.x, loc.y)
        self._canvas.create_oval(x -10, y - 10, x + 10, y + 10, fill=self.__color, tags=self._id)
