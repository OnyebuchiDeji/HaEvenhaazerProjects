"""
    04-JAN-2024
    
    In this version of the app, a popup window is implemented and closing it is implemented
    The closing implementation is done by me.
    A few changes are made as in the show_popup function is made a method that returns an instance of a popup window.
    Then two method are made to show the window and to close it, which I call via the on_press attributes of the buttons...
    in the KV files!

    I use the .dismiss() method of the Popup class to close the popup window
"""

from kivy.app import App
from kivy.uix.widget import Widget
from kivy.lang import Builder
from kivy.properties import ObjectProperty
from kivy.uix.label import Label
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.popup import Popup


"""
    ELABORATE:
        1. It turns out this was not working elegantly:
        class Widgets(Widget):
            popupwindow = make_popupwindow()
        I had to define the make_popupwindow function above this Widgets class because popupWindow was a class variable...
        not a member variable
        Sol: Make it a member variable as below, and NOTE how I had to do super().__init__(**kwargs) so as to...
        not overwrite the default initialization of the Widgets object inheriting from the Widget class, so it can funciton properly.

        2. The two methods, show_popup() and close_popup() are accessed from the kivy styling file.
        NOTE! In the Kivy file, under the <PopupWndow> tag, to access the clos_popup method, I had to write:
        app.root.close_popup, because the root class of the app is the Widgets class.
        If I did root.close_popup, because the root refers to the current class's context, which is teh PopupWindow, because...
        it is under the PopupWindow tag, it will tell me that PopupWindow object has no method, close_popup()
        Sol: Make it be on_press:app.root.close_popup()

        Lastly, I have explained why Widgers is the root class of the app! In this case, it is because in the Kivy script...
        an instance of it is made by this line of code:
        Widgets:
        This is because I use a Builder which, at the program's entry point, returns the kv file:

        kv = Builder.load_file("popupwindowdeji.kv")
        class PopupWindowDeji(App):
            def build(self):
                return kv

        If I hadn't used this, this is how it would have been:

        class PopupWindowDeji(App):
            def build(self):
                return Widgets()

        and there would be no need for the "Widgets: " line of code in the KV script!
"""
class Widgets(Widget):
    """
        Added: Mon-08-01-2024
        Notice how the Button added to the widget has to be postioned?
        This is because it is not in a Layout. A Layout, either Box or Flow, would automatically position...
        GUI components such as buttons added to it!
    """
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.popupwindow = make_popupwindow()

    ##  Anytime button is pressed, the popup window comes up!
    def show_popup(self):
        self.popupwindow.open()

    def close_popup(self):
        self.popupwindow.dismiss()

"""
    Remember FloatLayouts have size_hint and pos_hint
    Popup should be a FloatLayout that has some different Widgets
"""
class PopupWindow(FloatLayout):
    pass

##  This function creates a popup window anytime it is called!
def make_popupwindow() -> Popup:
    newPopup = PopupWindow()
    ## size_hint(None, None) prevents it from dynamic resizing, just the absolute size=(400, 400)
    popupWindow = Popup(title="Popup Window", content=newPopup, size_hint=(None, None), size=(400, 400))

    return popupWindow

"""
    NOTE! Because I use the Builder, it is what I return in the build() method of the main entry-point class.
    Normally, I am meant to return the Widgets class, like return Widgets().
    Notice how, because of I don't return it, in the KV style script, I make that same class:
    Widgets:
    That line of code instantiates the widget, and so everything works.

    If I didn't use a Builder, there would be no use for that line of code in the KV file, as I would return Widgets
    class App10(App):
        def build(self):
            return Widgets()
"""
kv = Builder.load_file("popupwindowdeji.kv")

class PopupWindowDeji(App):
    def build(self):
        return kv

if __name__ == "__main__":
    PopupWindowDeji().run()