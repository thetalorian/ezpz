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
        self.__gridShape = Vector2(0)
        self.__cellSize = Vector2(0)

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


    def organize(self, pos, children):
        self.__gridShape = self.__getGridShape(len(children))
        self.__cellSize = self.__getCellSize(children)
        self._widgetSize = self.__cellSize * self.__gridShape
        offset = Vector2(0) - (self._widgetSize / 2)

        cell = Vector2(0)
        for item in children:
            loc = offset + (cell * self.__cellSize) + (self.__cellSize / 2)
            item.pos = loc
            cell.x += 1
            if cell.x >= self.__gridShape.x:
                cell.x = 0
                cell.y += 1

    def indexByLoc(self, loc):
        offset = Vector2(0) - (self._widgetSize / 2)
        cell = Vector2(-1)
        for i in range(0, self.__gridShape.x):
            left = offset.x + self.__cellSize.x * i
            right = offset.x + self.__cellSize.x * (i + 1)
            if left < loc.x and loc.x <= right:
                cell.x = i
                break

        for i in range(0, self.__gridShape.y):
            top = offset.y + self.__cellSize.y * i
            bottom = offset.y + self.__cellSize.y * (i + 1)
            if top < loc.y <= bottom:
                cell.y = i
                break

        if cell.x != -1 and cell.y != -1:
            index = cell.x + cell.y * self.__gridShape.x
        else:
            index = -1

        return index

    # def update(self, child, loc):
    #     print(f"Grid updating {child} with {loc}")
    #     cell = self.getCellbyLoc(loc)
    #     print(f"Found cell: {cell}")
    #     if cell.x != -1 and cell.y != -1:
    #         print("It's on the grid")
    #         index = cell.x + cell.y * self.__gridShape.x
    #         print(f"Updating item {child} with {index}")


        #index = self.__items.index(item)
        #print(f"Found index {index}")
        #self.organize()
        #self.refresh()
