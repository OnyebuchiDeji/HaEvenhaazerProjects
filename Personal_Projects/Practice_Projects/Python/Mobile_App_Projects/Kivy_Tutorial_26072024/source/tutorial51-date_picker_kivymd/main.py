"""
    Date: Sun-18-Aug-2024

    This episode demonstrates the use of the Date Picker.

"""

from kivymd.app import MDApp
from kivy.lang import Builder
from kivy.core.window import Window
from kivymd.theming import ThemeManager
from kivymd.uix.boxlayout import MDBoxLayout
from kivymd.uix.pickers import MDModalDatePicker, MDModalInputDatePicker, MDDockedDatePicker

# MDNavigationBar().color
from kivy.properties import (
    ObjectProperty,
    StringProperty,
    ListProperty
)

# import datetime

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
        self.title = "Date Picker -- KivyMD"
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
    
    def show_date_picker(self):
        ##  This is the normal one. It's modal.
        ##  The arguments set the default date.
        # self.date_dialog = MDModalDatePicker(year=2005, month=4, day=15)
        self.date_dialog = MDModalDatePicker(mode="range")

        ##  This is also modal. But is for one to input a Date. E.g. One's date of birth.
        # self.date_dialog = MDModalInputDatePicker(year=2005, month=4, day=15)

        ##  This one is docked.
        # self.date_dialog = MDDockedDatePicker(year=2005, month=4, day=15,
            # pos_hint = {"right":1}  #   This is used to change the eposition that it docks to
        # )

        ##  Attach to a method
        self.date_dialog.bind(on_ok=self.on_save, on_cancel=self.on_cancel)
        self.date_dialog.open()

    def close_date_picker(self):
        self.date_dialog.dismiss()
    
    #   Click okay
    def on_save(self, instance):
        """
            1. With the instance, I can get the chosen Date value and the Date range.
               Kivy 2.0.0 does pass in the value (date) and date_range as arguments to the bound functions 

            Date range is gotten by using: _get_date_range or compare_date_range.
            But to get range, set the mode of the DatePicker to range
            # print(instance, value, date_range)    ##  From episode. Not doable in Kivy 2.0.0 (using the arguments)

        """
        # print(instance.compare_date_range())
        
        print([attr for attr in dir(instance) if "mode" in attr])
        print(f"Ctime: {instance.get_date()[0].ctime()}")
        print(f"Year: {instance.get_date()[0].year}")
        print(f"Day: {instance.get_date()[0].day}")
        #   Returns the chosen date as a datetime.date object
        print(f"Date (Type datetime.date): {instance.get_date()[0]}")
        print(f"Selected Data Range (Only works in `mode='range'`): f{instance._get_date_range()}")   ##  Returns a Python list
        date = instance.get_date()[0].strftime("%d/%m/%Y")
        range_val = f"{instance._get_date_range()[0]} - {instance._get_date_range()[len(instance._get_date_range()) -1]}"
        output_label_ref = self.root.ids.id_date_label
        if instance.mode != "range":
            output = date
            output_label_ref.text = "Date is {}".format(date)
        else:
            output = range_val
            output_label_ref.text = "Date Range Selected:\n {}".format(range_val)

        self.close_date_picker()

    #   Click Cancel
    def on_cancel(self, instance):
        #   Instead of using `self.date_dialog`, one can use
        # instance.dismiss()
        print(instance)
        self.close_date_picker()
        output_label_ref = self.root.ids.id_date_label
        output_label_ref.text = "Clicked Cancel"
    
        
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

