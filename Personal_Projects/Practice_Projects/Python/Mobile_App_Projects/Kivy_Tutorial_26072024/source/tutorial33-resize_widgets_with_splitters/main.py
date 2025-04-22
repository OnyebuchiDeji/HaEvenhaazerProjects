"""
    Date: Thurs-1-Aug-2024

    This tutorial demonstrates implementation of the Splitter to split up sections in a widget
    and to resize the widgets with them.

    It can be pulled and dragged
"""

from kivy.app import App
from kivy.uix.widget import Widget
from kivy.lang import Builder
from kivy.core.window import Window
from kivy.properties import ObjectProperty

Builder.load_file('base_style.kv')


class MyLayout(Widget):
    ...
        


class MyApp(App):
    def build(self):
        self.title = "Widget Splitters"
        Window.clearcolor = (0.15, 0.07, 0.1, 1)
        return MyLayout()
        

if __name__ == "__main__":
    MyApp().run()