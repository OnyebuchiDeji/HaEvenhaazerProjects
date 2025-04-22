"""
    This uses an external python module called `customtkinter`
    This is differenet from the core Python module, tkinter.

    Here is a GUI for a login system -- it's a simple login system. It does not
    use databases or anything of the like.

    It's very, very simple like normal tkinter, in terms of syntax.

    But it's very eaasy to change themes and the like.

    The foreground parameter, 'fg', however, does not change the color of the text in the Widget.
    Rather, it changes the color of the parent elmenet that wraps around that widget.
    Like how, in CSS, a div can be used as a container for an element, to help in styling it...
    especially the fact that all elements have a container, especially text elements.
"""

import customtkinter

#   Can be 'Dark' or "Light" or "System", the most-latter for the system deafault
"""
    Here I change the color scheme to these:
        customtkinter.set_default_color_theme("dark-blue")
        customtkinter.set_default_color_theme("green")

"""
customtkinter.set_appearance_mode("Dark")
customtkinter.set_default_color_theme("blue")

root = customtkinter.CTk()
root.geometry("800x450")


def login():
    print("Test")



frame = customtkinter.CTkFrame(master=root)
frame.pack(padx=60, pady=20, fill="both", expand=True)

"""Note that both `fg_color` and `bg_color` do the same thing"""
label = customtkinter.CTkLabel(master=frame, text="Login System",
                                font=("Roboto", 24), fg_color="yellow", text_color="white")

label.pack(padx=10, pady=12)

entry_username = customtkinter.CTkEntry(master=frame, placeholder_text="Username")
entry_username.pack(padx=10, pady=12)
entry_password = customtkinter.CTkEntry(master=frame, placeholder_text="Password", show='*')
entry_password.pack(padx=10, pady=12)

button = customtkinter.CTkButton(master=frame, text="Login", command=login)
button.pack(padx=10, pady=12)

checkbox = customtkinter.CTkCheckBox(master=frame, text="Remember Me")
checkbox.pack(padx=10, pady=12)

root.mainloop()

