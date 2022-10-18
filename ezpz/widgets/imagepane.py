from typing import Type
from PIL import Image, ImageTk

from .widget import Widget
from ..ezpzVector2 import Vector2
from ..contexts import Context

class ImagePane(Widget):
    def __init__(self, id, canvas: Type['EZPZCanvas'], context: Context = Context.WORLD):
        super().__init__(id, canvas, context)
        self.__image = ""
        self.__scale = Vector2(1)

    @property
    def matchScale(self) -> bool:
        return self.__scale == self._canvas.getScale(self.context)
        

    def setImage(self, image):
        print("DDImage set Image")
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
        if not self.matchScale:
            self.rescale()
        loc = self._canvas.toScreen(self._pos, self.context)

        # if self._context == Context.WORLD:
        #     loc = self._canvas._worldToScreen(self._pos)
        # else:
        #     loc = self._pos
        (x, y) = (loc.x, loc.y)
        self._canvas.create_image(x, y, image=self.__img, tags=self._id)
        #print(f"{self._id}: {self._id}")