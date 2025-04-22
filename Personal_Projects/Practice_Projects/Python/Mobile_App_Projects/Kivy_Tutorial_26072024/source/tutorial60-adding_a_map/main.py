"""
    Date: Mon-19-Aug-2024

    This episode demonstrates how to add a map to a Kivy app

    Requirements:
        1.  `pip install mapview`
        2.  Since kivy garden has already been installed, do `garden install mapview`
    
    This app is just the Map

"""

from kivymd.app import MDApp
from kivy.core.window import Window
from kivy.lang import Builder
from kivymd.uix.boxlayout import MDBoxLayout
from kivy_garden.mapview import MapView


#   The KivyMD app
class MapViewApp(MDApp):

    def oninit(self):
        self.title = "World Map with Kivy"
        Window.clearcolor = (0.3, 0.25, 0.3, 1)

    def build(self):
        self.oninit()

        ##  Specify the lat and long for a location on the earth surface
        ##  Note that positive(+) lat is N and negative(-) is S
        ##  Likewise positive(+) lon is E and negative(-) is W
        ##  The below is the longitude and latitude for Keele at ST5 5DZ
        mapview = MapView(zoom=10, lat=53, lon=-2.2707)

        return mapview
        
if __name__ == "__main__":
    MapViewApp().run()
