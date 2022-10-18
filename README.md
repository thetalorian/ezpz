# ezpz
Packaged code for tkinter canvas with Pan & Zoom functionality along with a widget and layout placement system.


# Example Use
See the example folder for one potential application.

EZPZ was designed to be an extensible and flexible UI base for creating MVC applications with rich image based user interfaces. In the example AppWindow is meant to be a view class that can leverage the ezpz widgets to create UI elements for whatever test case the model requires and make those widgets available to the controller class (hypersimplified here as main.py)

Individual widgets may or may not have drag and drop capabilities, be assigned key or mouse button bindings linked to callback functions, and are optional to have an on screen representation rendered. They can exist in either a statically positioned overlay context, or in the world context where they will be subject to changes from user input for zooming and scaling. Widgets can also be assigned a layout manager and have other widgets assigned to them as children, at which point the layout manager will dictate the child widget's positions in relation to themselves and the parents.

This is a personal use project and is very much a work in progress.

### References
Package structure based on https://python-packaging.readthedocs.io/en/latest/minimal.html.
Test install with pip3 install -e .