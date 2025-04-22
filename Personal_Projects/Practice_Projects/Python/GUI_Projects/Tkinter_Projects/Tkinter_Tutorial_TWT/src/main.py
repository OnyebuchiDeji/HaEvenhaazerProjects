"""
    1. Made it OOP
    2.  Added check buton
    3.  Added textbox
    4.  Used condition of check button and command in normal button
        to display a message either via a messagebox or just prinintg
    5.  Added shortcut
    6.  Added exit dialog
    7.  Added Menu bar
"""

import tkinter as tk
#  note this is a separate file; that is why ut cannot be accessed this way:
#   tk.messagebox
from tkinter import messagebox 


class MyGUI:

    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Deji's GUI")

        self.menubar = tk.Menu(self.root)
        #   tear off is to remove a dash line at the top
        self.filemenu = tk.Menu(self.menubar, tearoff=0)
        
        #   `exit` refers to the basic Python exit function
        self.filemenu.add_command(label="Close Without Prompt", command=exit)
        self.filemenu.add_separator()   #   To separate options
        self.filemenu.add_command(label="Close", command=self.on_close)

        self.actionmenu = tk.Menu(self.menubar, tearoff=0)
        self.actionmenu.add_command(label="Show Message", command=self.show_message)


        self.menubar.add_cascade(menu=self.filemenu, label="File")
        self.menubar.add_cascade(menu=self.actionmenu, label="Action")

        self.root.config(menu=self.menubar)

        self.label = tk.Label(self.root, text="Your Message", font=("Arial", 18))
        self.label.pack(padx=10, pady=10)
        self.textbox = tk.Text(self.root, height=5, font=("Arial", 17))

        #   For shortcut function
        self.textbox.bind("<KeyPress>", self.shortcut)
        self.textbox.pack(padx=10, pady=10)


        self.check_state=tk.IntVar()

        self.check_btn = tk.Checkbutton(self.root, text="Show Messagebox", font=("Arial", 16),
                                    variable=self.check_state)
        #   Attaching a variable to the check button
        self.check_btn.pack(padx=10, pady=12)

        self.button = tk.Button(self.root, text="Show Message", font=("Arial", 10),
                                command=self.show_message)
        self.button.pack(padx=10, pady=10)

        self.clearbtn = tk.Button(self.root, text="Clear", font=("Arial", 18),
                                command=self.clear)
        self.clearbtn.pack(padx=10, pady=10)
        
        ##  Exit Dialog Box
        self.root.protocol("WM_DELETE_WINDOW", self.on_close)

        self.root.mainloop()



    def show_message(self):
        ##   If check box is unchecked, the below prints 0
        ##   If it is, the below prints one
        # print(self.check_state.get())
        if (self.check_state.get()):
            print("Button Checked!")
            messagebox.showinfo(title="Message", message=self.textbox.get("1.0", tk.END))
        else:
            #   Print every string in the text box
            #   Note, '1.0' -> line 1, character 0,
            #   then, tk.END -> to file End
            print((self.textbox.get("1.0", tk.END)).strip())

    def shortcut(self, event):
        # print(event)
        #   From the below keysym and state for enter = Return, 8
        #   keysym and state for Ctrl = Control_l, 8
        # keysym and state for Ctrl+Enter = Return 12
        # print(event.keysym)
        # print(event.state)
        if event.state==12 and event.keysym == "Return":
            self.show_message()

    def on_close(self):
        if (messagebox.askyesno(title="Quit?", message="Do you really want to quit?")):
            print("Closing...")
            self.root.destroy()
        else:
            print("Cool")
    
    def clear(self):
        self.textbox.delete("1.0", tk.END)


def main():
    MyGUI()


if __name__=="__main__":
    main()
