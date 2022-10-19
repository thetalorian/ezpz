import math
from typing import Type, List

from .layout import Layout
from ..ezpzVector2 import Vector2
from ..contexts import Context

class Row(Layout):
    def __init__(self, padding = 10):
        super().__init__()
        self.__padding = padding

    def __getWidgetSize(self, children):
        size = Vector2(0)
        for item in children:
            size.w += item.size.w
            if item.size.h > size.h:
                size.h = item.size.h
        size.w += self.__padding * (len(children) - 1)
        self._widgetSize = size


    def organize(self, pos, children):
        self.__getWidgetSize(children)
        offset = Vector2(0) - (self._widgetSize / 2)

        for item in children:
            loc = offset + Vector2(item.size.w / 2, self._widgetSize.h / 2)
            offset += Vector2(item.size.w + self.__padding, 0)
            item.pos = loc


    def update(self, child, event):
        print(f"Grid updating {child} with {event}")
