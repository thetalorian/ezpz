from abc import ABC, abstractmethod
from typing import Type
from ..ezpzVector2 import Vector2

class Coord(ABC):
    def __init__(
        self,
        id: str,
        canvas: Type['Canvas'],
    ):
        self._id: str = id
        self._canvas = canvas
        self._pos: Vector2 = Vector2(0)
        self._ref: Vector2 = Vector2(0)

    #@abstractmethod
    def activate(self, _):
        pass

    def pin(self, event: Vector2):
        self._ref = event

    #@abstractmethod
    def drag(self, event: Vector2, scale: Vector2):
        pass

    #@abstractmethod
    def drop(self, event: Vector2):
        pass

    @property
    def pos(self) -> Vector2:
        return self._pos

    @pos.setter
    def pos(self, _pos: Vector2):
        self._pos = _pos

    @property
    def id(self) -> str:
        return self._id

    @property
    def x(self) -> int:
        return self._pos.x

    @property
    def y(self) -> int:
        return self._pos.y

    @property
    def ref(self) -> Vector2:
        return self._ref

    @property
    def size(self) -> Vector2:
        return Vector2(0)

    def __repr__(self) -> str:
        return self._id

    def __eq__(self, other) -> bool:
        return other == self._id
