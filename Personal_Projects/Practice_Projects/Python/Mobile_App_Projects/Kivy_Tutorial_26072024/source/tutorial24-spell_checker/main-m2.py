"""
    Date: Wed-31-July-2024

    This tutorial follows the Method1
    But it uses a class to ellicit the same funcitonality.

"""

from kivy.app import App
from kivy.uix.widget import Widget
from kivy.uix.textinput import TextInput
from kivy.lang import Builder
from kivy.core.window import Window
from kivy.core.spelling import Spelling


Builder.load_file('base_style-m2.kv')

class MyLayout(Widget):
    def press(self):
        #   Create Instance of Spelling
        spelling = Spelling()

        #   Selct the Language
        spelling.select_language('en_US')

        #   See the language options
        # print(spelling.list_languages())

        #   Grab the word from the textbox
        word: str = self.ids.word_input.text
        options = spelling.suggest(word)

        x = ""
        for item in options:
            x = f"{x}, {item}"

        #   update the label
        self.ids.word_label.text = x
    

class SingleWordInput(TextInput):
    def insert_text(self, substring, from_undo=False):
        if not " " in substring:
            return super().insert_text(substring, from_undo=from_undo)


class MyApp(App):
    def build(self):
        self.title = "Spell Checker"
        Window.clearcolor = (0.2, 0.2, 0.2, 1)
        return MyLayout()
        
if __name__ == "__main__":
    MyApp().run()