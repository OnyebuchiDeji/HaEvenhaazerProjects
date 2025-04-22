"""
    Date: Thurs-1-Aug-2024

    This tutorial demonstrates implementation of the ScreenManager for Multiple Screens
"""

from kivy.app import App
from kivy.uix.widget import Widget
from kivy.lang import Builder
from kivy.core.window import Window
from kivy.properties import ObjectProperty
from kivy.uix.screenmanager import ScreenManager, Screen

#   Define Each Screen to be Used
class FirstScreen(Screen):
    ...

class SecondScreen(Screen):
    ...

class ScreenMaster(ScreenManager):
    ...

#   Desugnate the .kv design file
kv = Builder.load_file('base_style.kv')



class MyApp(App):
    def build(self):
        self.title = "ScreenManager - Multiple Screens"
        Window.clearcolor = (0.15, 0.07, 0.1, 1)
        return kv
        

if __name__ == "__main__":
    MyApp().run()