"""
    Date: Mon-12-Aug-2024

    This episode demonstrates installing use of KivyMD

    KivyMD meand "Kivy Material Design". It is a set of standards created by Google that set a
    basis or guidline for how app should look like in terms of design.
    E.g to create an android.

    This episodes involves downloading KivyMD and seeing the app that shows these things.

    The DOCS: https://kivymd.readthedocs.io/en/latest/
    Download Instructions KivyMD at https://github.com/kivymd/KivyMD
    To install it:
        git clone https://github.com/kivymd/KivyMD.git --depth 1
        cd KivyMD
        pip install .
"""

from kivy.app import App
from kivy.uix.widget import Widget
from kivy.lang import Builder


#   Designate the .kv design file
Builder.load_file("base_style.kv")

class MyLayout(Widget):
    pass


class MyApp(App):
    def build(self):
        return MyLayout()


if __name__ == "__main__":
    MyApp().run()