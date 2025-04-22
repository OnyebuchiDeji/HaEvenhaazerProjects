"""
    Date: Mon-12-Aug-2024

    This episode demonstrates the implementation of switches
"""

from kivy.app import App
from kivy.uix.widget import Widget
from kivy.lang import Builder
from kivy.core.window import Window


#   Designate the .kv design file
Builder.load_file("base_style.kv")

class MyLayout(Widget):
    def switch_clicked(self, callerWidget):
        """
            Changes Text of Lable to Indicate the State of the Switch using the `active` member
            attribute of the Switch Widget.
            Furthermore, when using Markup, the markup language in the text must be enclosed
            in square brackets '[]' else the markup language text/tag will show and markup won't
            take true effect.

            However, this logic was done in the .kv design file.
        """
        #   All that is needed to be done here
        switch_state = callerWidget.active
        #   No need to set this here since it's already been set in the .kv design file
        # callerWidget.markup = True
        print(switch_state)
        
        """Logic done in KV design file"""
        # if (switch_state):
        #     self.ids.switch_state_label.text = f"[size=100][b]Switch State: {"On"}[/b][/size]"
        # else:
        #     self.ids.switch_state_label.text = f"[size=100][b]Switch State: {"Off"}[/b][/size]"

    def toggle_switch_disable(self):
        switch_ref = self.ids.my_switch
        switch_ref.disabled = not switch_ref.disabled

class MyApp(App):
    def build(self):
        self.title = "Switches"
        Window.clearcolor = (0.15, 0.07, 0.1, 1)
        return MyLayout()


if __name__ == "__main__":
    MyApp().run()