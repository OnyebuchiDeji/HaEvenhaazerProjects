"""
    Date: Tue-13-Aug-2024

    This episode demonstrates the use of KivyMD to create a Card

    Here, the code from the kivymd folder downloaded with pip into the KivyMD directory 
    is taken. The documentation for implementing every uix and kind of thing is in this directory below:
    Code from the KivyMD/kivymd/uix/cards folder is taken.

    I can look at it to learn how to design apps.

    The Code demonstrates the creation of Cards.
    According to the above source code, there are three types of


"""

from kivy.app import App
from kivy.uix.widget import Widget
from kivy.properties import (
    ObjectProperty,
    StringProperty
)
from kivy.lang import Builder
from kivy.core.window import Window

from kivymd.app import MDApp
from kivymd.uix.card import MDCard


#   Designate the .kv design file
Builder.load_file("base_style.kv")

class MyCard(MDCard):
    '''Implements a material card.'''

    text = StringProperty()

class MyLayout(Widget):
    pass


#   The KivyMD app
class MyApp(MDApp):
    # root = MyLayout()
    def build(self):
        self.title = "KivyMD Design"
        Window.clearcolor = (0.07, 0.07, 0.1, 1)
        self.root = MyLayout()
        return self.root

    def on_start(self):
        for style in ("elevated", "filled", "outlined"):
            self.root.ids.box.add_widget(
                MyCard(style=style, text=style.capitalize())
            )
    

if __name__ == "__main__":
    MyApp().run()