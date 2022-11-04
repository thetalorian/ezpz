import logging
from typing import Type
from PIL import Image, ImageTk

from .widget import Widget
from ..ezpzVector2 import Vector2
from ..contexts import Context, Anchor

class BoxImage(Widget):
    def __init__(self, id, canvas: Type['EZPZCanvas'], context: Context = Context.WORLD, anchor: Anchor = Anchor.C):
        super().__init__(id, canvas, context, anchor)
        self.__image = None
        self.__scale = Vector2(100)
        self.__boxSize = Vector2(1)
        self.__rotation = 0
        self.__text = ""
        self.__font = {}
        self.__font['face'] = "Arial"
        self.__font['scaled'] = 20
        self.__font['size']= 20
        self.__font['style'] = "bold"
        self.__textpadding = 5

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


    @property
    def matchScale(self) -> bool:
        return self.__scale == self._canvas.getScale(self.context)


    @property
    def size(self) -> Vector2:
        if self.rotation in [90, 270]:
            return Vector2(self.boxSize.y, self.boxSize.x)
        return self.boxSize

    @property
    def boxSize(self) -> Vector2:
        return self.__boxSize

    @boxSize.setter
    def boxSize(self, value: Vector2) -> None:
        self.__boxSize = value
        self.fixImage()


    @property
    def rotation(self) -> int:
        return self.__rotation

    @rotation.setter
    def rotation(self, value: int) -> None:
        self.__rotation = value
        self.fixImage()


    def setImage(self, image):
        self.__image = image
        self.fixImage()

    def fixImage(self):
        if self.__image:
            self.__fixedimage = self.__image.rotate(self.rotation, expand=1).resize((self.size.x, self.size.y))
            self.rescale()



    def rescale(self):
        self.__scale = self._canvas.getScale(self._context)
        if self.__image:
            (w, h) = self.__fixedimage.size
            scaled = Vector2(w, h) * (self.__scale / 100)
        #print(f"Size: ({w}, {h}) Scaled: {scaled}")
            resized = self.__fixedimage.resize((int(scaled.x), int(scaled.y)))
            self.__img = ImageTk.PhotoImage(resized)


    def render(self):
        if not self.matchScale:
            self.rescale()
        loc = self._canvas.toScreen(self.apos, self.context, self.anchor)
        (x, y) = (loc.x, loc.y)
        if self.__image:
            self._canvas.create_image(x, y, image=self.__img, tags=self._id)
            filler=""
        else:
            filler="#242464"
        boxSize = self.size * (self.__scale / 100) / 2
        self._canvas.create_rectangle(loc.x - boxSize.x, loc.y - boxSize.y, loc.x + boxSize.x, loc.y + boxSize.y, width=5, fill=filler, tags=self._id)
        if self.__text:
            textoffset = 0
            #textoffset = self.__img.height() / 2 + self.__font['scaled'] / 2 + (self.__textpadding * self.__scale.y / 100)
            self._canvas.create_text(x, y + textoffset, text=self.__text, font=self.font,  tags=self._id, angle=self.__rotation)


#        self._canvas.create_text(loc.x, loc.y, text="HELLO WORLD", fill="#000000", font=('Helvetica 17 bold'), angle=self.__rotation)
#        self._canvas.create_text(loc.x, loc.y, text="HELLO WORLD", fill="#DDDDDD", font=('Helvetica 15 bold'), angle=self.__rotation)
