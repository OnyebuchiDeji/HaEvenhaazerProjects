"""
    Date: Tue-11-June-2024

    This demonstration shows making a GUI that has tabs

    The submodule ttk contains a UI component called a Notebook.
    The notebook alllows multiple tabs to be used.
"""

import tkinter as tk
from tkinter import ttk #   Importing the submodule


def main():
    root = tk.Tk()
    root.title("Notebook App")
    root.geometry("480x270")

    notebook = ttk.Notebook(root)
    notebook.pack(expand=True, fill="both")

    #   Frames are added to the notebook as tabs
    #   A frame is essentially a space where one can add other widgets
    frame1 = tk.Frame(notebook, width=400, height=200, background="red")
    frame2 = tk.Frame(notebook, width=400, height=200, background="indigo")
    frame3 = tk.Frame(notebook, width=400, height=200, background="violet")
    frame4 = tk.Frame(notebook, width=400, height=200, background="plum")

    label1 = tk.Label(frame1, text="On Tab 1", background="whitesmoke")
    label1.pack()
    label2 = tk.Label(frame2, text="On Tab 2", background="darkgrey")
    label2.pack()
    button1 = tk.Button(frame2,text="Tab 2 Button", background="purple")
    button1.pack()
    label3 = tk.Label(frame3, text="On Tab 3", background="grey")
    label3.pack()
    entry1 = tk.Entry(frame3, background="gainsboro")
    entry1.pack()

    #   Giving a grid layout to `frame4`
    label4 = tk.Label(frame4, text="On Tab 4", background="grey")
    label5 = tk.Label(frame4, text="On Tab 4", background="white")
    label4.grid(row=0, column=0)
    label5.grid(row=0, column=1)

    entry2 = tk.Entry(frame4, background="antiquewhite")
    entry3 = tk.Entry(frame4, background="lightpink")
    entry2.grid(row=1, column=0)
    entry3.grid(row=1, column=1)

    frame4.columnconfigure(index=0, weight=1)
    frame4.columnconfigure(index=1, weight=1)
    frame4.rowconfigure(index=0, weight=1)
    frame4.rowconfigure(index=1, weight=1)


    frame1.pack(fill="both", expand=True)
    frame2.pack(fill="both", expand=True)
    frame3.pack(fill="both", expand=True)
    frame4.pack(fill="both", expand=True)

    notebook.add(frame1, text="Tab 1")
    notebook.add(frame2, text="Tab 2")
    notebook.add(frame3, text="Tab 3")
    notebook.add(frame4, text="Tab 4")


    root.mainloop()



if __name__=="__main__":
    main()