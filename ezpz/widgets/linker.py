from typing import Type
from PIL import Image, ImageTk

from .widget import Widget
from ..ezpzVector2 import Vector2
from ..contexts import Context, Anchor

class Linker(Widget):
    def __init__(self, id, canvas: Type['EZPZCanvas'], context: Context = Context.WORLD, anchor: Anchor = Anchor.C):
        super().__init__(id, canvas, context, anchor)
        self.__color = "#000000"

    def setColor(self, color):
        self.__color = color


    def render(self):
        polygon = []
        for child in self.children:
            cloc = self._canvas.toScreen(child.apos, child.context, child.anchor)
            polygon.append(cloc.x)
            polygon.append(cloc.y)

        self._canvas.create_polygon(polygon, outline=self.__color, fill='', width=2)
        super().render()

    def childUpdated(self, child, event):
        print(f"Updating child for {self._id}")
        if self.updatecall:
            print(f"I've got a method...")
            points = []
            for child in self.children:
                points.append([child.pos.x, child.pos.y])
            self.updatecall(points)
        self.refresh()

    @property
    def size(self) -> Vector2:
        if self.layout:
            return self.layout.size
        return Vector2(0)


