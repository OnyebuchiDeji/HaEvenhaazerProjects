"""
    Date: Mon-12-Aug-2024

    This episode demonstrates the use of the Markup language in Kivy to change the Style of Text
"""

from kivy.app import App
from kivy.uix.widget import Widget
from kivy.lang import Builder
from kivy.core.window import Window


#   Designate the .kv design file
Builder.load_file("base_style.kv")

class MyLayout(Widget):
    pass

class MyApp(App):
    def build(self):
        self.title = "Markup in Kivy"
        Window.clearcolor = (0.15, 0.07, 0.1, 1)
        return MyLayout()


if __name__ == "__main__":
    MyApp().run()