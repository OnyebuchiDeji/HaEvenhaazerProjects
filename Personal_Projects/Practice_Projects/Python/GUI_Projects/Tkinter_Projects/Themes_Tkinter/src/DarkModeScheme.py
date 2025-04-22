"""
    Date: Tue-11-June-2024

    Here only the core python package tkinter; no external packages, just as for the
    "CustomColorSchemes.py" work.

    What is done:
        1.  Implemented class LoginApp that is instantiated with the tk.Tk() object as a parameter
        2.  Made light_mode and dark_mode dictionaries used to change theme configuration
        3.  Created a basic login form
        4.  Created function `apply_theme` to apply the themes depending on the `is_dark_mode` flag
                This function uses the main parent Widget, the root or window, to get a list
                of all its children; and then they are looped over appropriately.
        5.  Implemented the `toggle_theme()` function hooked to the "Toggle Dark Mode" Button object
        6.  Implemented login logic
        7.  Created custom `messagebox` from popup from tk.Toplevel()
        8.  Made login logic create a CustomMessageBox with the appropriate message!
"""

import tkinter as tk

class LoginApp:
    def __init__(self, root: tk.Tk):
        self.root = root
        self.is_dark_mode = False

        #   Dictionaries to define the theme modes
        self.light_mode={
            "bg": "white",
            "fg": "black",
            "entry_bg": "#eee",
            "entry_fg": "black",
            "btn_bg": "#ddd",
            "btn_fg": "black"
        }
        self.dark_mode={
            "bg": "#333",
            "fg": "white",
            "entry_bg": "#555",
            "entry_fg": "white",
            "btn_bg": "#444",
            "btn_fg": "white"
        }

        self.label_username = tk.Label(root, text="Username")
        #   sticky=tk.W -- sticky to the West
        self.label_username.grid(row=0, column=0, padx=10, pady=10, sticky=tk.W)

        self.entry_username = tk.Entry(root)
        self.entry_username.grid(row=0, column=1, padx=10, pady=10)

        self.label_password = tk.Label(root, text="Password")
        self.label_password.grid(row=1, column=0, padx=10, pady=10, sticky=tk.W)

        #   show='*' hides the password text when being entered
        self.entry_password = tk.Entry(root, show="*")
        self.entry_password.grid(row=1, column=1, padx=10, pady=10)

        self.login_button = tk.Button(root, text="Login", command=self.login)
        self.login_button.grid(row=2, column=0, columnspan=2, pady=10)

        self.toggle_button = tk.Button(root, text="Toggle Dark Mode", command=self.toggle_theme)
        self.toggle_button.grid(row=3, column=0, columnspan=2, pady=10)

        #   To start with the custom light mode
        self.apply_theme(self.light_mode)
        
    def login(self):
        username = self.entry_username.get()
        password = self.entry_password.get()

        if username == "user" and password=="pass":
            CustomMessageBox(self.root, "Login", "Successfully Logged In!",
                self.dark_mode if self.is_dark_mode else self.light_mode)
        else:
            CustomMessageBox(self.root, "Login", "Login Failed!",
                self.dark_mode if self.is_dark_mode else self.light_mode)
            
        

    def toggle_theme(self):
        if self.is_dark_mode:
            self.apply_theme(self.light_mode)
        else:
            self.apply_theme(self.dark_mode)
        
        self.is_dark_mode = not self.is_dark_mode


    def apply_theme(self, theme):
        """
            Here every child widget belonging to the parent
            is looped over; the `self.root.winfo_children()` function returns
            a list of Widget objects.
        """
        self.root.config(bg=theme['bg'])

        for widget in self.root.winfo_children():
            #   For every widgets, get their class -- winfo == widget-info
            widget_type= widget.winfo_class()
            if widget_type == "Label":
                widget.config(bg=theme['bg'], fg=theme['fg'])
            elif widget_type == "Entry":
                widget.config(bg=theme['entry_bg'], fg=theme['entry_fg'], insertbackground=theme['fg'])
            elif widget_type == "Button":
                widget.config(bg=theme['btn_bg'], fg=theme['btn_fg'])


class CustomMessageBox(tk.Toplevel):
    def __init__(self, parent, title, message, theme):
        super().__init__(parent)
        self.theme = theme

        self.title(title)
        self.geometry('480x270')
        self.config(bg=self.theme['bg'])
        
        self.label = tk.Label(self, text=message, bg=self.theme['bg'], fg=self.theme['fg'])
        self.label.pack(padx=20, pady=20)

        #   self.destroy destroys the message box
        self.ok_button = tk.Button(self, text="OK", bg=self.theme['btn_bg'],
                                    fg=self.theme['btn_fg'], command=self.destroy)
        self.ok_button.pack(pady=10)


def main():
    root = tk.Tk()
    root.title("Login App")
    app = LoginApp(root)
    root.mainloop()

if __name__=="__main__":
    main()