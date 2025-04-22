"""
    Example from the customtkinter github repository.
    A simple example that shows all the components a=in a high-level way, with no
    OOP structure.
"""

import tkinter as tk
import customtkinter as ctk


ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("blue")

app = ctk.CTk()
app.geometry("400x580")
app.title("CustomTkinter simple_example.py")


def btn_callback():
    print("Button Click", combobox_1.get())

def slider_callback(value):
    progressbar_1.set(value)


frame_1 = ctk.CTkFrame(master=app)
frame_1.pack(pady=20, padx=60, fill="both", expand=True)

label_1 = ctk.CTkLabel(master=frame_1, justify=tk.LEFT)
label_1.pack(pady=12, padx=10)

"""
    Consider how the `slider_1` runs the `slider_callback` anytime it detects an
    event. It even passes its value to the function IMPLICITELY, snd uses it
    to change the value of the `progressbar_1` using its `.set()` method!
"""

progressbar_1 = ctk.CTkProgressBar(master=frame_1)
progressbar_1.pack(pady=12, padx=10)

button_1 = ctk.CTkButton(master=frame_1, command=btn_callback)
button_1.pack(pady=12, padx=10)

slider_1 = ctk.CTkSlider(master=frame_1, command=slider_callback, from_=0, to=1)
slider_1.pack(pady=12, padx=10)
slider_1.set(0.5)

entry_1 = ctk.CTkEntry(master=frame_1, placeholder_text="CTkEntry")
entry_1.pack(pady=12, padx=10)

optionmenu_1 = ctk.CTkOptionMenu(frame_1, values=["Option 1", "Option 2", "option 42 long long long...."])
optionmenu_1.pack(pady=12, padx=10)
optionmenu_1.set("CTkOptionMenu")

combobox_1 = ctk.CTkComboBox(frame_1, values=["Option 1", "Option 2", "Option 42 long long long..."])
combobox_1.pack(pady=12, padx=10)
combobox_1.set("CTkComboBox")

checkbox_1 = ctk.CTkCheckBox(master=frame_1)
checkbox_1.pack(pady=12, padx=10)

radiobutton_var = tk.IntVar(value=1)

radiobutton_1 = ctk.CTkRadioButton(master=frame_1, variable=radiobutton_var, value=1)
radiobutton_1.pack(pady=12, padx=10)

radiobutton_2 = ctk.CTkRadioButton(master=frame_1, variable=radiobutton_var, value=2)
radiobutton_2.pack(pady=12, padx=10)

switch_1=ctk.CTkSwitch(master=frame_1)
switch_1.pack(pady=12, padx=10)

app.mainloop()