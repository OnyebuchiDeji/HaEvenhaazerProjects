"""
    Date: Fri-26-July-2024
    
    Yo! World!

    Pree that the window's size is dynamic, and renders the text appropriately.
"""

import kivy
from kivy.app import App
from kivy.uix.label import Label


class MyApp(App):
    def build(self):
        self.title = "Yo World!"
        return Label(text="Yo! World!", font_size=70)



if __name__ == '__main__':
    MyApp().run()