from typing import Type
from PIL import Image, ImageTk

from .widget import Widget
from ..ezpzVector2 import Vector2
from ..contexts import Context

class Container(Widget):
    def __init__(self, id, canvas: Type['EZPZCanvas'], context: Context = Context.WORLD):
        super().__init__(id, canvas, context)
        self.layout = ""


    def render(self):
        super().render()


    @property
    def size(self) -> Vector2:
        if self.layout:
            return self.layout.size
        return Vector2(0)