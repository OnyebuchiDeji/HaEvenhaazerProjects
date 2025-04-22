"""
    Date: Sat-27-July-2024

    Box Layout: used to stack things either vertically or horizontally.
"""

from kivy.app import App
from kivy.uix.widget import Widget
from kivy.properties import ObjectProperty
from kivy.lang import Builder

#   Designate the .kv styling/design file
Builder.load_file('source/tutorial8-kivy_box_layout/base_style.kv')



class MyLayout(Widget):
    pass

class App(App):
    def build(self):
        self.title = "Box Layout"
        return MyLayout()


if __name__ == '__main__':
    App().run()