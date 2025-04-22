import kivy
from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.gridlayout import GridLayout
from kivy.uix.textinput import TextInput


""""
    Date: 02-JAN-2024
    
    This version of the app adds a GridLayout and Adds Function for Text Input!
    It makes no use of the Kivy Styling Files
"""

class MyGrid(GridLayout):
    def __init__(self, **kwargs):
        # Calling GridLayout constructor
        super(MyGrid, self).__init__(**kwargs)
        self.cols = 4   #   A property, changes the number of columns
        # self.rows = 0   #   Likewise, for row
        self.add_widget(Label(text="First Name: "))
        self.first_name = TextInput(multiline=False)
        self.add_widget(self.first_name)

        self.add_widget(Label(text="Last Name: "))
        self.last_name = TextInput(multiline=False)
        self.add_widget(self.last_name)

        self.add_widget(Label(text="Email: "))
        self.email = TextInput(multiline=False)
        self.add_widget(self.email)

class MyApp(App):
    def build(self):
        return MyGrid()
    
if __name__ == "__main__":
    MyApp().run()