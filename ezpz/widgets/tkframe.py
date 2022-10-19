from typing import Type
from PIL import Image, ImageTk

from .widget import Widget
from ..ezpzVector2 import Vector2
from ..contexts import Context, Anchor

class TKFrame(Widget):
    def __init__(self, id, canvas: Type['EZPZCanvas'], context: Context = Context.WORLD, anchor: Anchor = Anchor.C):
        super().__init__(id, canvas, context, anchor)
        self.__frame = ""
        self.__size = Vector2(0)

    @property
    def matchScale(self) -> bool:
        return self.__scale == self._canvas.getScale(self.context)


    def setFrame(self, frame):
        self.__frame = frame

    def setSize(self, size):
        # Allow user to override size settings until I can get actual widget size to calculate
        self.__size = size

    def render(self):
        loc = self._canvas.toScreen(self.apos, self.context, self.anchor)
        (x, y) = (loc.x, loc.y)
        self._canvas.create_window(x, y, window=self.__frame, tags=self._id)

    @property
    def size(self) -> Vector2:
        #self._canvas.update_idletasks()
        #return Vector2(self.__frame.winfo_width(), self.__frame.winfo_height())
        return self.__size


        return Vector2(self.__img.width(), self.__img.height())