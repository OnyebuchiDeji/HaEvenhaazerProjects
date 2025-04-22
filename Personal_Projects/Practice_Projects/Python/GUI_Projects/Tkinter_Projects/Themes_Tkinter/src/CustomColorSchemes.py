"""
    This app demonstrates the changing of themes in the Tkinter GUI

    Themes are represented using JSON files.

    What is done:
    1.  Create the theme configuration JSON files
    2.  Going to create custom `messagebox` using tk.Toplevel() to make a custom messagebox
    3.  Create function to load theme, and returns the json as Python dictionary
    4.  Create function to apply theme to the `app`, the GUI
    5.  Create function `on_theme_change()` to call  the `load_theme_from_json()` function
            and pass its returned value into the `apply_theme_to_gui()` function
    6.  The `on_theme_change` function is passed in as an argument to the `callback` parameter
        of the `trace_add` method of the global tk.StringVar object that stores the name of the
        current theme json config file.
        Basically, when the dropdown changes this variable, the callback calls the `on_theme_change` function
        which changes the theme of th egui components and updates the `current_theme` global variable.
        This variable is used to update the theme of the tk.Toplevel (popup) object when the
        `Show Message` tk.Button is pressed. 
    7.  I added my own theme `Deji_Neat`
"""

import tkinter as tk
import json
import os



def load_theme_from_json(theme_name):
    dir = "resources/"

    with open(f"{os.path.join(dir, theme_name)}.json", "r") as f:
        theme = json.load(f)
    return theme


def apply_theme_to_gui(theme):
    """
        The  `theme` returned from the json is a Python dictionary.
        Hence these.
    """
    app.config(bg=theme["background"])
    textbox.config(fg=theme['foreground'], bg=theme['background'],
                   font=(theme['font'], theme['fontsize']))
    button.config(fg=theme['foreground'], bg=theme['background'],
                   font=(theme['font'], theme['fontsize']))
    option_menu.config(fg=theme['foreground'], bg=theme['background'],
                   font=(theme['font'], theme['fontsize']))

    ##  This is the dictionary that will be updated with the current theme
    current_theme.update(theme)


def show_custom_messagebox():
    """
        It's not possible to redefine a default message box in tkinter from the
        `messagebox` module
    """
    popup = tk.Toplevel(app)
    popup.title("Messagepopup")
    popup.config(bg=current_theme["messagebox_bg"])
    msg = tk.Label(popup, text=textbox.get(), fg=current_theme['messagebox_fg'],
        bg=current_theme['messagebox_bg'])

    msg.pack(padx=20, pady=20)
    button_close = tk.Button(popup, text="Close", command=popup.destroy)
    button_close.pack(pady=20)


def on_theme_change(*args):
    #   theme_var is a string variable representing the theme name
    theme = load_theme_from_json(theme_var.get())
    apply_theme_to_gui(theme)


app = tk.Tk()
app.title("Theme Changing App")
current_theme = {}

textbox = tk.Entry(app)
#   Note the function `show_custom_messagebox` is passed in as a first-order
#   entity, an object
button = tk.Button(app, text="Show Message", command=show_custom_messagebox)

theme_var = tk.StringVar(app)
#   This is a variable that stores the theme name
theme_var.set("Classic_Elegance")
themes = ["Classic_Elegance", "Deji_Neat", "Midnight_Oasis", "Ocean_Breeze",
          "Soft_Serenity", "Sunset_Glow"]
option_menu = tk.OptionMenu(app, theme_var, *themes)

default_theme = load_theme_from_json("Classic_Elegance")
apply_theme_to_gui(default_theme)
#   Using `.trace()` in theme_var.trace("w", on_theme_change) is  depracared
#   so changed to `.trace_add` and 'write'
theme_var.trace_add("write", on_theme_change)

##  Add to the app
textbox.pack(padx=10, pady=10)
button.pack(padx=10, pady=10)
option_menu.pack(padx=10, pady=10)

app.mainloop()

# if __name__=="__main__":
#     main()