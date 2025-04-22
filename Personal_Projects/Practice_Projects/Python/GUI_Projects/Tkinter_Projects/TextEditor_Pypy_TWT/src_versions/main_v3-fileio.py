"""
    date: Tue-11-June-2024

    1.  Create Window
    2.  Add title
    3.  Create Text Area widget
    4.  Initialize main loop
    5.  Determine the size of widget by setting size of column it's added in.
    6.  Add `frame` widget and two buttons within it.
    7.  Make `frame` widget fill the column area it occupies using sticky
    8.  Add padding to buttons to separate them, then use sticky to make them have
        the same size, stretching them along the `frame` widget's full width
    9.  Made buttons do things
            Use the `command` property to attach functions to actions on the button
    10. use `askopenfilename`, `asksaveasfilename` functions
    11. Create the open_file and save_file functions and attach to approriate buttons.

    Hence the app is able to write in text and save it in a very user-friendly way.

"""

import tkinter as tk
from tkinter.filedialog import askopenfilename, asksaveasfilename

def open_file(window: tk.Tk, text_edit: tk.Text):
    #   Specifies the type of files and their extensions
    filepath = askopenfilename(filetypes=[("Text Files", ".txt")])

    #   If file path does not exist, exit function
    if not filepath:
        return

    #   Delete everything currently in the text editor GUI
    #   `1.0` => 1 means the line 1, and character 0, the start of the file
    #   then tk.END refers to the end of the file.
    #   It's like file.seek() and using os.SEEK_END 
    text_edit.delete(1.0, tk.END)
    with open(filepath, "r") as f:
        content = f.read()
        #   Insert at the END of the file, which, since the text_edit widget area 
        #   has been cleared, the END is now at the very beginning off the file.
        #   THen place content inside
        text_edit.insert(tk.END, content)
    
    #   Change window title
    window.title(f"Open File: {filepath}")


def save_file(window: tk.Tk, text_edit: tk.Text):
    filepath = asksaveasfilename(filetypes=[("Text Files", ".txt")])

    if not filepath:
        return

    #   Take text_edit widget content and put in file:
    #   Yh, it overwrites already-existing files
    with open(filepath, "w") as f:
        content = text_edit.get(1.0, tk.END)
        f.write(content)

    window.title(f"Saving File {filepath}")


def main():
    #   Create window
    window = tk.Tk()
    window.title("Text Edit")

    #   Resizing text area according to its column, row position
    window.rowconfigure(0, minsize=400)
    window.columnconfigure(1, minsize=500)

    #   Text Edit Widget

    ##  Can pass in background color, foreground color
    #   Pree how the bacground color was changed.
    text_edit = tk.Text(window, font="Helvetica 18", background="gainsboro")



    #   Adding widgets based on row, column position
    #3  Adding the text_edit area on the window's screen...
    #3  like specifying its position.
    text_edit.grid(row=0, column=1)

    #   This is a vertical column to store the different buttons
    #   `relief` gives the element a 3d appearance
    #   `bd` is a 2px border
    frame = tk.Frame(window, relief=tk.RAISED, bd=2, background="antiquewhite")
    #   At first frame had no size, unless one sets it manually...
    #   or one added new widgets, as below:
    save_button = tk.Button(frame, text="Save", background="grey", bd="4", command=lambda: save_file(window, text_edit))

    #   Because the `open_file` function takes arguments... use a lambda function
    open_button = tk.Button(frame, text="Open", background="grey", bd="4",command=lambda: open_file(window, text_edit))

    ##  1. Place the button widgets inside the frame widget accordingly
    #   2. Adding padding between different buttons -- would have been margin in CSS/
    #       But this padding affects their outside.
    #   3. Make buttons same width with the `sticky` property
    #       Note that because of the padding, the buttons do not touch the full width end to end
    #       of the frame widget they are within 

    save_button.grid(row=0, column=0, padx=5, pady=5, sticky="ew")
    open_button.grid(row=1, column=0, padx=5, pady=5, sticky="ew")


    ##  Specify frame's position to add to its parent, the window.
    #   `sticky` expands the frame widget so its sepcified sides stick to the specified 
    #   side of the parent container (the window column area), EG:
    #   "ns", "n", "e" -- for north south, north, etc.
    #   without the sticky, see how the `frame` widget's height does not fill
    #   its window column..
    frame.grid(row=0, column=0, sticky="ns")


    #   Keeps window running in other process (most likely)
    #   If not in Pypy, it will be in a separate thread
    window.mainloop()


if __name__ =="__main__":
    main()