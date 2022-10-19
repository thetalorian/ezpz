from example.dimensionWindow import DimensionWindow
import ezpz
from ezpz.contexts import Anchor
from ezpz.widgets import Thumbnail, ImagePane, Container, TKFrame
from ezpz.layouts import Grid, Column, Row
from ezpz import Context, Vector2, Anchor
from PIL import Image
import tkinter as tk

from ezpz.widgets.label import Label
class AppWindow(ezpz.Window):
    def __init__(self):
        super().__init__()

    def setImage(self, path):
        print(f"AppWindow setting image path: {path}")
        self._canvas.setImage(Image.open(path))

    def showThumbs(self):
        image = Image.open("test.jpg")
        icon = Image.open("open.png")
        icon = icon.resize((64, 64))
        self.thumbnails = Container('thumbnails', self._canvas)
        self.thumbnails.setLayout(Grid())

        button = ImagePane(f"Button1", self._canvas)
        button.setImage(icon)
        #button.setCallback(self.addNewThumb)
        button.tag_bind('<ButtonPress-1>', self.addNewThumb)
        self.thumbnails.add(button)

        title = ""
        for x in range(0,10):
            title = f"Thumb{x}"
            thumb = Thumbnail(title, self._canvas)
            thumb.setImage(image)
            #thumb.setCallback(self.openImage)
            thumb.tag_bind('<Double-ButtonPress-1>', self.openImage)
            #self._canvas.tag_bind(title, '<Double-ButtonPress-1>', thumb.activate)
            self.thumbnails.add(thumb)


        self._canvas.addItem(self.thumbnails)

    def addNewThumb(self, _):
        print("Adding new thumbnail")
        image = Image.open("test.jpg")
        count = len(self.thumbnails)
        thumb = Thumbnail(f"Thumb{count+1}", self._canvas)
        thumb.setImage(image)
        self.thumbnails.add(thumb)
        print(f"Current count: {len(self.thumbnails)}")
        self._canvas._refresh()

    def openImage(self, _):
        #print(f"Opening Image from {thumb}")
        self._canvas.clearItems()
        image = Image.open("test.jpg")
        imagepane = ImagePane('image', self._canvas)
        imagepane.setImage(image)
        self._canvas.addItem(imagepane)
        returnbutton = ImagePane('goback', self._canvas, Context.OVERLAY, anchor=Anchor.NE)
        returnbutton.setImage(Image.open("cancel.png").resize((16,16)))
        returnbutton.pos = Vector2(-20, 20)
        returnbutton.tag_bind('<ButtonPress-1>', self.closeImage)
        self._canvas.addItem(returnbutton)

    def closeImage(self, _):
        self._canvas.reset()
        self.showThumbs()

    def showFrameWindow(self):
        self.frame = TKFrame('frame', self._canvas)

        data = {}
        data['width'] = 2.5
        data['height'] = 3.5
        data['depth'] = 1.5
        data['units'] = "in"

        self.dimensions = DimensionWindow(self, data)

        container = Container('container', self._canvas)
        container.setLayout(Column())

        label = Label('label', self._canvas)
        label.setText("YEAAAAAAAAAAAAA")
        label.setFont(size=30, face='Roboto', style='italic bold')
        container.add(label)

        label2 = Label('label', self._canvas)
        label2.setText("BOIIIEEE")
        label2.setFont(size=20, face='Roboto', style='bold')
        container.add(label2)

        label3 = Label('label', self._canvas)
        label3.setText("Good Going!")
        label3.setFont(size=35, face='Roboto')
        container.add(label3)


        self.frame.setFrame(self.dimensions)
        container.add(self.frame)


        buttons = Container('buttons', self._canvas)
        buttons.setLayout(Row(padding=10))
        acceptButton = ImagePane('acceptButton', self._canvas)
        #acceptButton.pos = Vector2(-20, 60)
        acceptButton.setImage(Image.open("accept.png").resize((16,16)))
        acceptButton.tag_bind('<ButtonPress-1>', self.dimensions.report)

        cancelButton = ImagePane('cancelButton', self._canvas)
        #cancelButton.pos = Vector2(20, 60)
        cancelButton.setImage(Image.open("cancel.png").resize((16,16)))
        cancelButton.tag_bind('<ButtonPress-1>', self.closeEntryWindow)


        buttons.add(acceptButton)
        buttons.add(cancelButton)
        container.add(buttons)

        self._canvas.addItem(container)

    def closeEntryWindow(self, _):
        self._canvas.clearItems()
        self.showThumbs()


if __name__=="__main__":
    AppWindow()