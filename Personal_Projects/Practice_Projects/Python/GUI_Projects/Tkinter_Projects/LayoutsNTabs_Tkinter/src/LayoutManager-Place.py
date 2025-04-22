"""
    Date: tue-11-June-2024

    Using Different Layouts:
        1.  Pack
        2.  Grid
        3. and `Place`, though not a Layout, just specifies position of ui components
"""

import tkinter as tk


root = tk.Tk()
root.geometry("320x180")

label1 = tk.Label(root, text="Label 1:")
entry1 = tk.Entry(root)
label2 = tk.Label(root, text="Label 2:")
entry2 = tk.Entry(root)
button1 = tk.Button(root, text="Button 1")
button2 = tk.Button(root, text="Button 2")

#   Add the above UI elements using the different Layout Managers
#   to put them in the GUI

"""
    Using Place Function

    It is just used to specify the x and y coordinates of the widgets.
    It positions with the origins being at the top-left corener of th egeometry
"""

label1.place(x=10, y=10)
entry1.place(x=70, y=10)
label2.place(x=10, y=50)
entry2.place(x=70, y=50)



root.mainloop()
