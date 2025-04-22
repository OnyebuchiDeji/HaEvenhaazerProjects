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
    Using Pack Layout
    The Pack Layout stacks everything on top of one another
    consecutively according to the order of packing.
"""
#   So button2 will be on top if it calls pack here
# button2.pack()

##  Using padx and 
## pady spaces elements apart from each other
##  Then using `side=tk.LEFT` displaces the elements to be stacked
##  in a left-wide direction -- note that they are in the order in which they were stacked...
##  only difference is that its horizontal, stacked side by side.
##  But the buttons are stacked normally, top-on-bottom
label1.pack(padx=5, pady=5, side=tk.LEFT)
entry1.pack(padx=5, pady=5, side=tk.LEFT)
label2.pack(padx=5, pady=5, side=tk.LEFT)
entry2.pack(padx=5, pady=5, side=tk.LEFT)
#   tk.Y stretches the widget to fill the space vertically
#   tk.X stretches it to fill up hotrizontal space 
#   tk.BOTH soes both
button1.pack(padx=5, pady=5, expand=True, fill=tk.BOTH)
button2.pack(padx=5, pady=5, expand=True, fill=tk.BOTH)

root.mainloop()
