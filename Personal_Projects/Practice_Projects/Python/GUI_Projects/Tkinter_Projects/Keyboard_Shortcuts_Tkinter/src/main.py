
"""
    Mapping Keyword shortcuts/binding key events to a function.
    Then binding multiple keyboard elements to a certain function.

    For keyboard shortcuts bound to the whole Application, they have to be bound to the root
"""


import tkinter as tk
from tkinter.messagebox import showinfo
import sys



class MyApplication:
    def __init__(self):
        self.root = tk.Tk()

        self.entry = tk.Entry()
        self.entry.pack()
        ##   Return represents "Enter" -- it maps to a function
        ### M1
            # self.entry.bind("<Return>", lambda event: showinfo("Message", self.entry.get()))
        ### M2    
        ##  Note for this way, there's no need to use a lambda to pass in the 'event' argument
        self.entry.bind("<Return>", self.show_message)

        self.entry2 = tk.Entry()
        self.entry2.pack()

        self.button = tk.Button(text='Show', command=lambda: showinfo("Message", self.entry.get()))
        self.button.pack()


        """
            Some more keyboard shortcut bindings
        """
        #    To Show Dialog Message box
        self.root.bind("<Control-m>", lambda event: showinfo("Message", message="You Pressed Key 'Ctrl+ m'"))
        #   To Close Window
        self.root.bind("<Control-x>", lambda event: sys.exit())
        
        self.root.mainloop()

    def show_message(self, event):
        print(event)
        showinfo("Message", self.entry.get())


if __name__=="__main__":
    MyApplication()