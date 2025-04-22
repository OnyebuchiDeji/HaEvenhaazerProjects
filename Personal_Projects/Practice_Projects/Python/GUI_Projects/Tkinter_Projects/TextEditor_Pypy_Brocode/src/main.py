"""
    Done following Bro Code.

    These were done:
        1.  Made text editor layout and everything
        2.  Added buttons:
                1.  One to bring out a `colorchooser`.
                2.  Another that enabled one to display every system font to change the font of their text
                3.  Another that allowed one to change the font-size using a spinbox, to increment font size
                    and it changed live.
        3.  Added Menu bar and Menu options with different commands.
            there were commands to QUIT, PASTE, COPY, and CUT.


"""

import tkinter as tk
from tkinter import filedialog, colorchooser, font
from tkinter import messagebox as tkmsgbx
from tkinter import filedialog as tkfd

import os


def change_color():
    color=colorchooser.askcolor(title="Pick a Color")
    # print(color)    #   Prints a tuple of RGB and Hex form
    text_area.config(fg=color[1])

def change_font(*args):
    text_area.config(font=(font_name.get(), size_box.get()))

def new_file():
    window.title(window_title + ": Untitled")
    #   Remember it means: line 1, character pos 0, to END of file
    text_area.delete(1.0, tk.END)

def open_file():
    #   To view and accept all files as well as text files
    file_path = tkfd.askopenfilename(defaultextension=".txt",
                                file=[("All Files", "*.*"),
                                ("Text Documents", "*.txt")])

    try:
        window.title(f"{window_title}: {os.path.basename(file_path)}")
        #   Empty File
        text_area.delete(1.0, tk.END)

        file = open(file_path, "r")

        text_area.insert(1.0, file.read())
        print("File Read")
    
    except [FileExistsError, FileExistsError, Exception] as errors:
        print("Couldn't read file!")
        [print(error) for error in errors]

    finally:
        file.close()
        
        


def save_file():
    file_path = tkfd.asksaveasfilename(initialfile="untitled.txt",
                                       defaultextension=".txt",
                                       filetypes=[("All Files", "*.*"),
                                                  ("Text Documents", "*.txt")])
    if (file_path is None):
        return
    else:
        try:
            window.title(f"{window_title}: {os.path.basename(file_path)}")
            file = open(file_path, "w")

            file.write(text_area.get(1.0, tk.END))
            print("File Saved!")
        
        except [FileExistsError, FileExistsError, Exception] as errors:
            print("Couldn't save file!")
            [print(error) for error in errors]

        finally:
            file.close()


def cut():
    text_area.event_generate("<<Cut>>")

def copy():
    text_area.event_generate("<<Copy>>")

def paste():
    text_area.event_generate("<<Paste>>")

def about():
    tkmsgbx.showinfo("About this program", "It was written on Thursday 12 June 2024.\
                    This day is actually my elder brother's birthday.\
                    I wrote this program following Bro Code from Youtube.\
                    It is a program I have wanted to do for some time.")

def quit():
    window.destroy()



window = tk.Tk()
window_title = "Deji Text Editor"
window.title(window_title)
file_path = None

window_width, window_height = 500, 500
screen_width = window.winfo_screenwidth()
screen_height = window.winfo_screenheight()

#   For the displacement of the Window position on computer's screen
#   to center it
x = int(screen_width / 2 - (window_width / 2))
y = int(screen_height / 2 - (window_height / 2))

window.geometry("{}x{}+{}+{}".format(window_width, window_height, x, y))

font_name = tk.StringVar(window)
font_name.set("Arial")

font_size = tk.StringVar(window)
font_size.set("20")

text_area = tk.Text(window, font=(font_name.get(), font_size.get()))

#   Scrollbar of Text Area  #
scroll_bar = tk.Scrollbar(text_area)

##  Allows text area to expand by changing the grid's first column's size
window.grid_rowconfigure(0, weight=1)
window.grid_columnconfigure(0, weight=1)
text_area.grid(sticky=tk.N + tk.E + tk.S + tk.W)
scroll_bar.pack(side=tk.RIGHT, fill=tk.Y)
text_area.config(yscrollcommand=scroll_bar.set)


#   For Buttons, Option Menu, and Spin Box?
##  They are placed in this frame
frame = tk.Frame(window)
frame.grid()


color_button = tk.Button(frame, text="Change Color", command=change_color)
color_button.grid(row=0, column=0)


#   Adding all the fonts to the option menu
##  the *font.families() is imported, and the .families() is its method
font_box = tk.OptionMenu(frame, font_name, *font.families(), command=change_font)
font_box.grid(row=0, column=1)

#   A Spin Box -- increases or decreases the font
size_box= tk.Spinbox(frame, from_=1, to=100, textvariable=font_size, command=change_font)
size_box.grid(row=0, column=2)

##  Various drop-down menus

menu_bar = tk.Menu(window)
#   Add the above menu to the window
window.config(menu=menu_bar)

#   tearoff removes a dashed overline
file_menu = tk.Menu(menu_bar, tearoff=0)
menu_bar.add_cascade(label="File", menu=file_menu)
file_menu.add_command(label="New", command=new_file)
file_menu.add_command(label="Open", command=open_file)
file_menu.add_command(label="Save", command=save_file)
file_menu.add_separator()
file_menu.add_command(label="Quit", command=quit)

edit_menu = tk.Menu(menu_bar, tearoff=0)
menu_bar.add_cascade(label="Edit", menu=edit_menu)
edit_menu.add_command(label="Cut", command=cut)
edit_menu.add_command(label="Copy", command=copy)
edit_menu.add_command(label="Paste", command=paste)

help_menu = tk.Menu(menu_bar, tearoff=0)
menu_bar.add_cascade(label="Help", menu=help_menu)
help_menu.add_command(label="About", command=about)

window.mainloop()