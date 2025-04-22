"""
    Date: Fri-26-July-2024
    
    Input Boxes and Buttons -- Making a Form
"""

import kivy
from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.gridlayout import GridLayout
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button

class MyGridLayout(GridLayout):
    #   Initialize Infinite Keywords
    def __init__(self, **kwargs):
        #   Call GridLayout constructor
        super(MyGridLayout, self).__init__(**kwargs)

        #   Set Columns
        self.cols = 2

        #   Add Widgets
        self.add_widget(Label(text="First Name: "))
        #   Add Input Box
        self.fname = TextInput(multiline=False)
        self.add_widget(self.fname)

        
        self.add_widget(Label(text="Last Name: "))
        self.lname = TextInput(multiline=False)
        self.add_widget(self.lname)

        self.add_widget(Label(text="Favourite Color: "))
        self.color = TextInput(multiline=False)
        self.add_widget(self.color)

        #   Create a Submit Button
        self.submit_btn = Button(text="Submit", font_size=32)
        #   Bind Button to a method:
        self.submit_btn.bind(on_press=self.press)
        self.add_widget(self.submit_btn)

    ##  The second argument can be named anything.
    ##  It references the button that caused the event
    def press(self, event_triggerer):
        fname = self.fname.text
        lname = self.lname.text
        color = self.color.text

        # print(event_triggerer)    <-- prints the object's info
        # print(f"My name is {fname} {lname}, and my favourite color is {color}.")
        info = f"My name is {fname} {lname}, and my favourite color is {color}."
        self.add_widget(Label(text=info))

        #   Clear input boxes
        self.fname.text = ""
        self.lname.text = ""
        self.color.text = ""

class MyApp(App):
    def build(self):
        self.title = "Inputs and Buttons"
        return MyGridLayout()



if __name__ == '__main__':
    MyApp().run()