import math
from typing import Type, List

from .layout import Layout
from ..ezpzVector2 import Vector2
from ..contexts import Context

class Column(Layout):
    def __init__(self, padding = 10):
        super().__init__()
        self.__padding = padding

    def __getWidgetSize(self, children):
        size = Vector2(0)
        for item in children:
            size.h += item.size.h + self.__padding
            if item.size.w > size.w:
                size.w = item.size.w
        size.h += self.__padding * (len(children) - 1)
        self._widgetSize = size


    def organize(self, pos, children):
        self.__getWidgetSize(children)
        offset = Vector2(0) - (self._widgetSize / 2)

        for item in children:
            loc = offset + Vector2(self._widgetSize.w / 2, item.size.h / 2)
            offset += Vector2(0, item.size.h + self.__padding)
            item.pos = loc


    def update(self, child, event):
        print(f"Grid updating {child} with {event}")
