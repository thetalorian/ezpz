from typing import Type
from PIL import Image, ImageTk

from .widget import Widget
from ..ezpzVector2 import Vector2
from ..contexts import Context, Anchor

class ImagePane(Widget):
    def __init__(self, id, canvas: Type['EZPZCanvas'], context: Context = Context.WORLD, anchor: Anchor = Anchor.C):
        super().__init__(id, canvas, context, anchor)
        self.__image = ""
        self.__scale = Vector2(1)

    @property
    def matchScale(self) -> bool:
        return self.__scale == self._canvas.getScale(self.context)


    def setImage(self, image):
        self.__image = image
        self.rescale()

    def rescale(self):
        self.__scale = self._canvas.getScale(self._context)
        (w, h) = self.__image.size
        scaled = Vector2(w, h) * (self.__scale / 100)
        #print(f"Size: ({w}, {h}) Scaled: {scaled}")
        resized = self.__image.resize((int(scaled.x), int(scaled.y)))
        self.__img = ImageTk.PhotoImage(resized)


    def render(self):
        if self.__image:
            if not self.matchScale:
                self.rescale()
            loc = self._canvas.toScreen(self.apos, self.context, self.anchor)
            (x, y) = (loc.x, loc.y)
            self._canvas.create_image(x, y, image=self.__img, tags=self._id)

    @property
    def size(self) -> Vector2:
        (w, h) = self.__image.size
        return Vector2(w, h)