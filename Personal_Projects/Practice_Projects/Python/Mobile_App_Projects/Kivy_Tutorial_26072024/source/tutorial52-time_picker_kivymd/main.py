"""
    Date: Sun-18-Aug-2024

    This episode demonstrates the use of the Time Picker.

"""

from kivymd.app import MDApp
from kivy.lang import Builder
from kivy.core.window import Window
from kivymd.theming import ThemeManager
from kivymd.uix.boxlayout import MDBoxLayout
from kivymd.uix.pickers import MDTimePickerDialHorizontal, MDTimePickerDialVertical, MDTimePickerInput

# MDNavigationBar().color
from kivy.properties import (
    ObjectProperty,
    StringProperty,
    ListProperty
)

from datetime import datetime, time

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
        self.title = "Time Picker -- KivyMD"
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
    
    def show_time_picker(self):
        # default_time = datetime.strptime("2:46:00", '%H:%M:%S')
        ##  OR 
        default_time = time.fromisoformat("02:46:00")
        self.time_dialog = MDTimePickerDialHorizontal()
        self.time_dialog.set_time(default_time)
        
        # self.time_dialog = MDTimePickerDialVertical()
        # self.time_dialog = MDTimePickerInput()


        ##  Attach to a method
        self.time_dialog.bind(on_ok=self.on_save, on_cancel=self.on_cancel)
        self.time_dialog.open()

    def close_time_picker(self):
        self.time_dialog.dismiss()
    
    #   Click okay
    def on_save(self, instance):
        print(instance)
        print([attr for attr in dir(instance) if "time" in attr])
        print(instance.time)
        # print(instance._get_time_input()) ##  This is the private method used to get the time from the UI
        # print(instance._get_dial_time(instance))
        # print(instance._time_input())   ##  This is just not the right method. It returns a WeakProxy object
        # time.strftime
        time_val = instance.time.strftime('%H:%M:%S')
        # print(type(time_val))
        
        output_label_ref = self.root.ids.id_time_label
        output_label_ref.text = "Time is {}".format(time_val)

        self.close_time_picker()

    #   Click Cancel
    def on_cancel(self, instance):
        #   Instead of using `self.date_dialog`, one can use
        # instance.dismiss()
        self.close_time_picker()
        # print(instance)
        output_label_ref = self.root.ids.id_time_label
        output_label_ref.text = "Clicked Cancel!"
    
        
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

