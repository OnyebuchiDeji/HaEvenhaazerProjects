"""
    03-JAN-2024
    This Version shows the implementation of a simple drawing application
"""

import kivy
from kivy.app import App
from kivy.uix.widget import Widget
from kivy.properties import ObjectProperty
from kivy.graphics import Rectangle, Color, Ellipse, Line

"""
    Kivy grpahics work like it does on OpenGl.
    There is a Canvas with drawing instructions, the positions can be update and such.
    The instructions are updated and moved accordingly, not as pygame works

    Note!   For objects in kv, whether the screen, the Widget, GridLayout surface, FloatLayout surface, and Buttons...
    Their origin is from the bottom left!
    You can go through the library to learn how to use them! that's where I went to to find Ellipse

    the app8.kv os not used!
"""
class Touch(Widget):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        with self.canvas:   ##  Handle to canvas object
            ##  To change the object's color, the entire canvas's drawing color for every object has to be changed first.
            ##  Defai=ult Color is white!
            Color(1, 0, 0, 0.5, mode="rgba")
            self.rect1 = Rectangle(pos=(20, 20), size=(50, 50))
            Color(0.7, 0.2, 0.7, 0.5, mode="rgba")
            self.rect2 = Rectangle(pos=(250, 300), size=(50, 100))
            Color(0.3, 0.7, 0.9, 0.5, mode="rgba")
            self.line = Line(points=(20, 300, 400, 300, 400, 150))


    def on_touch_down(self, touch):
        print("Mouse Down!", touch)
        self.rect1.pos = touch.pos


    def on_touch_move(self, touch):
        print("Mouse Moved!", touch)
        self.rect1.pos = touch.pos

    def on_touch_up(self, touch):
        print("Mouse Up!", touch)


class App8(App):
    def build(self):
        return Touch()

if __name__== "__main__":
    App8().run()