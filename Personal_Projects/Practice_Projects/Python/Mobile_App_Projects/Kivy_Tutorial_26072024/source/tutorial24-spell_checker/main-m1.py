"""
    Date: Wed-31-July-2024

    This tutorial demonstrates the implementation of a spell checker built-in in Kivy
    This requires the library, PyEnchant:
            ```pip install PyEnchant```
        though it is used implicitely by the kivy Spelling class

    This Method1 shows the modifying of the TextInput to only allow one word
    to be entered.
    It overides the `insert_text` method of the TextInput defined in the Kivy Stylesheet
    The logic shows how it prevents anything from being enetered when a space is clicked.
    It does this without needing to create another class.

    In contrast, the method2 does create another class.
    Here is reference to where the idea came from:
        https://kivy.org/doc/stable/api-kivy.uix.textinput.html#module-kivy.uix.textinput


"""

from kivy.app import App
from kivy.uix.widget import Widget
from kivy.uix.textinput import TextInput
from kivy.lang import Builder
from kivy.core.window import Window
from kivy.core.spelling import Spelling


Builder.load_file('base_style-m1.kv')

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
    
    def insert_text(self, substring, from_undo):
        if not " " in substring:
            self.ids.word_input.text += substring


class MyApp(App):
    def build(self):
        self.title = "Spell Checker"
        Window.clearcolor = (0.2, 0.2, 0.2, 1)
        return MyLayout()
        
if __name__ == "__main__":
    MyApp().run()