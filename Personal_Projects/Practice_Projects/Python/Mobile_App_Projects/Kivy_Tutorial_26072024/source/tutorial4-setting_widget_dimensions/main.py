"""
    Date: Fri-27-July-2024
    
    Following tutorial3, but specifying the height and width of widgets
    But using size_hint_y and size_hint_x set to None to enable
    changing the width and height of widgets, including the top/inner grid layout.
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

        #   Set width and height of Parent GridLayout   <-- No need for this.
        # self.size_hint_y = None
        # self.height = 200
        # self.size_hint_x = None
        # self.width = 400

        #   Create Second/Inner GridLayout and set width and height of widget
        self.top_grid = GridLayout(cols=2,
                                size_hint_y = None,
                                height = 150,
                                size_hint_x = None,
                                width = 400)  #   or self.top_grid.cols = 2 in next line


        #   Add Widgets
        self.top_grid.add_widget(Label(text="First Name: ",
                                size_hint_y = None,
                                height = 50,
                                size_hint_x = None,
                                width = 400))
        #   Add Input Box
        self.fname = TextInput(multiline=False,
                                size_hint_y = None,
                                height = 50,
                                size_hint_x = None,
                                width = 400)
        self.top_grid.add_widget(self.fname)

        
        self.top_grid.add_widget(Label(text="Last Name: ",
                                size_hint_y = None,
                                height = 50,
                                size_hint_x = None,
                                width = 400))
        self.lname = TextInput(multiline=False,
                                size_hint_y = None,
                                height = 50,
                                size_hint_x = None,
                                width = 400)
        self.top_grid.add_widget(self.lname)

        self.top_grid.add_widget(Label(text="Favourite Color: ",
                                size_hint_y = None,
                                height = 50,
                                size_hint_x = None,
                                width = 400))
        self.color = TextInput(multiline=False,
                                size_hint_y = None,
                                height = 50,
                                size_hint_x = None,
                                width = 400)
        self.top_grid.add_widget(self.color)

        #   Add top_grid to Parent Grid
        self.add_widget(self.top_grid)

        ##  Have to specifically put size_hint_y to None to manipulate height
        ##  Likewise, size_hint_x = None, to manipulate width
        self.submit_btn = Button(text="Submit", font_size=32,
                                size_hint_y = None,
                                height = 50,
                                size_hint_x = None,
                                width = 200)
        
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
        self.title = "Widget Dimension Control -- size_hints"
        return MyGridLayout()



if __name__ == '__main__':
    MyApp().run()