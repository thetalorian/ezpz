from dataclasses import dataclass
from typing import Type

@dataclass
class Vector2:
    x: int
    y: int

    def __init__(self, *args):
        if len(args) > 1:
            self.x = args[0]
            self.y = args[1]
        else:
            self.x = args[0]
            self.y = args[0]

    def __add__(self, other) -> Type['Vector2']:
        if isinstance(other, Vector2):
            return Vector2(self.x + other.x, self.y + other.y)
        else:
            return Vector2(self.x + other, self.y + other)

    def __sub__(self, other) -> Type['Vector2']:
        if isinstance(other, Vector2):
            return Vector2(self.x - other.x, self.y - other.y)
        else:
            return Vector2(self.x - other, self.y - other)

    def __mul__(self, other) -> Type['Vector2']:
        if isinstance(other, Vector2):
            return Vector2(self.x * other.x, self.y * other.y)
        else:
            return Vector2(self.x * other, self.y * other)

    __rmul__ = __mul__

    def __truediv__(self, other) -> Type['Vector2']:
        if isinstance(other, Vector2):
            return Vector2(self.x / other.x, self.y / other.y)
        else:
            return Vector2(self.x / other, self.y / other)

    def __div__(self, other) -> Type['Vector2']:
        if isinstance(other, Vector2):
            return Vector2(self.x // other.x, self.y // other.y)
        else:
            return Vector2(self.x // other, self.y // other)


    def clamp(self, _min, _max):
        self.x = max(min(self.x, _max), _min)
        self.y = max(min(self.y, _max), _min)

    def toList(self):
        return [self.x, self.y]

    def __repr__(self):
        return f"({self.x}, {self.y})"

    @property
    def w(self) -> int:
        return self.x

    @w.setter
    def w(self, _w: int):
        self.x = _w

    @property
    def h(self) -> int:
        return self.y

    @h.setter
    def h(self, _h: int):
        self.y = _h

