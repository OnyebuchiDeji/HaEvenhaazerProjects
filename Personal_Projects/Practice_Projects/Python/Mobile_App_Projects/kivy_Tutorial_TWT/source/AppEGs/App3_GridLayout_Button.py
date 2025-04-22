import kivy
from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.gridlayout import GridLayout
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button

"""
    Date: 02-JAN-2024
   
    This version involves the implementation of adding a GridLayout and a Button!
    Adds a Button, and centers it in the GUI Bottom.
    This is done by making another grid layout inside the first, main grid layout.
    The button will be left in the main layout, while the newly made gridlayout contains the Labels and TextInput.
    Moreover, added an event, a function to be called when the button is pressed.

    It makes no use of the Kivy styling sheets, doing exavtly what was done in App5.

    It enables text input of first name, last name, email, and adds a functional submit button to print these...
    enabling one to store the input in variables! 
"""

class MyGrid(GridLayout):
    def __init__(self, **kwargs):
        # Calling GridLayout constructor
        super(MyGrid, self).__init__(**kwargs)
        self.cols = 1

        self.insideGrid = GridLayout()
        self.insideGrid.cols = 2
        # self.rows = 0   #   Likewise, for row
        self.insideGrid.add_widget(Label(text="First Name: "))
        self.first_name = TextInput(multiline=False)
        self.insideGrid.add_widget(self.first_name)

        self.insideGrid.add_widget(Label(text="Last Name: "))
        self.last_name = TextInput(multiline=False)
        self.insideGrid.add_widget(self.last_name)

        self.insideGrid.add_widget(Label(text="Email: "))
        self.email = TextInput(multiline=False)
        self.insideGrid.add_widget(self.email)

        ##  To add the new GridLayout into the main one!
        self.add_widget(self.insideGrid)

        ##  Add a Button
        self.submit = Button(text="Submit", font_size=40)

        self.submit.bind(on_press=self.intrFunc)
        self.add_widget(self.submit)

    def intrFunc(self, instance):
        self.pressed("cake!")
        print(instance.text)

    def pressed(self, sth):
        print("First Name: ", self.first_name.text)
        print("Last Name: ", self.last_name.text)
        print("Email: ", self.email.text)
        ##  Clear the input boxes after input:
        self.first_name.text = ""
        self.last_name.text = ""
        self.email.text = ""
        print(sth)


class MyApp(App):
    def build(self):
        return MyGrid()
    
if __name__ == "__main__":
    MyApp().run()