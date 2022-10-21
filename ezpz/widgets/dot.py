from typing import Type
from .widget import Widget
from ..contexts import Context, Anchor

class Dot(Widget):
    def __init__(self, id, canvas: Type['EZPZCanvas'], context: Context = Context.WORLD, anchor: Anchor = Anchor.C):
        super().__init__(id, canvas, context, anchor)
        self.__color = "#000000"

    def setColor(self, color):
        self.__color = color

    def render(self):
        loc = self._canvas.toScreen(self.apos, self.context)
        (x, y) = (loc.x, loc.y)
        self._canvas.create_oval(x -10, y - 10, x + 10, y + 10, fill=self.__color, tags=self._id)
