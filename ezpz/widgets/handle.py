from typing import Type
from ..ezpzVector2 import Vector2
from .coord import Coord
from ..contexts import Context

class Handle():
    # Handle class gives widgets drag and drop abilities

    def __init__(
        self,
        widget: Type['Widget'],
        button: str,
        invert: bool = False
    ):
        self._widget = widget
        self._inversion = -1 if invert else 1
        self._button = button
        self._widget.canvas.tag_bind(self._widget.id, f"<ButtonPress-{button}>", self.grab)
        self._ref = Vector2(0)


    def grab(self, event):
        self._widget.canvas.bind(f"<B{self._button}-Motion>", self.drag)
        self._widget.canvas.bind(f"<ButtonRelease-{self._button}>", self.drop)
        self.pin(event)

    def pin(self, event):
        self._ref = Vector2(event.x, event.y)

    def drag(self, event):
        if self._widget.context == Context.SCREEN:
            scale = 100
        else:
            scale = self._widget.canvas.getScale(self._widget.context)
        self._widget.pos -= ((self._ref - Vector2(event.x, event.y)) / (scale / 100)) * self._inversion
        self.pin(event)
        self._widget.canvas._refresh()

    def drop(self, event):
        self._widget.canvas.bind(f"<B{self._button}-Motion>", '')
        self._widget.canvas.bind(f"<ButtonRelease-{self._button}>", '')
        self._widget.update(event)

