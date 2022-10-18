import tkinter as tk
import uuid
from PIL import Image, ImageTk

from .widgets.waypoint import Waypoint
from .widgets.thumbnail import Thumbnail
from .widgets.widget import Widget
from .widgets.dot import Dot
from .widgets.imagepane import ImagePane
from .ezpzVector2 import Vector2
from .contexts import Context

class Canvas(tk.Canvas):
    def __init__(self, container, width, height):
        super().__init__(container, width=width, height=height, bg='#222222')
        self.__container = container
        self.__center = Vector2(width/2, height/2)
        self.__canvassize = Vector2(width, height)
        self.__scale = Vector2(100)
        
        self.__container.update_idletasks()
        self.__offset = Waypoint("offset", self)
        self.__items = []
        self.__setBindings()

    def __setBindings(self):
        self.bind("<MouseWheel>", self.__changeScale)
        self.bind("<Configure>", self.__recalibrate)
        self.bind("<Double-ButtonPress-2>", self.__recenter)
        self.bind("<ButtonPress-3>", self.__resize)

    def __recalibrate(self, _):
        self.__container.update_idletasks()
        self.__center = Vector2(self.winfo_width()/2, self.winfo_height()/2)
        #print(f"Re-centering to: {self.__center}")
        self._refresh()

    def __recenter(self, _):
        self.__offset.pos = Vector2(0)
        self._refresh()

    def __resize(self, event):
        self.__changeScale(event, scale=100)
        self._refresh()

    def setImage(self, image):
        print(f"Canvas set image")
        self.__container.update_idletasks()
        self.__items['image'].setImage(image)
        self._refresh()
        #self.centerImage()

    def addItem(self, item):
        self.__offset.add(item)
        #self.__items.append(item)
        # id = uuid.uuid1()
        # item = DDPoint(id, self)
        # self.__items[item.id] = item
        self._refresh()

    def clearItems(self):
        self.__offset.clear()
        #self.__items.clear()
        self._refresh()

    def reset(self):
        self.clearItems()
        self.__recenter("")
        self.__resize("")

    def _refresh(self):
        self.delete('all')
        self.__offset.render()

    def __changeScale(self, event, scale=""):
        loc = Vector2(0) if not event else Vector2(event.x, event.y)
        ref = self.toContext(loc, Context.WORLD)

        if scale:
            self.__scale = Vector2(scale)
        elif event:
            self.__scale -= Vector2(event.delta)
        else:
            self.__scale = Vector2(100)
        self.__scale.clamp(5, 400)

        newRef = self.toContext(loc, Context.WORLD)
        self.__offset.pos += ref - newRef
        self._refresh()

    def getScale(self, context: Context):
        if context == Context.WORLD:
            return self.__scale
        return Vector2(100)

    def _worldToScreen(self, world: Vector2) -> Vector2:
        return (world - self.__offset.pos) * (self.__scale / 100) + self.__center


    def toScreen(self, coord: Vector2, context: Context):
        if context == Context.WORLD:
            return (coord - self.__offset.pos) * (self.__scale / 100) + self.__center
        if context == Context.OVERLAY:
            return coord + self.__center
        return coord

    def _screenToWorld(self, screen: Vector2) -> Vector2:
        return ((screen - self.__center) / (self.__scale / 100.0)) + self.__offset.pos

    def toContext(self, coord: Vector2, context: Context):
        if context == Context.WORLD:
            return ((coord - self.__center) / (self.__scale / 100.0)) + self.__offset.pos
        if context == Context.OVERLAY:
            return coord - self.__center
        return coord


    def centerImage(self):
        if self.__image == "":
            return

        (w, h) = self.__image.size
        self.__canvassize = Vector2(self.winfo_width(), self.winfo_height())
        print(f"Canvas Size: {self.__canvassize}")
        if (w >= h): # Landscape
            scale = self.__canvassize.x / w
        else: # Profile
            scale = self.__canvassize.y / h
        self.__scale = Vector2(scale)
        self.__resizeImage()
        #self.__offset.pos = Vector2(0) - (self.__canvassize / 2) * self.__scale
        self.__offset.pos = Vector2(0) - (self.__canvassize / 2)
        self._refresh()
