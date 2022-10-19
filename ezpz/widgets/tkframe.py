from typing import Type
from PIL import Image, ImageTk

from .widget import Widget
from ..ezpzVector2 import Vector2
from ..contexts import Context, Anchor

class TKFrame(Widget):
    def __init__(self, id, canvas: Type['EZPZCanvas'], context: Context = Context.WORLD, anchor: Anchor = Anchor.C):
        super().__init__(id, canvas, context, anchor)
        self.__frame = ""

    @property
    def matchScale(self) -> bool:
        return self.__scale == self._canvas.getScale(self.context)


    def setFrame(self, frame):
        self.__frame = frame


    def render(self):
        loc = self._canvas.toScreen(self._pos, self.context, self.anchor)
        (x, y) = (loc.x, loc.y)
        self._canvas.create_window(x, y, window=self.__frame, tags=self._id)

    @property
    def size(self) -> Vector2:
        return Vector2(self.__img.width(), self.__img.height())