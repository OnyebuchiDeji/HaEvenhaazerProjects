"""
    Date: Fri-27-July-2024
    
    Coloring the TextInput and Button Widgets
    The normal way of using `background_color` does not work for Labels
    But using `color` does indeed work
"""

import kivy
from kivy.app import App
from kivy.uix.widget import Widget
from kivy.uix.label import Label
from kivy.properties import ObjectProperty
from kivy.lang import Builder

#   Explicitely loading the file to be used.
Builder.load_file('source/tutorial7-button_colors/base_style.kv')



class MyLayout(Widget):
    fname = ObjectProperty(None)
    lname = ObjectProperty(None)
    color = ObjectProperty(None)
    print_area = ObjectProperty(Label)

    #   Note that when using the Kivy Design language, if putting second argument...
    #   in the kv design app, pass in self.
    def press(self, event_trigerrer):
        fname = self.fname.text
        lname = self.lname.text
        color = self.color.text

        info = f"My name is {fname} {lname}, and my favourite color is {color}."
        print(info)
        print(event_trigerrer)
        
        self.print_area.text = info

        #   Clear input boxes
        self.fname.text = ""
        self.lname.text = ""
        self.color.text = ""

class App(App):
    def build(self):
        self.title = "Kivy Builder"
        return MyLayout()


if __name__ == '__main__':
    App().run()