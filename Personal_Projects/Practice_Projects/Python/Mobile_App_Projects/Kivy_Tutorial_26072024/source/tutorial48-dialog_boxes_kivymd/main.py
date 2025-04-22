"""
    Date: Fri-16-Aug-2024 - Thurs-14-Aug-2024

    This episode demonstrates the use of Dialog Boxes in KivyMD
    

"""

from kivymd.app import MDApp
from kivy.lang import Builder
from kivy.core.window import Window
from kivymd.theming import ThemeManager
from kivymd.uix.boxlayout import MDBoxLayout
from kivymd.uix.dialog import (
    MDDialog, MDDialogIcon, MDDialogHeadlineText,
    MDDialogSupportingText, MDDialogContentContainer,
    MDDialogButtonContainer
)
from kivymd.uix.divider import MDDivider
from kivymd.uix.list import (
    MDListItem,
    MDListItemLeadingIcon,
    MDListItemSupportingText
)
from kivymd.uix.button import MDButton, MDButtonText
from kivy.uix.widget import Widget


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


#   The KivyMD app
class MyApp(MDApp):
    light_theme = False
    theme_text_l = "L"
    theme_text_d = "D"
    dialog_obj = None


    def build(self):
        self.title = "KivyMD Dialog Boxes"
        Window.clearcolor = (0.28, 0.25, 0.3, 1)

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

    def show_alert_dialog(self, msg):
        if not self.dialog_obj:
            self.dialog_obj: MDDialog = MDDialog(
                MDDialogIcon(icon="alert"),
                MDDialogHeadlineText(text="Alert"),
                MDDialogSupportingText(
                    text=msg
                ),
                MDDialogButtonContainer(
                    Widget(),
                    MDButton(
                        MDButtonText(text="CANCEL"),
                        style="text",
                        on_release=self.close_alert_dialog
                    ),
                    MDButton(
                        MDButtonText(text="ACCEPT"),
                        style="text",
                        on_release=self.dialog_conclude
                    ),
                    spacing="8dp",
                ),
            )
            self.dialog_obj.open()
    
    def close_alert_dialog(self, objRef=None):
        #   Close Dialog
        self.dialog_obj.dismiss()
        self.dialog_obj = None
    
    def dialog_conclude(self, obj):
        #   Close Dialog
        self.close_alert_dialog()
        self.root.ids.id_my_label.text = "Indeed, Preee the Dialog Box!"


    def show_alert_dialog_v2(self):
        if not self.dialog_obj:
            self.dialog_obj:MDDialog = MDDialog(
                MDDialogIcon(icon="refresh"),
                MDDialogHeadlineText(text="Reset Settings?"),
                MDDialogSupportingText(
                    text="This will reset your app preferences back to their "
                    "default settings. The following accounts will also "
                    "be signed out:"
                    ),
                MDDialogContentContainer(
                    MDDivider(),
                    MDListItem(
                        MDListItemLeadingIcon(
                            icon="gmail",
                        ),
                        MDListItemSupportingText(
                            text="evenhaazer335@gmail.com"
                        ),
                        theme_bg_color="Custom",
                        md_bg_color=self.theme_cls.transparentColor,
                    ),
                    MDListItem(
                        MDListItemLeadingIcon(
                            icon="gmail",
                        ),
                        MDListItemSupportingText(
                            text="ebenayo10@gmail.com"
                        ),
                        theme_bg_color="Custom",
                        md_bg_color=self.theme_cls.transparentColor,
                    ),
                    MDDivider(),
                    orientation="vertical",
                ),
                MDDialogButtonContainer(
                    Widget(),
                    MDButton(
                        MDButtonText(text="CANCEL"),
                        style="text",
                    ),
                    MDButton(
                        MDButtonText(text="ACCEPT"),
                        style="text",
                    ),
                    spacing="8dp",
                ),
            )
            self.dialog_obj.open()
    

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

