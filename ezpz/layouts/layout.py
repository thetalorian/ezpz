from abc import ABC, abstractmethod
from typing import Type, List

class Layout(ABC):

    @abstractmethod
    def organize(self, position: Type['Vector2'], items: List):
        pass

    def update(self, child, event):
        pass