"""
    03-JAN-2024
    
    This version of the app implements having multiple windows, but more accurately, multiple screens!
    It asks for a password input, a login form, using logic to transition to teh next page!
    If the password is typed correctly, it moves to the next page. Else, it does not, and reasks for the input!
"""

from kivy.app import App
from kivy.lang import Builder
##  Importing screen and screen manager
from kivy.uix.screenmanager import ScreenManager, Screen

"""
    Note! In the KV scripts, when something like a button is declared this way:
    Button:
        text: "Deji"    ##  This is its property...
    It just makes a button in the current window.
    This is the declaration of an instance of a Button object

    But if declared this way:
    <Button>:
        text: "Deji"
        color: (1.0, 0.0, 0.0, 0.5)
    This is declaring of a template of how buttons should be made!
    This is like how css works: it is making something like a template for every button that is made...
    so that every button made gets those properties!
    It does not actually make a button 
    
"""



""""
    Most of the implementation is done in the KV file!

    Note these lines of KV script code!
    app.root.current = "Second_Screen"
    It starts with app because it needs access to current screen
    if it was must root.current, it won't work, because the root would refer to the current Screen class.
    That is, if under <OtherWindow>, it will refer to class OtherWindow, likewise with MainWindow.
    But in the case of app.root, I am trying to access another class from within the current class...
    so I need reference from the whole app
    That is why this code below works
    root.manager.transition.direction = "left"
    It refers to each screen class individually...
    The MainWindow's button causes its transition direction to move left, whereas the OtherWindow's cause it to move right!
"""
class MainWindow(Screen):
    pass

class OtherWindow(Screen):
    pass

class WindowManager(ScreenManager):
    pass

##  The builder allows one to load in the Kivy file regardless of its name! So it does not have to be...
##  The same with the app!
##  It loads up the file and returns the file when building the app
"""
    NOTE THiS! I had to add the builder after all the above classes!...
    when it was above them it did not work!
    So anytime the Builder, is to be used, because the build(self) method below has to return a gui object,
    this is the way to use it!  
"""
kv = Builder.load_file("app9.kv")


class App9(App):
    def build(self):
        return kv
    
if __name__ == "__main__":
    App9().run()
    
