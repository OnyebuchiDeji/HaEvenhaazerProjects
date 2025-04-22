"""
    Date: Fri-27-July-2024
    
    The Kivy Builder.

    Enables one to designate and include different kivy design files
    not just the default.
"""

import kivy
from kivy.app import App
from kivy.uix.widget import Widget
from kivy.uix.label import Label
from kivy.properties import ObjectProperty
from kivy.lang import Builder

#   Explicitely loading the file to be used.
# Builder.load_file('source/tutorial6-kivy_builder/custom.kv')


#   Load a String -- but goes against the goal of separating design file from logic file.
kvFile = """
<MyLayout>
    fname: fname_id
    lname: lname_id
    color: color_id
    print_area: print_area_id
    
    GridLayout:
        cols: 1
        size: root.width, root.height

        GridLayout:
            cols: 2

            Label:
                text: "First Name"
            TextInput:
                id: fname_id
                multiline: False    
            Label:
                text: "Last Name"
            TextInput:
                id: lname_id
                multiline: False    
            Label:
                text: "Favourite Color"
            TextInput:
                id: color_id
                multiline: False
        
        Button:
            text: "Submit"
            font_size: 35
            size_hint_y: None
            height: 100
            on_press: root.press(self)
        
        Label:
            id: print_area_id
            text: ""
            font_size: 20
            size_hint_y: None
            height: 100
"""
Builder.load_string(kvFile)





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