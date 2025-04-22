"""
    date: Tue-11-June-2024

    1.  Create Window
    2.  Add title
    3.  Create Text Area widget
    4.  Initialize main loop
    5.  Determine the size of widget by setting size of column it's added in.
"""

import tkinter as tk




def main():
    #   Create window
    window = tk.Tk()
    window.title("Text Edit")

    #   Set size of a specific area -- in this case that of the text area
    #   Here is settting the size of the row 0, column 0 to 400, 500 respectively
    #   Note now that there is no widget in this column
    window.rowconfigure(0, minsize=400)
    window.columnconfigure(0, minsize=500)

    #   Text Edit Widget

    ##  Can pass in background color, foreground color
    #   Pree how the bacground color was changed.
    text_edit = tk.Text(window, font="Helvetica 18", background="gainsboro")



    #   Adding widgets based on row, column position
    #3  Adding the text_edit area on the window's screen...
    #3  like specifying its position.
    #   In this case, the text area is added to column 1, row 0...
    #   but the first possible is column 0, row 0
    #   Note that because there's no other widget, it takes the size of the whole window
    text_edit.grid(row=0, column=1)

    #   Keeps window running in other process (most likely)
    #   If not in Pypy, it will be in a separate thread
    window.mainloop()


if __name__ =="__main__":
    main()