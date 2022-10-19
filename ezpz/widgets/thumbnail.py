from typing import Type
from PIL import Image, ImageTk

from .widget import Widget
from ..ezpzVector2 import Vector2
from ..contexts import Context, Anchor

class Thumbnail(Widget):
    def __init__(self, id, canvas: Type['EZPZCanvas'], context: Context = Context.WORLD, anchor: Anchor = Anchor.C):
        super().__init__(id, canvas, context, anchor)
        self.__image = ""
        self.__scale = Vector2(100)
        self.addHandle("1")

    @property
    def matchScale(self) -> bool:
        return self.__scale == self._canvas.getScale(self._context)

    def setImage(self, image):
        (w, h) = image.size
        if w > h:
            ratio = float(h)/w
            scale = Vector2(100, 100 * ratio)
        else:
            ratio = float(w)/h
            scale = Vector2(100 * ratio, 100)
        self.__image = image.resize((int(scale.x), int(scale.y)))
        self.rescale()

    def rescale(self):
        self.__scale = self._canvas.getScale(self._context)
        (w, h) = self.__image.size
        scaled = Vector2(w, h) * (self.__scale / 100)
        #print(f"Size: ({w}, {h}) Scaled: {scaled}")
        resized = self.__image.resize((int(scaled.x), int(scaled.y)))
        self.__img = ImageTk.PhotoImage(resized)

    def render(self):
        print(f"Rendering thumbnail {self}")
        if not self.matchScale:
            self.rescale()

        loc = self._canvas.toScreen(self.apos, self.context, self.anchor)
        (x, y) = (loc.x, loc.y)
        self._canvas.create_image(x, y, image=self.__img, tags=self._id)
        #print(f"{self._id}: {self._id}")

    @property
    def size(self) -> Vector2:
        return Vector2(100, 100)