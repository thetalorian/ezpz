from abc import ABC, abstractmethod
from typing import Type, List
from ..ezpzVector2 import Vector2

class Layout(ABC):
    def __init__(self):
        self._widgetSize = Vector2(0)

    @abstractmethod
    def organize(self, position: Type['Vector2'], items: List):
        pass

    def indexByLoc(loc):
        return -1

    @property
    def size(self):
        return self._widgetSize
