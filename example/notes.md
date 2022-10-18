Ok, time to rethink #827.

Having explored the problem space a bit, I'm thinking it would be better to reorganize things a bit for the UI. I'm trying to make it at least semi-generic and reusable, so I feel like the naming is getting odd, and it would actually be a good idea to try to create more of a separation between the interface and the arcbg app, including the demo section.

This whole ezpz set of functions looks like it should become its own package, so I'd like to move them off and just have the demo app separately import that package and work with it.

To clear it up a bit it seems like a good idea to start introducing some actual abstract classes and concepts, and just reorganize in general.

So we have an idea of a Window, and that window just includes a fully stretched Canvas.

So to get the most basic app going the user would just do:

```
from ezpz import Window

def main():
    window = ezpz.Window()
    window.start()
```

From that point the user should be able to make calls to add widgets and hopefully add callbacks for those widgets.

So, I think the canvas doesn't actually need to maintain a list of items directly, if we can pass the widget object back through the handler, so the canvas would just need a list of layouts, and when rendering we would call each layout and have that layout render each of its items.

The thing I'm trying to figure out is if the layouts should also be widgets. In theory they would need a location, but I'm thinking it would be at least potentially a thing where we would also want the layout itself to be drag and drop capable. Like a floating button menu. If that's the case ones that don't have a drag and drop or visible background would just pass on their render, while layouts that do do want that can render their group representation (image, box, whatever) and then draw its own widgets on top of that.

So, yeah, in that case we don't actually need a differentiation between a widget and a layout, a layout is just a widget with the ability to have other widgets added to it.

That said, it seems like the previous DDPoint class is now just the base widget. That should be abstracted. We can also then abstract out a layout class to extend widget, which forces an item list and an addItem method.

