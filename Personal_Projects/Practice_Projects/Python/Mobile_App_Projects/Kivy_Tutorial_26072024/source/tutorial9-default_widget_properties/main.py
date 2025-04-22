"""
    Date: Sat-27-July-2024

    This tutorial demonstrates setting the default properties of a widget
    to get more control over it.
    This is done by inheriting these Kivy Widget properties.
"""

from kivy.app import App
from kivy.uix.widget import Widget
from kivy.properties import ObjectProperty
from kivy.lang import Builder

#   Designate the .kv styling/design file
Builder.load_file('source/tutorial9-default_widget_properties/base_style.kv')



class MyLayout(Widget):
    pass


class App(App):
    def build(self):
        self.title = "Default Widget Properties in KV Designer"
        return MyLayout()


if __name__ == '__main__':
    App().run()