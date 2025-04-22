"""
    Date: Fri-27-July-2024
    
    Introducing the Kivy desing language to abstract logic from design.
    Note that kivy looks for the kivy design file that has the same name
    as the main app, e.g. MyApp, but in lowercase.
"""

import kivy
from kivy.app import App
from kivy.uix.widget import Widget
from kivy.uix.label import Label
from kivy.properties import ObjectProperty
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

class MyApp(App):
    def build(self):
        self.title = "Kivy Design Language"
        return MyLayout()


if __name__ == '__main__':
    MyApp().run()