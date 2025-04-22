"""
    Date: Sun-28-July-2024

    This tutorial demonstrates the use of the Float Layout

    Float Layouts must always use the size_hint and the pos_hint
"""
from kivy.app import App
from kivy.uix.widget import Widget
from kivy.properties import ObjectProperty
from kivy.lang.builder import Builder
from kivy.core.window import Window

#   If float layout was to be used here, do the below
## from kivy.uix.floatlayout import FloatLayout


Builder.load_file("source/tutorial13-float_layout/base_style.kv")

class MyLayout(Widget):
    pass


class MyApp(App):
    def build(self):
        self.title = "Float Layout"
        Window.clearcolor = (0.65, 0.65, 0.65, 1)
        return MyLayout()

if __name__ == "__main__":
    MyApp().run()