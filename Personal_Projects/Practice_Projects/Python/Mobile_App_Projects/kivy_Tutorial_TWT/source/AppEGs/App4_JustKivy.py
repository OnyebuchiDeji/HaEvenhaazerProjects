"""
    Date: 02-JAN-2024

    Using the KV language. It separates the style from your code
    The kv file should have the all lower case form of the name of the main class -- in this case, MyApp
    However, it should not have app in its name, so:
    EG: MyApp   -> my.kv.
    Yet, it works normally for me regardless!

"""

import kivy
from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.gridlayout import GridLayout
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.uix.widget import Widget

"""
    This version of the app goes into the KV style scripting, as most of the implementation was just done on the...
    Kivy style file!
    It does what was done in App2, but only in the Kivy Script!
    In it, a Widget object is made and a GridLayout is added into it and another GridLayout in that!
    And a button is added tot the outer GridLayout, while the inner has the input fields!

    Kivy searches for the Class that has the same name as the one in the tag
    The Widget Class has its default position and size (width and height), so it is changed in the kv script.
    Kivy objects have their origin at the bottom left corner. This is the same for the window positioning

    The extra things added are these:
    It resizes the window and shifts its position!
"""

class MyGrid(Widget):
    pass

class App4(App):
    def build(self):
        return MyGrid()

if __name__== "__main__":
    App4().run()