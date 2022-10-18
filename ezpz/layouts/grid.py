import math
from typing import Type, List

from .layout import Layout
from ..ezpzVector2 import Vector2
from ..contexts import Context

class Grid(Layout):
    def __init__(self, padding = 10):
        super().__init__()
        self.__padding = padding
        self.__widgetSize = Vector2(0)
        self.__offset = Vector2(0)

    def __getGridShape(self, count):
        rows = math.floor(math.sqrt(count))
        cols = math.ceil(count / rows)
        return Vector2(cols, rows)

    def __getCellSize(self, children):
        size = Vector2(0)
        for item in children:
            if item.size.w > size.w:
                size.w = item.size.w
            if item.size.h > size.y:
                size.h = item.size.h
        return size + self.__padding

    def __getOffset(self):
        self.__offset = self.pos - (self.__widgetSize / 2)

    def organize(self, pos, children):
        gridShape = self.__getGridShape(len(children))
        cellSize = self.__getCellSize(children)
        widgetSize = cellSize * gridShape
        offset = pos - (widgetSize / 2)

        cell = Vector2(0)
        for item in children:
            loc = offset + (cell * cellSize) + (cellSize / 2)
            item.pos = loc
            cell.x += 1
            if cell.x >= gridShape.x:
                cell.x = 0
                cell.y += 1


    def update(self, child, event):
        print(f"Grid updating {child} with {event}")
        #index = self.__items.index(item)
        #print(f"Found index {index}")
        #self.organize()
        #self.refresh()
