"""
    Date: Mon-19-Aug-2024

    This episode demonstrates how to remove the Titlebar from a Kivy app

    These were done and used:
        1.  Using the `Window.borderless=True` is what removes the Border.
        2.  Changing the position where the Window appears at 

"""

from kivy.config import Config
import time

#   Tried to animate the windows motion
"""left = 0
top = 0
while True:
    left -= 20
    top += 50
    Config.set("graphics", "position", "custom")
    Config.set("graphics", "left", left)
    Config.set("graphics", "top", top)
    time.sleep(2)

    if left <= -120 and top >= 200:
        break"""

##  The above have to be done befor the below

from kivymd.app import MDApp
from kivy.lang import Builder
from kivymd.uix.boxlayout import MDBoxLayout
from kivy.core.window import Window     ##  Gives access to the property to remove the Titlebar

from kivy.properties import (
    ObjectProperty,
    StringProperty,
    ListProperty
)



#   Designate the .kv design file
Builder.load_file("base_style.kv")


class MyBoxLayout(MDBoxLayout):
    pass


#   The KivyMD app
class MyApp(MDApp):
    light_theme = False
    theme_text_l = "L"
    theme_text_d = "D"


    def build(self):
        self.title = "No Titlebar"
        Window.borderless = True
        Window.clearcolor = (0.3, 0.25, 0.3, 1)
        self.theme_cls.theme_style = "Light" if self.light_theme else "Dark"
        self.theme_cls.primary_palette = "Forestgreen"
        self.theme_cls.accent_palette = "Red"

        self.root = MyBoxLayout()
        return self.root

    def toggle_theme(self):
        self.light_theme = not self.light_theme
        self.theme_cls.theme_style = "Light" if self.light_theme else "Dark"
        self.root.ids.id_theme_btn.text = self.theme_text_l if self.light_theme else self.theme_text_d
        
        
if __name__ == "__main__":
    MyApp().run()
