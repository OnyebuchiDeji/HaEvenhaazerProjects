"""
    03-JAN-2024
    
    In this version of the app, a popup window is implemented.
    However, closing the popup window is not implemented.
    I implement my in my PopupWindowApp.
"""

from kivy.app import App
from kivy.uix.widget import Widget
from kivy.lang import Builder
from kivy.properties import ObjectProperty
from kivy.uix.label import Label
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.popup import Popup
from kivy.uix.button import Button


"""
    NOTE Even a widget takes the size of the parent container just like layouts!
    Layouts take the size of the parent container, but can still be resized
"""
class SubWidgets(Widget):
    ##  Anytime button is pressed, the popup window comes up!
    def btn(self):
        show_popup()

class Widgets(Widget):
   flVar = ObjectProperty(FloatLayout)
   def __init__(self, **kwargs):
       super().__init__(**kwargs)
       self.w1 = SubWidgets()
       self.w2 = SubWidgets()
       self.w3 = Widget()
       self.w3.add_widget(Button(text="btn3", size=(250, 250)))
       self.w3.remo

       self.btn1 = Button(text="btn1") 
    #    self.btn1.size_hint
       self.btn2 = Button(text="btn2")
       self.btn1.pos = 50, 50
       self.btn2.pos = 75,75
       self.w3
    #    self.btn2.width = self.width
    #    self.btn2.height = self.height
    #    self.floatLayoutObj.add_widget(self.btn1)s
       self.w1.add_widget(self.btn1)
       self.w2.add_widget(self.btn2)
       self.flVar.add_widget(self.w1)
       self.flVar.add_widget(self.w2)
       self.flVar.add_widget(self.w3)
       self.flVar.remove_widget(self.w3)
    #    self.add_widget(self.w1) 
    #    self.add_widget(self.w2)
    #    self.add_widget(self.w3)
    

##  Popup should be a FloatLayout that has some different Widgets
"""
    Remember FloatLayouts have size_hint and pos_hint
"""
class PopupWindow(FloatLayout):
    pass

##  This function creates a popup window anytime it is called!
def show_popup():
    show = PopupWindow()
    ## size_hint(None, None) prevents it from dynamic resizing, just the absolute size=(400, 400)
    popupWindow = Popup(title="Popup Window", content=show, size_hint=(None, None), size=(400, 400))

    popupWindow.open()
    # popupWindow.dismiss() This closes the window

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

kv = Builder.load_file("app10.kv")
wg = Widgets()

class App10(App):
    def build(self):
        return wg

if __name__ == "__main__":
    App10().run()