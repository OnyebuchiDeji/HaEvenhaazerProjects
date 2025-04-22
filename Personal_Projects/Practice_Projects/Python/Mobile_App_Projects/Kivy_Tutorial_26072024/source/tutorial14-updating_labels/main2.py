"""
    Date: Sun-28-July-2024

    This tutorial demonstrates how to update Labels in Kivy
"""

from kivy.app import App
from kivy.uix.widget import Widget
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.properties import ObjectProperty
from kivy.lang.builder import Builder
from kivy.core.window import Window

Builder.load_file("source/tutorial14-updating_labels/base_style2.kv")

class MyLayout(Widget):
    def on_submit(self, event_trigerrer):
        print(event_trigerrer)

        #   Create variables for the widgets with ids
        #   one can reference the ids using `self.ids`
        #   variable fname becomes a reference that widget defined in the kivy design/style file
        fname: TextInput= self.ids.name_input

        output = f"My name is {fname.text}"         
        output = output.strip()

        #   Update the label
        self.ids.output_label.text = output

        #   Clear the input box
        fname.text = ""




class MyApp(App):
    def build(self):
        self.title = "Float Layout"
        Window.clearcolor = (0.65, 0.65, 0.65, 1)
        return MyLayout()

if __name__ == "__main__":
    MyApp().run()