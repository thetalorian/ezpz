from operator import invert
from typing import Type
from ..ezpzVector2 import Vector2
from .coord import Coord
from ..contexts import Context
from .widget import Widget
from .handle import Handle

class Waypoint(Widget):
    def __init__(
        self,
        id: str,
        canvas: Type['Canvas'],
        context: Context = Context.WORLD
    ):
        super().__init__(id, canvas, context)
        self._handle = Handle(self, "2", invert=True)
        self.canvas.bind("<ButtonPress-2>", self._handle.grab)
#        self._canvas.bind('<ButtonPress-2>', self.pin)
#        self._canvas.bind('<B2-Motion>', self.drag)
        #self._canvas.bind('<B2-Motion>', lambda event, ref=self: self._canvas.grabWidget(event, ref))
        #self._canvas.bind("<ButtonPress-2>", lambda event, ref=self: self._canvas.__grabWidget(event, ref))
        #self._canvas.bind("<B2-Motion>", lambda event, ref=self: self._canvas.__dragWidget(event, ref))

    # def activate(self, _):
    #     print(f"Activating {self._id}")

    # def setLayout(self, layout):
    #     self.__layout = layout

    # def pin(self, event):
    #     print(f"Pinning {self}")
    #     #self._ref = event
    #     self._ref = Vector2(event.x, event.y)

    # def drag(self, event):
    #     print(f"Dragging {self} {event}")
    #     if self._context == Context.SCREEN:
    #         scale = 100
    #     else:
    #         scale = self._canvas.scale
    #     self._pos += ((self._ref - Vector2(event.x, event.y)) / (scale / 100))
    #     self.pin(event)
    #     self._canvas._refresh()

    # def drop(self, event: Vector2):
    #     pass

    # @property
    # def pos(self) -> Vector2:
    #     return self._pos

    # @pos.setter
    # def pos(self, _pos: Vector2):
    #     # print(f"Setting pos at {_pos}")
    #     self._pos = _pos

    # @property
    # def id(self) -> str:
    #     return self._id

    # @property
    # def x(self) -> int:
    #     return self._pos.x

    # @property
    # def y(self) -> int:
    #     return self._pos.y

    # @property
    # def ref(self) -> Vector2:
    #     return self._ref

    # @property
    # def size(self) -> Vector2:
    #     return Vector2(0)

    # def render(self):
    #     pass

    # def __repr__(self) -> str:
    #     return self._id

    # def __eq__(self, other) -> bool:
    #     return other == self._id
