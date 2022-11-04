import math
from typing import Type, List

from .layout import Layout
from ..ezpzVector2 import Vector2
from ..contexts import Context

class Free(Layout):
    def __init__(self):
        super().__init__()

    def organize(self, position: Type['Vector2'], items: List):
        return super().organize(position, items)

    @property
    def size(self):
        return Vector2(2000)