from typing import Type
from PIL import Image, ImageTk

from .widget import Widget
from ..ezpzVector2 import Vector2
from ..contexts import Context, Anchor

class Label(Widget):
    def __init__(self, id, canvas: Type['EZPZCanvas'], context: Context = Context.WORLD, anchor: Anchor = Anchor.C):
        super().__init__(id, canvas, context, anchor)
        self.__text = ""
        self.__font = {}
        self.__font['face'] = "Arial"
        self.__font['size']= 20
        self.__font['scaled'] = 20
        self.__font['style'] = "bold"
        self.__scale = Vector2(100)

    def setText(self, text):
        self.__text = text

    @property
    def matchScale(self) -> bool:
        return self.__scale == self._canvas.getScale(self._context)

    @property
    def font(self):
        return f"{self.__font['face']} {str(self.__font['scaled'])} {self.__font['style']}"

    def rescale(self):
        self.__scale = self._canvas.getScale(self._context)
        self.__font['scaled'] = int(self.__font['size'] * (self.__scale.x / 100))


    def setFont(self, face="", size=0, style=""):
        if face:
            self.__font['face'] = face
        if size:
            self.__font['size'] = size
            self.__font['scaled'] = int(size * (self.__scale.x / 100))
        if style:
            self.__font['style'] = style

    def render(self):
        if not self.matchScale:
            self.rescale()
        
        loc = self._canvas.toScreen(self.apos, self.context, self.anchor)
        (x, y) = (loc.x, loc.y)
        self._canvas.create_text(x, y, text=self.__text, font=self.font,  tags=self._id)

    @property
    def size(self) -> Vector2:
        return Vector2(len(self.__text) * self.__font['size'], self.__font['size'])
