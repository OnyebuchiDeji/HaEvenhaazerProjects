"""
    Date: Sat-27-July-2024

    This tutorial demonstrates how to load an image.

    Two ways of doing this:
        1.  In Python File -- requires from kivy.uix.image import Image
        2.  In Kivy Design File, which is the best way.
"""

from kivy.app import App
from kivy.uix.widget import Widget
from kivy.properties import ObjectProperty
from kivy.lang import Builder
from kivy.core.window import Window
# from kivy.uix.image import Image



#   Designate the .kv styling/design file
Builder.load_file('source/tutorial12-loading_images/base_style.kv')



class MyLayout(Widget):
    pass


class App(App):
    def build(self):
        self.title = "Background Coloring"
        Window.clearcolor = (0.65, 0.65, 0.65, 1)
        return MyLayout()


if __name__ == '__main__':
    App().run()