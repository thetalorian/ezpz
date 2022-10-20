from typing import Type
from PIL import Image, ImageTk

from .widget import Widget
from ..ezpzVector2 import Vector2
from ..contexts import Context, Anchor

class Thumbnail(Widget):
    def __init__(self, id, canvas: Type['EZPZCanvas'], context: Context = Context.WORLD, anchor: Anchor = Anchor.C):
        super().__init__(id, canvas, context, anchor)
        self.__image = ""
        self.__text = ""
        self.__font = {}
        self.__font['face'] = "Arial"
        self.__font['scaled'] = 20
        self.__font['size']= 20
        self.__font['style'] = "bold"
        self.__scale = Vector2(100)
        self.__textpadding = 5
        #self.addHandle("1")

    @property
    def matchScale(self) -> bool:
        return self.__scale == self._canvas.getScale(self._context)


    def setText(self, text):
        self.__text = text

    @property
    def font(self):
        return f"{self.__font['face']} {str(self.__font['scaled'])} {self.__font['style']}"

    def setFont(self, face="", size=0, style=""):
        if face:
            self.__font['face'] = face
        if size:
            self.__font['size'] = size
            self.__font['scaled'] = int(size * (self.__scale.x / 100))
        if style:
            self.__font['style'] = style

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
        self.__font['scaled'] = int(self.__font['size'] * (self.__scale.x / 100))

    def render(self):
        if not self.matchScale:
            self.rescale()

        loc = self._canvas.toScreen(self.apos, self.context, self.anchor)
        (x, y) = (loc.x, loc.y)
        self._canvas.create_image(x, y, image=self.__img, tags=self._id)
        if self.__text:
            textoffset = self.__img.height() / 2 + self.__font['scaled'] / 2 + (self.__textpadding * self.__scale.y / 100)
            self._canvas.create_text(x, y + textoffset, text=self.__text, font=self.font,  tags=self._id)

    @property
    def size(self) -> Vector2:
        (width, height) = self.__image.size
        if self.__text:
            height += self.__font['size'] + self.__textpadding
        return Vector2(width, height)