"""
    Date: Wed-21-July-2024
    
    This tutorial demonstrates a Simple Calculator App
"""

from kivy.app import App
from kivy.uix.widget import Widget
from kivy.properties import ObjectProperty
from kivy.lang import Builder
from kivy.core.window import Window

"""
    Something for automating the size depending on the device platform
    if(platform == 'android' | platform == 'ios' | paltform == 'android'):
            Window.maximize()
        else:
            Window.size = (620, 1024)

        return kv
"""

#   Set App Size
# desired_size = 
Window.size = (324, 666)
Builder.load_file("source/tutorial15-simple_calculator/base_style.kv")


class MyLayout(Widget):
    
    def clear_input(self):
        self.ids.calc_input.text = "0"


class CalculatorApp(App):
    def build(self):
        self.title = "My Calculator App"
        Window.clearcolor = (0.65, 0.65, 0.65, 1)
        return MyLayout()


if __name__ == "__main__":
    CalculatorApp().run()