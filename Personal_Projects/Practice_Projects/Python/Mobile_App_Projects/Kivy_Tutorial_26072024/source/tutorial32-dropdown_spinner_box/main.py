"""
    Date: Thurs-1-Aug-2024

    This tutorial demonstrates implementation of drop-down spinner box

    Let me try to describe them:
        The spinners are like drop-down buttons that if clicked when collapsed, they expand and
        list other items, kind of like the Accordion but without that smooth transition.
    What's implemented
        In the code, if any of those dropped-down items (buttons) are clicked, that item's name replaces the text
        of the label, of is `click_label` and then the spinner automatically collapses the drop-down list.
    
    the Spinner can drop-down or "drop-up", depending on the space it has.
    Originally, it was dropping-up, because there was no space below; the solution was to create an
    empty label below, so that it can take up that space.


    Takeaways/Usefulness:
        1.  Can be used as part of searching UI -- for example, it can highlight the
            current file being viewed, since the Spinner takes the name of the text that is clicked.
            then when that text is clicked corresponding file is displayed in the space below it.

        2.  It can be an alternative to Accordions -- even though it does not have the transition of
            Accordions, it does not take up the space they do.
            Whereas Accordions woulf be stylish for Flash cards that are related and henced grouped together...
            The Spinner Dropdown is useful in choosing from a List of options when a button is clicked.

            So in contrast to point 1, it will be useful in listing a small number of items, as its not
            good in searching as things are not dynamically added to it (not that it cannot be)
            But seems more suitable in giving a drop down list of button options that when clicked, the text
            change of the Spinner indicate which state/option is currently active -- e.g When theme
            type 'Light' is clicked, the Spinner will indicate this -- and the `spinner_clicked` method
            can be used to cause the theme change. 
"""

from kivy.app import App
from kivy.uix.widget import Widget
from kivy.lang import Builder
from kivy.core.window import Window
from kivy.properties import ObjectProperty

Builder.load_file('base_style.kv')


class MyLayout(Widget):
    def spinner_clicked(self, spinner_text):
        """
            this changes the text of the label of id `click_label`
            to whatever the text of the spinner is.
        """
        self.ids.click_label.text = f"You Chose: {spinner_text}"
        


class MyApp(App):
    def build(self):
        self.title = "Drop-Down Spinner Box"
        Window.clearcolor = (0.15, 0.07, 0.1, 1)
        return MyLayout()
        

if __name__ == "__main__":
    MyApp().run()