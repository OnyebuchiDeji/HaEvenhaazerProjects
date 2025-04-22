"""
    Date: Tue-13-Aug-2024

    This episode demonstrates the use of KivyMD to create a Color Themes

    KivyMD has a Unified Design Theory based on Goolgle's Material Design.
    It involves keeping a Color Theme and running with it, like demonstrated here.

    Unlike in the tutorial, the theme colors of the individual buttons could not be changed
    as shown in the episode.
    Only defining the `theme_style`, `primary_palette`, and `accent_palette` worked.

"""

from kivymd.app import MDApp
from kivymd.uix.button import MDButton
from kivy.lang import Builder
from kivy.core.window import Window
from kivymd.theming import ThemeManager

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
        #   Set theme style
        self.theme_cls.theme_style = "Light"
        #   For Primary Widgets Area Colors
        self.theme_cls.primary_palette = "Indigo"
        self.theme_cls.accent_palette = "Red"

        # MDButton().color

        # ref: ThemeManager = self.theme_cls
        # ref.surfaceTintColor
        # ref.surfaceDimColor
        # ref.scrimColor
        # ref.primaryColor
        # ref.rippleColor
        # ref.shadowColor
        # ref.inversePrimaryColor
        # ref.inverseSurfaceColor
        # ref.tertiaryColor
        # ref.color

        #   Designate the .kv design file
        return Builder.load_file("base_style2.kv")


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

if __name__ == "__main__":
    MyApp().run()