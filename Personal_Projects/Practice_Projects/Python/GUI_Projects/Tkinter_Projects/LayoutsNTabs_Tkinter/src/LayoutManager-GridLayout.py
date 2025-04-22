"""
    Date: tue-11-June-2024

    Using Different Layouts:
        1.  Pack
        2.  Grid
        and `Place`, though not a Layout, just specifies position of ui components
"""

import tkinter as tk


root = tk.Tk()

label1 = tk.Label(root, text="Label 1:")
entry1 = tk.Entry(root)
label2 = tk.Label(root, text="Label 2:")
entry2 = tk.Entry(root)
button1 = tk.Button(root, text="Button 1")
button2 = tk.Button(root, text="Button 2")

#   Add the above UI elements using the different Layout Managers
#   to put them in the GUI

"""
    Using Grid Layout

    The Grid Layout provides a rigid Layout with everything having its own
    cell in the grid.

    There are parameters like `columnspan`to make an element occupy more than one cell of that row.
    Parameters like `expand` and `fill` do not work with grid layouts, jus tpack layouts
"""

label1.grid(row=0, column=0, padx=5, pady=5)
entry1.grid(row=0, column=1, padx=5, pady=5)
label2.grid(row=1, column=0, padx=5, pady=5)
entry2.grid(row=1, column=1, padx=5, pady=5)
#   Pree that these buttons are to the left normally...
#   Since its they are the only ones in rows 2 and 3, they should span the whole length
#   so use columnspan=2, so that it spans two columns' cells on that row.
button1.grid(row=2, column=0, columnspan=2, padx=5, pady=5)
button2.grid(row=3, column=0, columnspan=2, padx=5, pady=5)

root.mainloop()
