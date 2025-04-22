"""
    Date: Thurs-1-Aug-2024

    This tutorial demonstrates implementation of the Tabs that can be toggled through for different
    screens

    This is a neat way of a Single-Page app/

"""

from kivy.app import App
from kivy.uix.widget import Widget
from kivy.lang import Builder
from kivy.core.window import Window
from kivy.properties import ObjectProperty
from kivy.uix.tabbedpanel import TabbedPanel


Builder.load_file('base_style.kv')


class MyLayout(TabbedPanel):
    ...


class MyApp(App):
    def build(self):
        self.title = "Tabs"
        Window.clearcolor = (0.1, 0.07, 0.15, 1)
        return MyLayout()
        

if __name__ == "__main__":
    MyApp().run()