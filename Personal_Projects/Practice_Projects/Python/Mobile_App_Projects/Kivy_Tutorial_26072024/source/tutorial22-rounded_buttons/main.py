"""
    Date: Wed-31-July-2024

    This tutorial demonstrates more ways to style the Button widget
"""

from kivy.app import App
from kivy.uix.widget import Widget
from kivy.lang import Builder
from kivy.core.window import Window

Builder.load_file('base_style.kv')

class MyLayout(Widget):
    ...

class MyApp(App):
    def build(self):
        self.title = "Rounded Buttons"
        Window.clearcolor = (0.65, 0.65, 0.65, 1)
        return MyLayout()
        
if __name__ == "__main__":
    MyApp().run()