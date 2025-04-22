"""
    Date: Thurs-15-Aug-2024 - Thurs-14-Aug-2024

    This episode demonstrates the use of KivyMD to use The MDBottomNavigation objects.

    NavigationBars or BottomNavigation objects are not Appbars; Navbars are used for Navigating between Screens
    In contrast, Appbars are used as a way of hiding tools to be used for that page or Screen.
    
    However, this episode demonstrates the use of MDNavigatorBar objects, not
    MDBottomNavigation.
    This is because use of MDBottomNavigation is limited to Kivy 1.2.0, whereas, Kivy 2.0.0 pioneers
    the use of the MDNavigationBar and hence is more robust since one has more access to the Screens
    and hence what is displayed.
    This is because using MDNavigationBar involves creation and use of Screens and a ScreenManager 
    and the `MDNavigationItem` objects used in `MDNavigationBar` require these sub-objects,
    `MDNavigationItemIcon`, `MDNavigationItemLabel` for the Icon and Labels of the NavigationItem respectively.

    But this episode I use MDNavBar because MDBottomNavigation does not work since I use Kivy 2.0.0.

    

"""

from kivymd.app import MDApp
from kivy.lang import Builder
from kivy.core.window import Window
from kivymd.theming import ThemeManager
from kivymd.uix.boxlayout import MDBoxLayout
from kivymd.uix.navigationbar import MDNavigationItem, MDNavigationBar
from kivymd.uix.label import MDLabel
from kivymd.uix.screen import MDScreen
from kivymd.uix.screenmanager import MDScreenManager
# MDNavigationBar().color
from kivy.properties import (
    ObjectProperty,
    StringProperty
)

#   Designate the .kv design file
Builder.load_file("base_style.kv")

class BaseMDNavigationItem(MDNavigationItem):
    name = StringProperty()
    icon = StringProperty()
    text = StringProperty()

class BaseScreen(MDScreen):
    screen_title = StringProperty()
    text = StringProperty()

    # def add_paragraph(self, text:str):
    #     self.add_widget(MDLabel(
    #         text=text
    #     ))
        
    def add_text(self, text: str):
        self.text += f"\n[size=20]{text}[/size]"


class MyBoxLayout(MDBoxLayout):
    pass

#   The KivyMD app
class MyApp(MDApp):
    light_theme = False
    theme_text_l = "L"
    theme_text_d = "D"
    

    def build(self):
        self.title = "KivyMD NavigationBars"
        Window.clearcolor = (0.28, 0.25, 0.3, 1)

        """ By Default, the light theme is used. """
        #   Set theme style and color palettes
        self.theme_cls.theme_style = "Light" if self.light_theme else "Dark"
        self.theme_cls.primary_palette = "Indigo"
        self.theme_cls.accent_palette = "Red"
        r: ThemeManager = self.theme_cls
        # r.Colr
        self.root = MyBoxLayout()
        return self.root

    def toggle_theme(self):
        self.light_theme = not self.light_theme
        self.theme_cls.theme_style = "Light" if self.light_theme else "Dark"
        self.root.ids.id_theme_btn.text = self.theme_text_l if self.light_theme else self.theme_text_d
    
    
    def on_switch_tabs(self, bar: MDNavigationBar, item: MDNavigationItem, item_icon: str, item_text: str):
        """
            This takes a certain number of arguments for its parameyers. And it does not in
        """
        scrn_m_ref: MDScreenManager = self.root.ids.id_screen_manager
        scrn_m_ref.current = item_text
        # scrn_ref: BaseScreen = scrn_m_ref.get_screen(item_text)
        # scrn_ref.add_paragraph(i)
    
    # def on_switch_tabs(self, *args):
    #     print(args)
    #     print(len(args))

        



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

