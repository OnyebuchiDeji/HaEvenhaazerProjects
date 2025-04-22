"""
    Date: Fri-27-July-2024
    
    Following tutorial3, but fixing the Layout for the Button object.
    Using row_force_default and col_force_default and
    row_default_height and col_default_width to force-change
    the row and column width and height.
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
        self.cols = 1



        #   Force-setting row and column sizes of the Parent GridLayout:
        self.row_force_default=True
        self.row_default_height=120 #   because the inner grid has 3 widgets of row-height 40
        self.col_force_default=True
        self.col_default_width=400  #   because the inner grid has 2 columns of width 100

        #   Create Second/Inner GridLayout and force-set row and column size
        self.top_grid = GridLayout(cols=2,
                                   row_force_default=True,
                                   row_default_height=40,
                                   col_force_default=True,
                                   col_default_width=200)  #   or self.top_grid.cols = 2 in next line
        

        #   Add Widgets
        self.top_grid.add_widget(Label(text="First Name: "))
        #   Add Input Box
        self.fname = TextInput(multiline=False)
        self.top_grid.add_widget(self.fname)

        
        self.top_grid.add_widget(Label(text="Last Name: "))
        self.lname = TextInput(multiline=False)
        self.top_grid.add_widget(self.lname)

        self.top_grid.add_widget(Label(text="Favourite Color: "))
        self.color = TextInput(multiline=False)
        self.top_grid.add_widget(self.color)

        #   Add top_grid to Parent Grid
        self.add_widget(self.top_grid)

        #   Create a Submit Button
        self.submit_btn = Button(text="Submit", font_size=32,
                                size_hint_y = None,
                                height = 50)
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
        self.title = "Widget Dimension Control -- row and col size-forcing"
        return MyGridLayout()



if __name__ == '__main__':
    MyApp().run()