"""
    Date: Sat-17-Aug-2024

    This episode demonstrates further tricks and tips that can be used with the Swiper in KivyMD
    
    These were done:
        1.  Use of buttons to navigate rather than swiping.
        2.  Attaching methods to Swiping events.

"""

from kivymd.app import MDApp
from kivy.lang import Builder
from kivy.core.window import Window
from kivymd.theming import ThemeManager
from kivymd.uix.boxlayout import MDBoxLayout
from kivymd.uix.swiper import MDSwiper, MDSwiperItem
from kivymd.uix.fitimage import FitImage

# MDNavigationBar().color
from kivy.properties import (
    ObjectProperty,
    StringProperty,
    ListProperty
)

import os

#   Designate the .kv design file
Builder.load_file("base_style.kv")


class MyBoxLayout(MDBoxLayout):
    pass


#   The KivyMD app
class MyApp(MDApp):
    light_theme = False
    theme_text_l = "L"
    theme_text_d = "D"

    def build(self):
        self.title = "KivyMD Image Swiper 2"
        Window.clearcolor = (0.3, 0.25, 0.3, 1)

        """ By Default, the light theme is used. """
        #   Set theme style and color palettes
        self.theme_cls.theme_style = "Light" if self.light_theme else "Dark"
        self.theme_cls.primary_palette = "Forestgreen"
        self.theme_cls.accent_palette = "Red"
        # r: ThemeManager = self.theme_cls
        self.root = MyBoxLayout()
        return self.root

    def toggle_theme(self):
        self.light_theme = not self.light_theme
        self.theme_cls.theme_style = "Light" if self.light_theme else "Dark"
        self.root.ids.id_theme_btn.text = self.theme_text_l if self.light_theme else self.theme_text_d
    
    def on_start(self):
        swiper_ref: MDSwiper = self.root.ids.id_swiper
        images_path = os.path.abspath(os.path.join(os.path.dirname(__file__), "../../", "resources"))
        print(images_path)

        for file in os.scandir(images_path):
            # print(file.name)
            # MDSwiperItem().
            swiper_ref.add_widget(
                MDSwiperItem(
                    FitImage(
                        source=os.path.join(images_path, file.name),
                        radius=[20,]
                    ))
            )
        
    def on_swipe_left(self):
        # print("Just Swiped Left")
        label_ref = self.root.ids.id_swipe_label
        swiper_ref:MDSwiper = self.root.ids.id_swiper
        print([attr for attr in dir(MDSwiper()) if not attr.startswith("_")])
        label_ref.text = f"[b][size=25]Swiped Left! Image ID: {swiper_ref.get_current_index()}[/size][/b]"
        print(swiper_ref)
        
    def on_swipe_right(self):
        # print("Just Swiped Right")
        label_ref = self.root.ids.id_swipe_label
        swiper_ref = self.root.ids.id_swiper
        label_ref.text = f"[b][size=25]Swiped Right! Image ID: {swiper_ref.get_current_index()}[/size][/b]"
        
    def on_overswipe_left(self):
        label_ref = self.root.ids.id_swipe_label
        swiper_ref = self.root.ids.id_swiper
        label_ref.text = f"[b][size=25]Swiped Left to The First Image! Image ID: {swiper_ref.get_current_index()}[/size][/b]"

    def on_overswipe_right(self):
        label_ref = self.root.ids.id_swipe_label
        swiper_ref = self.root.ids.id_swiper
        label_ref.text = f"[b][size=25]Swiped Right to The Last Image! Image ID: {swiper_ref.get_current_index()}[/size][/b]"

    def on_pre_swipe(self):
        print("Pree")
        
if __name__ == "__main__":
    MyApp().run()



#   'Red', 'Pink', 'Purple', 'DeepPurple',
#   'Indigo', 'Blue', 'LightBlue', 'Cyan',
#   'Teal', 'Green', 'LightGreen', 'Lime',
#   'Yellow', 'Amber', 'Orange', 'DeepOrange',
#   'Brown', 'Gray', 'BlueGray'.

"""
ThemeManager.primary_palette must be one of:
 ['Aliceblue', 'Antiquewhite', 'Aqua', 'Aquamarine', 'Azure', 'Beige', 'Bisque', 'Black', 'Blanchedalmond',
 'Blue', 'Blueviolet', 'Brown', 'Burlywood', 'Cadetblue', 'Chartreuse', 'Chocolate', 'Coral', 'Cornflowerblue',
 'Cornsilk', 'Crimson', 'Cyan', 'Darkblue', 'Darkcyan', 'Darkgoldenrod', 'Darkgray', 'Darkgrey', 'Darkgreen',
 'Darkkhaki', 'Darkmagenta', 'Darkolivegreen', 'Darkorange', 'Darkorchid', 'Darkred', 'Darksalmon', 'Darkseagreen', 'Darkslateblue',
 'Darkslategray', 'Darkslategrey', 'Darkturquoise', 'Darkviolet', 'Deeppink', 'Deepskyblue', 'Dimgray', 'Dimgrey',
 'Dodgerblue', 'Firebrick', 'Floralwhite', 'Forestgreen', 'Fuchsia', 'Gainsboro', 'Ghostwhite', 'Gold', 'Goldenrod', 'Gray',
 'Grey', 'Green', 'Greenyellow', 'Honeydew', 'Hotpink', 'Indianred', 'Indigo', 'Ivory', 'Khaki', 'Lavender', 'Lavenderblush',
 'Lawngreen', 'Lemonchiffon', 'Lightblue', 'Lightcoral', 'Lightcyan', 'Lightgoldenrodyellow', 'Lightgreen', 'Lightgray', 'Lightgrey',
 'Lightpink', 'Lightsalmon', 'Lightseagreen', 'Lightskyblue', 'Lightslategray', 'Lightslategrey', 'Lightsteelblue', 'Lightyellow', 'Lime',
 'Limegreen', 'Linen', 'Magenta', 'Maroon', 'Mediumaquamarine', 'Mediumblue', 'Mediumorchid', 'Mediumpurple', 'Mediumseagreen', 'Mediumslateblue',
 'Mediumspringgreen', 'Mediumturquoise', 'Mediumvioletred', 'Midnightblue', 'Mintcream', 'Mistyrose', 'Moccasin', 'Navajowhite', 'Navy', 'Oldlace',
 'Olive', 'Olivedrab', 'Orange', 'Orangered', 'Orchid', 'Palegoldenrod', 'Palegreen', 'Paleturquoise', 'Palevioletred', 'Papayawhip', 'Peachpuff', 'Peru',
 'Pink', 'Plum', 'Powderblue', 'Purple', 'Red', 'Rosybrown', 'Royalblue', 'Saddlebrown', 'Salmon', 'Sandybrown', 'Seagreen', 'Seashell', 'Sienna', 'Silver',
 'Skyblue', 'Slateblue', 'Slategray', 'Slategrey', 'Snow', 'Springgreen', 'Steelblue', 'Tan', 'Teal', 'Thistle', 'Tomato', 'Turquoise', 'Violet', 'Wheat', 'White',
 'Whitesmoke', 'Yellow', 'Yellowgreen']
"""

