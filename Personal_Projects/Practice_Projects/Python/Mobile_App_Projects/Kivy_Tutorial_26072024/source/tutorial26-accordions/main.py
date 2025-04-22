"""
    Date: Wed-31-July-2024

    This tutorial demonstrates implementation of Accordions.

    Check out what accordions are, though I'll describe them:
        It's that GUI effect that when you click on a line of text, the panel, it drops down showing alot hidden
        of text.
        Then when you click on that same line of text, that lot of hidden text 'scrolls up'.
        Where there are many of these, when one panel is clicked, it causes the others to close/contract.

    So it gives this stretching and contracting effect, like an Accordian (the instrument) does.

    IDEA: Could use these to make flashcards
"""

from kivy.app import App
from kivy.uix.widget import Widget
from kivy.lang import Builder
from kivy.core.window import Window
from kivy.properties import ObjectProperty

Builder.load_file('base_style.kv')

class MyLayout(Widget):
    ...

class MyApp(App):
    def build(self):
        self.title = "Accordions"
        Window.clearcolor = (0.15, 0.07, 0.15, 1)
        return MyLayout()
        
if __name__ == "__main__":
    MyApp().run()