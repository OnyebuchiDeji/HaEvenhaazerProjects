"""
        Date: 02-JAN-2024

    In this script, the members of the objects would be accessed from the kivy file script

    It does exactly what the App3 does; it enables text input of first name, last name, email, and adds a functional submit button to print these...
    enabling one to store the input in variables! But it does all of this in the kv style sheet!
    It does this with the use of the ObjectProperty objects, which reference the ids used in the Kivy Style scripts!
"""

import kivy
from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.gridlayout import GridLayout
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.uix.widget import Widget
from kivy.properties import ObjectProperty

"""
    program_ref: id

    the program_ref can be accessed from within the code, to get the id.
    Also, the name of the program_ref nd the id should be the same!
"""

class MyGrid(Widget):
    ##  These are class variables and so can be referenced with self. as done in funciton btn()
    ##  Making the nameVar and emailVar Object properties so that they can reference from the KV file. 
    nameVar = ObjectProperty(None)
    emailVar = ObjectProperty(None)

    ##  In the kivy file, the button is referenced using root.btn().
    ##  Note that the root for the function btn is the MyGrid class.
    ##  So root.btn() refers to the btn function in MyGrid
    def btn(self, sth):
        print("Name: ", self.nameVar.text, "Email: ", self.emailVar.text)
        self.nameVar.txt = ""
        self.emailVar.txt = ""
        aVar = sth
        print(aVar)

class App5(App):
    def build(self):
        return MyGrid()

if __name__== "__main__":
    App5().run()