"""
    Date: Mon-19-Aug-2024

    This episode demonstrates how to add a Keyboard in the Kivy App.
"""

from kivymd.app import MDApp
from kivy.core.window import Window
from kivy.lang import Builder
from kivymd.uix.boxlayout import MDBoxLayout
from kivy.uix.vkeyboard import VKeyboard
from kivy.uix.label import Label
from kivy.uix.gridlayout import GridLayout

class MyBoxLayout(MDBoxLayout):
    ...
    

#   The KivyMD app
class MyApp(MDApp):
    light_theme = False
    theme_text_l = "L"
    theme_text_d = "D"

    
    def oninit(self):
        self.title = "Keyboard in Kivy App"
        Window.clearcolor = (0.3, 0.25, 0.3, 1)
        self.theme_cls.theme_style = "Light" if self.light_theme else "Dark"
        self.theme_cls.primary_palette = "Firebrick"
        self.theme_cls.accent_palette = "Floralwhite"
    
    def build_screen_widgets(self):
        #   Define Our Layout
        layout = GridLayout(cols=1, rows=2, size_hint=(1.0, 1.0),)
        #   Define Our Keyboard
        keyboard = VKeyboard(on_key_up=self.key_up, pos_hint={"center_x":.5})
        #   Define Label
        self.label = Label(
            text = "Anticipating What You'll type...",
            font_size = "20sp",
            color="white",
            size_hint = (1.0, 0.8),
            halign = "center",
            valign = "middle"
        )
        self.label.text_size = (700, 600)
        layout.add_widget(self.label)
        layout.add_widget(keyboard)

        self.root.ids["id_screen"].add_widget(layout)

    def build(self):
        self.oninit()

        #   Designate the .kv design file
        Builder.load_file("base_style.kv")
        self.root = MyBoxLayout()

        return self.root
    
    def on_start(self):
        self.build_screen_widgets()


    def toggle_theme(self):
        self.light_theme = not self.light_theme
        self.theme_cls.theme_style = "Light" if self.light_theme else "Dark"
        self.root.ids.id_theme_btn.text = self.theme_text_l if self.light_theme else self.theme_text_d
    
    def key_up(self, keyboard, keycode, *args):
        # print(keyboard) #   This gives the Keyboard object's memory address
        # print(keycode)      #   This just prints the keycode
        # print(args)     ##  This prints the tuple with the key character/code

        ##  From Episode: The below won't work because the keycode is indeed not a tuple
        # if isinstance(keycode, tuple):    Dont't know the use of this
            # keycode = keycode[1]
        ##  Correct form:
        if isinstance(args, tuple):
            keycode_char = args[0]

        ##  Rather just do:
            # keycode_char = keycode

        ##  This prints the String form of every key pressed
        ##  E.g. If "Shift" key is pressed, it prints "shift"
        print(keycode) 
        ##  Whereas the below will print None if keys like "Shift" is pressed
        ##  So this one is the best to be used
        print(keycode_char)

        match keycode:
            # case "shift":

            case "backspace":
                self.label.text = self.label.text[:len(self.label.text)-1:]
            case "tab":
                if self.label.text == "Anticipating What You'll type...":
                    self.label.text = ""
                ##  Because the keycode_char for a tab is just 1
                ##  But a tab is by default 4 spaces, hence the below
                for i in range(4):
                    self.label.text += " "
                    print("Tab Pressed")
            case "enter":
                if self.label.text == "Anticipating What You'll type...":
                    self.label.text = ""
            
                self.label.text += "\n"

            case _:
                if keycode_char is not None:
                    if self.label.text == "Anticipating What You'll type...":
                        self.label.text = ""
            
                    self.label.text += keycode_char

        
        
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

