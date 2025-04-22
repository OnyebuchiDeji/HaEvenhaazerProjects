"""
    Date: Wed-31-July-2024

    This tutorial demonstrates implementation of sliders.

    One can also reference the ids without using ObjectProperty or self.ids

    But it is seen that the reason why `ObjectProperty` is used is so that Python can
    recognise that reference as defined
"""

from kivy.app import App
from kivy.uix.widget import Widget
from kivy.lang import Builder
from kivy.core.window import Window
from kivy.properties import ObjectProperty
# from kivy.uix.slider import Slider


Builder.load_file('base_style.kv')

class MyLayout(Widget):
    slider_text = ObjectProperty(None)
    def slider_value(self, *args):
        """The Slider Values are indeed float"""
        # print(*args)
        # print(type(args[0]))
        # print(type(args[1]))
        # print(type(args[0]))
        print(args[1])          #  The Value
        self.slider_text.text = str(float(args[1]))
        self.slider_text.font_size = str(float(args[1]) + 32)

class MyApp(App):
    def build(self):
        self.title = "Sliders"
        Window.clearcolor = (0.1, 0.12, 0.2, 1)
        return MyLayout()
        
if __name__ == "__main__":
    MyApp().run()