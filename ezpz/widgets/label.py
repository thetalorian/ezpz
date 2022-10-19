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
        self.__font['style'] = "bold"

    def setText(self, text):
        self.__text = text

    @property
    def font(self):
        return f"{self.__font['face']} {str(self.__font['size'])} {self.__font['style']}"

    def setFont(self, face="", size=0, style=""):
        if face:
            self.__font['face'] = face
        if size:
            self.__font['size'] = size
        if style:
            self.__font['style'] = style

    def render(self):
        loc = self._canvas.toScreen(self._pos, self.context, self.anchor)
        (x, y) = (loc.x, loc.y)
        self._canvas.create_text(x, y, text=self.__text, font=self.font,  tags=self._id)

    @property
    def size(self) -> Vector2:
        return len(self.__text)
        # NOTE: Not sure yet how to properly calculate size of text on screen.