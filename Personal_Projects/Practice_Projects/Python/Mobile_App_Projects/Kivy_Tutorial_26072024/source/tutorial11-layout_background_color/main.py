"""
    Date: Sat-27-July-2024

    This tutorial demonstrates two ways on how to change background color of the Kivy Layout.

    The First Method is done in the Kivy Design File.

    The Second Method involves the following module:
    from kivy.core.window import Window
    It is done in the Python file

    Now, one can write the code for the two methods; but the one written in the kivy
    design/style file will override this one
"""

from kivy.app import App
from kivy.uix.widget import Widget
from kivy.properties import ObjectProperty
from kivy.lang import Builder
from kivy.core.window import Window

#   Designate the .kv styling/design file
Builder.load_file('source/tutorial11-layout_background_color/base_style.kv')



class MyLayout(Widget):
    pass


class App(App):
    def build(self):
        self.title = "Background Coloring"
        Window.clearcolor = (0.25, 0.25, 0.25, 1)
        return MyLayout()


if __name__ == '__main__':
    App().run()