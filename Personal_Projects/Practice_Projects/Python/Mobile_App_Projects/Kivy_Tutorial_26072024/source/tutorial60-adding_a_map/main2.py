"""
    Date: Mon-19-Aug-2024

    This episode demonstrates how to add a map to a Kivy app using the Kivy Design file

    Requirements:
        1.  `pip install mapview`
        2.  Since kivy garden has already been installed, do `garden install mapview`

"""

from kivymd.app import MDApp
from kivy.core.window import Window
from kivy.lang import Builder
from kivymd.uix.boxlayout import MDBoxLayout
from kivy_garden.mapview import MapView


class MyBoxLayout(MDBoxLayout):
    ...
    

#   The KivyMD app
class MapViewApp(MDApp):
    light_theme = False
    theme_text_l = "L"
    theme_text_d = "D"
    
    def oninit(self):
        self.title = "World Map with Kivy"
        Window.clearcolor = (0.3, 0.25, 0.3, 1)
        self.theme_cls.theme_style = "Light" if self.light_theme else "Dark"
        self.theme_cls.primary_palette = "Forestgreen"
        self.theme_cls.accent_palette = "Red"

    def build(self):
        self.oninit()

        ##  Specify the lat and long for a location on the earth surface
        ##  Note that positive(+) lat is N and negative(-) is S
        ##  Likewise positive(+) lon is E and negative(-) is W
        ##  The below is the longitude and latitude for Keele at ST5 5DZ
        mapview = MapView(zoom=10, lat=53, lon=-2.2707)

        #   Designate the .kv design file
        Builder.load_file("base_style2.kv")
        self.root = MyBoxLayout()
        return self.root

    def toggle_theme(self):
        self.light_theme = not self.light_theme
        self.theme_cls.theme_style = "Light" if self.light_theme else "Dark"
        self.root.ids.id_theme_btn.text = self.theme_text_l if self.light_theme else self.theme_text_d
        
        
if __name__ == "__main__":
    MapViewApp().run()
