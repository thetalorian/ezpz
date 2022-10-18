import ezpz
from ezpz.widgets import Thumbnail, ImagePane, Container
from ezpz.layouts import Grid
from ezpz import Context, Vector2
from PIL import Image

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
        returnbutton = ImagePane('goback', self._canvas, Context.OVERLAY)
        returnbutton.setImage(Image.open("cancel.png").resize((16,16)))
        returnbutton.pos = Vector2(20, 20)
        returnbutton.tag_bind('<ButtonPress-1>', self.closeImage)
        self._canvas.addItem(returnbutton)

    def closeImage(self, _):
        self._canvas.reset()
        self.showThumbs()

if __name__=="__main__":
    AppWindow()