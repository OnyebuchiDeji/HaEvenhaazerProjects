"""
    Date: Thurs-1-Aug-2024

    This tutorial demonstrates implementation of Checkboxes
"""

from kivy.app import App
from kivy.uix.widget import Widget
from kivy.lang import Builder
from kivy.core.window import Window
from kivy.properties import ObjectProperty

Builder.load_file('base_style.kv')

class MyLayout(Widget):
    #   Since there are more options, this keeps track of the topping
    checks = []
    ##  Didn't really need the `value` argument since I already have the `event_source.`
    def checkbox_click(self, event_source, value, topping):
        ##  The below two return the same -- since value is self.active written in Kivy stylesheet
        # print(event_source.active)
        if value:
            MyLayout.checks.append(topping)
            self.ids.output_label.text = f"You Selected: {", ".join(MyLayout.checks)}"
        else:
            MyLayout.checks.remove(topping)
            self.ids.output_label.text = f"You Selected: {", ".join(MyLayout.checks)}"

class MyApp(App):
    def build(self):
        self.title = "Checkboxes"
        Window.clearcolor = (0.1, 0.07, 0.15, 1)
        return MyLayout()
        
if __name__ == "__main__":
    MyApp().run()