import tkinter as tk

"""
    Creating Responsive GUI Layout


"""

root = tk.Tk()

frame1 = tk.Frame(root)
frame2 = tk.Frame(root)

label1 = tk.Label(frame1, text="Label1")
entry1 = tk.Entry(frame1)
label2 = tk.Label(frame1, text="Label2")
entry2 = tk.Entry(frame1)
label3 = tk.Label(frame1, text="Label3")
text1= tk.Text(frame1, width=20, height=5)
button1 = tk.Button(frame1, text="Button1")

#   This makes the object fill the parent's left and right size
#   they expandd to fill the x-axis
label1.pack(fill="x")
entry1.pack(fill="x")
label2.pack(fill="x")
entry2.pack(fill="x")
label3.pack(fill="x")
#   `fill=both` does it so that the widget stretches to fill the area it occupies
#   fill='both' stetche both horizontally and vertically
#   If `expand=False` for text1, it will not expand with the screen.
#   Note that `fill` is not `expand`. `fill causes` the widget to take
#   the full space of the layout segment it is put in...
#   but `expand` causes the widget to expand in proportion to the screen's expansion.
text1.pack(fill="both", expand=False)
button1.pack(fill="x")


label4 = tk.Label(frame2, text="label4")
text2 = tk.Text(frame2, width=20, height=10)
button2 = tk.Button(frame2, text="Button2")

label4.pack(fill="x")
text2.pack(fill="both", expand=True)
button2.pack(fill="x")

frame1.pack(side=tk.LEFT, fill="both", expand=True)
frame2.pack(side=tk.LEFT, fill="both", expand=True)


root.mainloop()