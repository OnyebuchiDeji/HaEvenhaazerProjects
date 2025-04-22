"""
    Date: tue-11-June-2024

    Combining Layouts
"""

import tkinter as tk


root = tk.Tk()

frame1 = tk.Frame(root)
frame2 = tk.Frame(root)


label1 = tk.Label(frame1, text="Label 1:")
entry1 = tk.Entry(frame1)
label2 = tk.Label(frame1, text="Label 2:")
entry2 = tk.Entry(frame1)
button1 = tk.Button(frame2, text="Button 1")
button2 = tk.Button(frame2, text="Button 2")

##  `Pack` Way
# label1.pack()
# entry1.pack()
# label2.pack()
# entry2.pack()
# button1.pack()
# button2.pack()

##  Grid Way

label1.grid(row=0, column=0)
entry1.grid(row=0, column=1)
label2.grid(row=1, column=0)
entry2.grid(row=1, column=1)
button1.pack()
button2.pack()



frame1.pack(side=tk.LEFT)
frame2.pack(side=tk.LEFT)




root.mainloop()
