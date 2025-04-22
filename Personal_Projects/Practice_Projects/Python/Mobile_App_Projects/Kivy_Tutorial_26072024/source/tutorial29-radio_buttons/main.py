"""
    Date: Thurs-1-Aug-2024

    This tutorial demonstrates implementation of Radio Buttons.
    For single selections.
    Pree how in the Kivy styling, it still uses the Check Boxes keyword, but with the
    grouping attribute.
    So each button that should be grouped to make up the Radio Buttons should
    have this attribute set to the same value.
"""

from kivy.app import App
from kivy.uix.widget import Widget
from kivy.lang import Builder
from kivy.core.window import Window
from kivy.properties import ObjectProperty

Builder.load_file('base_style.kv')


class MyLayout(Widget):
    # checks = []   Not needed for radio buttons since only one can be chosen at a time 
    def checkbox_click(self, event_source, topping):
        if event_source.active:
            # MyLayout.checks.append(topping)
            # self.ids.output_label.text = f"You Selected: {", ".join(MyLayout.checks)}"
            self.ids.output_label.text = f"You Selected: {topping}"
        else:
            # MyLayout.checks.remove(topping)
            self.ids.output_label.text = f""


class MyApp(App):
    def build(self):
        self.title = "Radio Buttons"
        Window.clearcolor = (0.1, 0.07, 0.15, 1)
        return MyLayout()
        

if __name__ == "__main__":
    MyApp().run()