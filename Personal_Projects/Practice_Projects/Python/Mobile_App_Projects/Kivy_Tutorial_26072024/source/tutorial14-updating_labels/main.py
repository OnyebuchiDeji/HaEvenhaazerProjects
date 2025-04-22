"""
    Date: Sun-28-July-2024

    This tutorial demonstrates how to update Labels in Kivy.
    This tutorial was done without looking at the actual tutorial.

    But main2.py and base_style2.kv demonstrates another way to access the ids of widgets.
    from the kivy design/style file 
"""

from kivy.app import App
from kivy.uix.widget import Widget
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.properties import ObjectProperty
from kivy.lang.builder import Builder
from kivy.core.window import Window

Builder.load_file("source/tutorial14-updating_labels/base_style.kv")

class MyLayout(Widget):
    fname :TextInput = ObjectProperty(TextInput)
    lname :TextInput = ObjectProperty(TextInput)
    age :TextInput = ObjectProperty(TextInput)
    more_info :TextInput = ObjectProperty(TextInput)
    output_label : Label = ObjectProperty(Label)

    def on_submit(self, event_trigerrer):
        print(event_trigerrer)

        fname= self.fname.text
        lname = self.lname.text
        age = self.age.text
        more_info = self.more_info.text

        output = f"""My name is {fname} {lname} and I am {age} years old.\n"""
        output+= f"Here is more information about me:\n {more_info}"         
        
        output = output.strip()
        self.output_label.text = output

        self.fname.text = ""
        self.lname.text = ""
        self.age.text = ""
        self.more_info.text = ""




class MyApp(App):
    def build(self):
        self.title = "Float Layout"
        Window.clearcolor = (0.65, 0.65, 0.65, 1)
        return MyLayout()

if __name__ == "__main__":
    MyApp().run()