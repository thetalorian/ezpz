from typing import Type
from ..ezpzVector2 import Vector2
from .coord import Coord
from ..contexts import Context

class Button:
    def __init__(
        self,
        id: str,
        canvas: Type['Canvas'],
        context: Context = Context.WORLD
    ):
        super().__init__(id, canvas)
        self._context: Context = context
        self._layout: Type['Widget'] = ""
        self._canvas.tag_bind(self._id, '<ButtonPress-1>', self.activate)

    def activate(self, _):
        print(f"Activating {self._id}")
        if self._callback:
            self._callback()

    def setCallback(self, callback):
        self._callback = callback

