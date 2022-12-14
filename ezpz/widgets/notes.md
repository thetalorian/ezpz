Ok, so I'm probably going way overboard with this, but I keep telling myself it is in my own future interest for learning and for learning.

As I've been diving into the problem I'm hitting new ideas and approaches. In particular I'm thinking about the concept of widgets in the context of inheritance and composition, and I'm also thinking about the right way to represent layouts and organizing on-screen elements, and wondering if it makes sense to introduce additional coordinate systems.

First item is that I've currently got everything listed as widgets, but I've already started to break that by introducing buttons that are not actually widgets, but have a lot of repeated code, so it seems like what I may want is a way to group together the distinct functionality as add on classes for composition and allow for the basic element class to extend them in different combinations.

So, I'm currently starting with coords as the abstract base. That's just a named point in the world, consists of just an id and a Vector2 for its position, along with a context to indicate if the coordinates are world coordinates or screen coordinates. The current version also has the basics of the drag and drop code, since it started as a drag and drop point, but not everything actually needs drag and drop capabilities, so it seems like we would want to be able to split that out.

To do that we introduce a handle class that wraps up the drag and drop functionality. A coord with a handle can be moved, one without can't.

Additionally we want button functionality, the ability to provide a call back and activate it for a given element. Not everything needs that. Text labels and images are good examples, in theory they wouldn't do anything on a click or double click.

It's also worth thinking about screen representation. The drag and drop functionality of the widgets also applies to the offset waypoint element, but that doesn't have a representation at all. Do we need the ability to separate that out so we have a class of dragable obejects that are not rendered, or is it fine to just have draggable items that are not visible? I think we can ignore those cases and just make the render pass for the rare invisible objects.

Actually, I guess the same would apply for the button activity, the functionality can be there for all widgets, and just not set. I guess instead of having a subclass without activation we can just have the activation callback on all as an option. Maybe we will want to be able to bind callbacks on labels or images.

Ok, so that's fine. What about the handles? Maybe the solution there is just to make the drag and drop optional. So the base widget class still has drag and drop code, activation code, and rendering code, but all three are completely optional on any given widget.

Does that cover what we need?

Buttons are just images with a click or double click bound to them, with dragging disabled. They can be in screen space or in world space. Images would work the same way. I guess the same would actually work for the other widgets as well. Can we actually just have one generic widget class that gets used for everything? I feel like it's helpful to be able to extend and alter stuff, as with the thumbnail. Maybe the basic widget is helpful for general use, but also can be extended for more interesting functionality.


The other part that really needs some thinking is how to handle containers and layouts. Currently these are also widgets, which allows us to set a representation for it when the container is visisble, or not when it won't be, but that seems potentially complex. Specifically what if we want a variety of representations. I'm thinking that maybe a layout widget should have both a list of controlled widgets and an option to add a backing widget of any kind that will have its position pinned to the layout widget's position. That widget should then also have a drag and drop handle, but tied to the layout?

Hm. Actually, that sounds complex. Maybe the other way around is what we want, we can add a layout to any widget to make that widget act as a container for other widgets. Obviously some widgets will make more sense than others.

Which sort of starts to get my brain on the other topic I wanted to talk through. I'm thinking that it would be a good idea to have the widgets think about things not specifically in terms of screen vs world space, but in local vs parent. It would be handy to be able to express the sub positions of widgets relative to their parents. And that would also, at least to some degree, potentially open up generalizing the main canvas window. The waypoint is already a widget, existing outside of the rest of the widget structure, but it could be treated as the basic widget in this setup. Screen will be the parent context, world would be the local context. If instead of just having other widgets we start a widget chain there we have the option of adding any additional widgets we want into its assigned layout manager. The canvas wouldn't need to keep a list of its widgets, the widgets do that. And any widget can have a container added to it, allowing that to contain additional widgets that are positioned relative to itself. The difficulty with that is going to be making sure that the coordinates go through all of the proper shifts to get where they are going in the right context.

So, how does that happen?


Let's assume that we have the following:

Canvas Widget (Waypoint Drag and Drop offset) - Free range layout manager (no corrections)
Image backed window widget - grid layout manager
Thumbnail widget - no layout manager

The thumbnail's coordinates are relative to the window, and the window's coordinates are relative to the canvas (world space), and the canvas coordinates are relative to the screen. So, if we click on the screen and get screen space coordinates sent to the thumbnail we can calculate it's context coordinates by translating from screen to world and then from world to window. So the converted version would always be to call the equivalent of the screen to world function for the parent. Just like in reverse calling world to screen. Except in this case we don't call against the canvas directly, it's always the parent. And the first thing the parent does is to call the same conversion for its parent, which then does the same, so each level gets its own coordinate system.

The recursive calls would end when they get to the root widget, which would just do the actual screen to world calculations it does now, instead of having that happen on the canvas. 



Ok, more thoughts on widget design. At the moment the types of widgets I'm creating are starting to get a bit out of hand, and it seems like most if not all of them have common connections and features. If these features were a part of the base widget it would be far easier to customize and extend. So maybe it's time to rework things a bit.


Features that all widgets seem to want to at least have as options:

labels - It seems like a really good idea to be able to apply a label to each widget. That label should probably be able to be repositioned either over the widget or around it.

Images - Adding an image to a widget is really helpful. In the case of the thumbnails and now the box image widget we need to be able to set the render size of the image independent of the actual image size and the scale of the scene.

Rotation - box widget needs to be rotateable, could be helpful in other scenarios. It would allow us to set the widget size unrotated but have the rendering adjust.

Borders - The box image widget has a border, arguably we could just make that a normal feature as well, could be helpful with the thumbnails.

Anchors - We already have an anchor set, but that only indicates where our origin is with the parent. For more render control we would actually want the anchor to adjust the rendering. We always render with the widget's position being in the center, but it would be helpful to shift the rendering as well. Not sure whether we use a different anchor for that, or try to use the same one.

Also, layouts and sizes need to be beefed up and refactored so that we are properly adjusting for anchor positions on relative positions. And ideally the entire context system needs revamping as it doesn't make sense for individual items to be added to parents with different contexts. Instead we should have the contexts be layers with settings, so we could have a world context that shifts based on its offset value and scale, and an overlay that does neither, and all items are added to one or the other. In these cases the widgets themselves do not have a context, only the layer does. That makes creating them easier, and also gives us a way to have more control over render order, because we can always render all world objects before rendering any of the overlay objects.



So, let's recap, I guess:

We need a window to hold the canvas

We need one (or more) canvases. Originally the canvas was extended with the drag and drop and pan and zoom functionality, but maybe that's not the right approach. With the addition of layers it seems like most of that moves to the layers.

Each layer would have its own scale and offset, with the option to have those layers offsets and scales bound to controls. So really each canvas would just need a list of layers and would render the layers in order.

So then each layer is also kind of a widget, I guess.

So, maybe we really don't need to get crazy? Maybe we really do just have each child render its content based on its anchor in relative position to its parent.

So, if the layer has an anchor at center, it gets screen shifted to place that position at the middle of the canvas.

If we add a widget to that with a center anchor it also gets rendered at 0,0. Let's say it's an image that is 200 x 200.

Then we add a widget to that, with an anchor in the lower left, still with no offset. It renders at 0,0 relative to the lower left corner of the parent, which is currently at -100, 100 on the layer, shifted off by whatever the offset for the layer is. I guess if we link the layer size to the canvas size we can keep the anchors even on the technically endless screen. We can reset the size of the layer according to the canvas.


So let's see. At that point the process to render everything would be:

for each layer in List[layers]
    for each widget in list[widgets]
      for each widget in widget children