"""
    03-JAN-2024

    This Version shows the implementation of mouse and finger input!
"""

import kivy
from kivy.app import App
from kivy.uix.widget import Widget
from kivy.properties import ObjectProperty

"""
    In this version, a button is added to the Widget class, Touch.
    Then the already-defined methods, the on_touch methods that detect mouse and screen touches are overwritten.
"""


class Touch(Widget):
    """"
        These functions are inherited from the Widget class and are overwritten here
        The touch parameter enables one to get the positions of where has been pressed when one...
        touches the screen!
        When the touch events are enabled, anytime the button is touched, it no more changes the buttons' colors.
        The reason is because in the Touch class, trhe on_touch methods are overwritten.
        Normally, these methods will detect the change of the state of the button and change its color as a result.
        But because it has been overwritten to just print the position of the mouse, it no more has the prior function.
        To fix this, the function is done manually by me by adding an ObjectProperty to refer to the button!
     """
    ##  The Object Property reference to a specific Button
    btnVar = ObjectProperty(None)

    def on_touch_down(self, touch):
        print("Mouse Down!", touch)
        #   Accessing the class variable is still done self.
        #   This makes the button look more transparent when touched!
        self.btnVar.opacity = 0.5

    def on_touch_move(self, touch):
        print("Mouse Moved!", touch)

    def on_touch_up(self, touch):
        print("Mouse Up!", touch)
        #   THis makes the button look normal, more opaque when released!
        self.btnVar.opacity = 1

class App7(App):
    def build(self):
        return Touch()

if __name__== "__main__":
    App7().run()