"""
    Date: Thurs-15-Aug-2024 - Thurs-14-Aug-2024

    This episode demonstrates the use of KivyMD to implement the SpeedDial Button

    they are like a button that, when clicked, spin out to show more widgets/buttons that can be clicked
    for a specific task.

    BUT NOTE: MDFloatingActionButtonSpeedDial were removed in kivy 2.0.0.
    So I had to use something different, the MDFabButton -- Fab for Floating Action Button

    It's like a SpinnerBox

    In the end, there was no alternative. The data attribute didn't work.
    So I created a 'Speed Dial button' myself
    it's made up of Fab Buttons

    

"""

from kivymd.app import MDApp
from kivy.lang import Builder
from kivy.core.window import Window
from kivymd.theming import ThemeManager
from kivymd.uix.boxlayout import MDBoxLayout
from kivymd.uix.label import MDLabel
from kivymd.uix.button import MDFabButton, MDExtendedFabButton, MDExtendedFabButtonIcon, MDExtendedFabButtonText

# MDNavigationBar().color
from kivy.properties import (
    ObjectProperty,
    StringProperty,
    ListProperty
)

#   Designate the .kv design file
Builder.load_file("base_style.kv")


class MyBoxLayout(MDBoxLayout):
    pass

class MyExtFab(MDExtendedFabButton):
    icon_text = StringProperty()
    text_text = StringProperty()

class SpeedDial(MDFabButton):
    # options = ListProperty()
    widgets_ref = []
    count: float = 0
    expanded = False

    def add_button_option(self, in_icon: str, in_text: str, action):
        self.count += 1
        obj = MyExtFab()
        obj.on_press = (lambda x=0: action(in_icon, in_text))
        obj.icon_text = in_icon
        obj.text_text = in_text
        center_x = self.center_x/Window.size[0]
        center_y = self.center_y/Window.size[1]
        print(center_x, center_y - self.count * 0.1)
        obj.pos_hint = {"center_x": center_x, "center_y":  center_y + 0.07 + self.count * 0.08}
        # self.parent.add_widget(obj)
        print(type(obj))
        print(obj.text_text)
        self.widgets_ref.append(obj)
        return self.widgets_ref[len(self.widgets_ref)-1]

    def remove_button_option(self):
        for widget in self.widgets_ref:
            self.parent.remove_widget(widget)
        self.count = 0
    
    def expand(self, data: dict[str, str]):
        if not self.expanded:
            # print(self.data.values())
            for icon, text in data.items():
                res = self.add_button_option(icon, text, self.what_am_i)
                # res = self.add_button_option(icon, text)
                self.parent.add_widget(res)
            self.expanded = True
        else:
            self.remove_button_option()
            self.expanded = False
            
    def what_am_i(self, icon, text):
        print(f"My text says {text} with a/an {icon} icon")


#   The KivyMD app
class MyApp(MDApp):
    light_theme = False
    theme_text_l = "L"
    theme_text_d = "D"

    ##  Key is the icon and the Value is the text
    data = {
        "language-python": "Python",
        "youtube": "Youtube",
        "instagram": "Deji's IG",
        "language-cpp": "C++",
        "language-java": "Java",
        "language-javascript": "JS",
        "language-php": "PHP",
    }
    
    def build(self):
        self.title = "KivyMD Speed Dial Button"
        Window.clearcolor = (0.28, 0.25, 0.3, 1)

        """ By Default, the light theme is used. """
        #   Set theme style and color palettes
        self.theme_cls.theme_style = "Light" if self.light_theme else "Dark"
        self.theme_cls.primary_palette = "Darkturquoise"
        # self.theme_cls.primary_palette = "Forestgreen"
        self.theme_cls.accent_palette = "Red"
        # r: ThemeManager = self.theme_cls
        self.root = MyBoxLayout()
        return self.root

    def toggle_theme(self):
        self.light_theme = not self.light_theme
        self.theme_cls.theme_style = "Light" if self.light_theme else "Dark"
        self.root.ids.id_theme_btn.text = self.theme_text_l if self.light_theme else self.theme_text_d
    






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

