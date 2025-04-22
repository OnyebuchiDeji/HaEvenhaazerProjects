"""
    Date: Wed-31-July-2024

    This tutorial demonstrates implementation of Carousels.

    They allow one to click and drag to allow one to view images and such.
    Also, one can display images from a url

    I can also use these for Flash cards.
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
        self.title = "Carousel"
        Window.clearcolor = (0.15, 0.07, 0.12, 1)
        return MyLayout()
        
if __name__ == "__main__":
    MyApp().run()