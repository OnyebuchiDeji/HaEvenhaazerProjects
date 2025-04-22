"""
    Date: Sun-18-Aug-2024

    This episode demonstrates an introduction into the use of DataTables with KivyMD.

    This code demonstratees creating the Data Table only in this Python file; not in the Kivy file
    Hence the Builder is not used.

    However, unfortunately, KivyMD 2.0.0 does not have DataTable. I checked but still can't import it.
    It was removed from KivyMD.
    
    `dp` means `dispaly_pixels`

    This episode demonstrates Pagination of the Data Tables:
        1.  That is, one can click a Arrow Button to slide to a different page to view more data in the Data table.
        2.  One can choose the `Rows per Page` and the Range of Values on that page is indicated. E.g. (1-6 of 26) 
        3.  the `use_pagination` Boolean is used to make pagination enabled
        4.  `rows_num` attribute is used to indicate the number of rows shown per page
        5.  `pagination_menu_height` changes the height of the menu for the `Rows-per-Page` menu. for me it will just be size_hint_y or size
        6.  'pagination_menu_position' is used to change the position of the menu. For me it will just be pos_hint
    Note that every page stil shows the Header Row.
    This is an alternative to being able to Scroll Along the Height
"""

from kivymd.app import MDApp
from kivy.lang import Builder
from kivy.core.window import Window
from kivymd.theming import ThemeManager
from kivymd.uix.boxlayout import MDBoxLayout
from kivymd.uix.screen import MDScreen
from kivymd.uix.datatables import MDDataTable
from kivy.metrics import dp

# MDNavigationBar().color
from kivy.properties import (
    ObjectProperty,
    StringProperty,
    ListProperty
)

# from datetime import datetime, time


#   The KivyMD app
class MyApp(MDApp):
    light_theme = False
    theme_text_l = "L"
    theme_text_d = "D"


    def build(self):
        self.title = "Data Tables 2 -- KivyMD"
        Window.clearcolor = (0.3, 0.25, 0.3, 1)

        """ By Default, the light theme is used. """
        self.theme_cls.theme_style = "Light" if self.light_theme else "Dark"
        self.theme_cls.primary_palette = "Forestgreen"
        self.theme_cls.accent_palette = "Red"

        #   Define the Screen
        screen = MDScreen()

        #   Define Table
        table = MDDataTable(
            size_hint = (0.9, 0.6),
            pos_hint = {"center_x":0.5, "center_y":0.5},
            check = True,
            use_pagination = True,              #   Set Pagination
            rows_num = 3,                       #   Specifies the number of rows to show per page
            pagination_menu_height = '120dp',
            pagination_menu_pos = 'center',     #   Can be 'auto' But it wasn't working
            background_color = [1, 0, 0, .5],
            column_data = [
                ("First Name", dp(30)),
                ("Last Name", dp(30)),
                ("Email Address", dp(30)),
                ("Phone Number", dp(30)),
            ],
            row_data = [
                ("Deji", "Ayo-Metibemu", "evenhaazer335@gmail.com", "+447926740709"),
                ("Eben", "Ayo-Metibemu", "evenhaazerayo@gmail.com", "+2349063902481"),
                ("Even", "Ayo-Metibemu", "zayoeven335@gmail.com", "+2349035470731"),
                ("Haezer", "Ayo-Metibemu", "haezer335@gmail.com", "+2343420194300"),
                ("Deji", "Ayo-Metibemu", "evenhaazer335@gmail.com", "+447926740709"),
                ("Eben", "Ayo-Metibemu", "evenhaazerayo@gmail.com", "+2349063902481"),
                ("Even", "Ayo-Metibemu", "zayoeven335@gmail.com", "+2349035470731"),
                ("Haezer", "Ayo-Metibemu", "haezer335@gmail.com", "+2343420194300"),
                ("Deji", "Ayo-Metibemu", "evenhaazer335@gmail.com", "+447926740709"),
                ("Eben", "Ayo-Metibemu", "evenhaazerayo@gmail.com", "+2349063902481"),
                ("Even", "Ayo-Metibemu", "zayoeven335@gmail.com", "+2349035470731"),
                ("Haezer", "Ayo-Metibemu", "haezer335@gmail.com", "+2343420194300"),
            ]
        )

        ##  Bind Table to a Method
        table.bind(on_check_press=self.checked)
        table.bind(on_row_press=self.row_cell_clicked)

        ##  Add Table Widget to Screen
        screen.add_widget(table)
        
        self.root = screen
        return self.root

    def checked(self, instance, current_row):
        """
            When the Check Button for the Row is clicked...
            `current_row` should return the row's data in a list
        """
        print("Checked Button Clicked!")

    def row_cell_clicked(self, instance, instance_row):
        """
            When a Cell in the Row is clicked, it should return the Cell object called 'CellRow' object
        """
        print("Row Clicked!")
        


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

