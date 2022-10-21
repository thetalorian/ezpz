from operator import indexOf
from typing import Type
from ..ezpzVector2 import Vector2
from .coord import Coord
from ..contexts import Context, Anchor
from .handle import Handle
from ..layouts.free import Free

class Widget:
    def __init__(
        self,
        id: str,
        canvas: Type['Canvas'],
        context: Context = Context.WORLD,
        anchor: Anchor = Anchor.C
    ):
        self._id: str = id
        self._parent: Widget = ""
        self._canvas = canvas
        self._pos: Vector2 = Vector2(0)
        self._context: Context = context
        self._anchor: Anchor = anchor
        self.__children = []
        self.layout = Free()
        self.__update = ""

        # Ok, that was actually a big mistake.
        # I'm conflating self.layout to mean both the layout assigned to this widget,
        # as in the way its children will be handled, and the layout assigned to this
        # widget, as in the way it is handled as part of that collection.

        # I'm getting to the point where there are way to many cross references.
        # A layout has a parent widget, that it is assigned to, and a list of widgets
        # that it controls, but at the moment it looks like I also need to add
        # a parent widget to the list as well.

        # Honestly it may be cleaner across the board to assume that all widgets get
        # children, moving the item CRUD functions to the widget code itself and have the layout
        # just be responsible for resetting the positions of the children in relation to the parent.

        # Then, instead of checking to see if a widget has a layout when it is dropped, we
        # just check to see if its parent does, and if so we call that parent's reorder function,
        # which will just depend on the assigned layout.

        # There are still cross references, we would need to assign each widget's parent as we
        # add the widget to the parent's list, which is a bit ugly, but at least we aren't trying
        # to do the same for the layouts.
    @property
    def children(self):
        return self.__children

    @property
    def updatecall(self):
        return self.__update

    def addHandle(self, button: str, invert: bool=False):
        self._handle = Handle(self, button, invert)

    def bind(self, key: str, callback):
        self._canvas.bind(key, callback)

    def tag_bind(self, key: str, callback):
        self._canvas.tag_bind(self._id, key, callback)

    def setUpdate(self, callback):
        self.__update = callback

    def setLayout(self, layout):
        self.layout = layout

    def setParent(self, widget):
        self._parent = widget

    def add(self, widget):
        self.__children.append(widget)
        widget.setParent(self)
        self.layout.organize(self._pos, self.__children)
        if self._parent:
            self._parent.refresh()

    def refresh(self):
        self.layout.organize(self._pos, self.__children)

    def clear(self):
        self.__children.clear()

    def update(self, event):
        if self._parent:
            print(f"Updating {self._id}")
            self._parent.childUpdated(self, event)
        self._canvas._refresh()

    def childUpdated(self, child, event):
        print(f"Updating child for {self._id}")
        if self.__update:
            print(f"I've got a method...")
            loc = self._canvas.toContext(Vector2(event.x, event.y), self._context)
            i1 = self.__children.index(child)
            i2 = self.layout.indexByLoc(loc)
            self.__update(self, i1, i2)
        self.refresh()

    def moveBefore(self, i1, i2):
        mover = self.__children.pop(i1)
        t = i2 if i2 <= i1 else i2 - 1
        self.__children.insert(t, mover)

    def render(self):
        for item in self.__children:
            item.render()




    # def grab(self, event):
    #     self._canvas.bind('<B1-Motion>', self.drag)
    #     self._canvas.bind('<ButtonRelease-1>', self.drop)
    #     self.pin(event)

    # def pin(self, event):
    #     print(f"Pinning {self}")
    #     self._ref = Vector2(event.x, event.y)

    # #def drag(self, event: Vector2, scale: Vector2):
    # def drag(self, event):
    #     print(f"Dragging {self} {event}")
    #     if self._context == Context.SCREEN:
    #         scale = 100
    #     else:
    #         scale = self._canvas.scale
    #     #self._pos += ((self._ref - event) / scale) * self._invert
    #     self._pos -= ((self._ref - Vector2(event.x, event.y)) / (scale / 100))
    #     self.pin(event)
    #     self._canvas._refresh()

    # def drop(self, event):
    #     print(f"Dropping {self._id}")
    #     self._canvas.bind('<B1-Motion>', '')
    #     self._canvas.bind('<ButtonRelease-1>', '')

    def dropped(self, event):
        print(f"I've been dropped {self} {self.layout}")
        if self.layout:
            self.layout.updateItem(self, event)

    @property
    def pos(self) -> Vector2:
        return self._pos

    @pos.setter
    def pos(self, _pos: Vector2):
        # print(f"Setting pos at {_pos}")
        self._pos = _pos

    @property
    def canvas(self):
        return self._canvas

    @property
    def context(self):
        return self._context

    @property
    def anchor(self):
        return self._anchor

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

    def __len__(self):
        return len(self.__children)

    @property
    def apos(self) -> Vector2:
        if self._parent:
            return self.pos + self._parent.apos
        return self.pos
