"""
    Date: Thurs-1-Aug-2024

    This tutorial demonstrates implementation of adding images on buttons in Kivy.
"""

from kivy.app import App
from kivy.uix.widget import Widget
from kivy.lang import Builder
from kivy.core.window import Window
from kivy.properties import ObjectProperty

Builder.load_file('base_style.kv')


class MyLayout(Widget):
    def click_login_button(self):
        self.ids.my_label_id.text = "You're Pressing the Button"
        self.ids.login_image_id.source = "resources/login_pressed.png"

    def release_login_button(self):
        self.ids.my_label_id.text = "You Released the Button"
        self.ids.login_image_id.source = "resources/login.png"

        


class MyApp(App):
    def build(self):
        self.title = "Images on Buttons"
        Window.clearcolor = (0.15, 0.07, 0.1, 1)
        return MyLayout()
        

if __name__ == "__main__":
    MyApp().run()