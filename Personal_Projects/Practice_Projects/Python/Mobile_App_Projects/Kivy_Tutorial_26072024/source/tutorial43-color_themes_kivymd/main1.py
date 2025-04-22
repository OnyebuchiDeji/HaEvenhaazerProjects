"""
    Date: Tue-13-Aug-2024

    This episode demonstrates the use of KivyMD to create a Color Themes

    KivyMD has a Unified Design Theory based on Goolgle's Material Design.
    It involves keeping a Color Theme and running with it, like demonstrated here

"""

from kivymd.app import MDApp
# from kivymd.uix.ra import MD
from kivy.lang import Builder
from kivy.core.window import Window

from kivy.properties import (
    ObjectProperty,
    StringProperty
)




#   The KivyMD app
class MyApp(MDApp):
    def build(self):
        self.title = "Color Themes KivyMD"
        Window.clearcolor = (0.68, 0.65, 0.7, 1)

        """ By Default, the light theme is used. """
        #   For Primary Widgets Area Colors
        self.theme_cls.primary_palette = "Blue"
        self.theme_cls.accent_palette = "Yellow"

        #   Designate the .kv design file
        return Builder.load_file("base_style1.kv")


#   'Red', 'Pink', 'Purple', 'DeepPurple',
#   'Indigo', 'Blue', 'LightBlue', 'Cyan',
#   'Teal', 'Green', 'LightGreen', 'Lime',
#   'Yellow', 'Amber', 'Orange', 'DeepOrange',
#   'Brown', 'Gray', 'BlueGray'.

if __name__ == "__main__":
    MyApp().run()