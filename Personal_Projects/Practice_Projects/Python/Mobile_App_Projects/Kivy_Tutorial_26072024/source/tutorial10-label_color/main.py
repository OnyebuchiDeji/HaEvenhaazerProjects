"""
    Date: Sat-27-July-2024

    This tutorial demonstrates how to change the color of a label's font, its background
    and the style of the font, including outline width and color, boldness, and italics
"""

from kivy.app import App
from kivy.uix.widget import Widget
from kivy.properties import ObjectProperty
from kivy.lang import Builder

#   Designate the .kv styling/design file
Builder.load_file('source/tutorial10-label_color/base_style.kv')



class MyLayout(Widget):
    pass


class App(App):
    def build(self):
        self.title = "Label Coloring"
        return MyLayout()


if __name__ == '__main__':
    App().run()