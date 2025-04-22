import tkinter as tk

"""
    Here the `pack` layout is used all through.

    Can change height of texbox. It enables scrolling automatically...
    though it does not show the scrollbar
"""

root = tk.Tk()


def main():
    root.geometry("500x500")
    root.title("Deji's GUI")

    label = tk.Label(root, text="Yo! World!", font=("Arial", "18"))

    #   Different Layouts: `pack`, `grid`, `place`
    #   padx, pady, for positioning
    label.pack(padx=20, pady=20)

    #   font=("style", font_size_in_points)
    textbox = tk.Text(root, height=3, font=("Helvetica", 16))
    textbox.pack(padx=10)

    #   If one wants a text box without multiple lines, like for user name or password:
    entry_area = tk.Entry(root, width=15)
    #   Added paddiing
    entry_area.pack(pady=5)

    # button = tk.Button(root, text="Click! Me!", font=("Arial", 18))
    # button.pack(padx=10, pady=10)

    buttonframe = tk.Frame(root)
    #   The weight is to stretch the buttons to fill the x-axis
    #   Making a grid area with three columns
    buttonframe.columnconfigure(0, weight=1)
    buttonframe.columnconfigure(1, weight=1)
    buttonframe.columnconfigure(2, weight=1)

    btn1 = tk.Button(buttonframe, text="1", font=("Arial", 18))
    #   First row and first column
    #   Make the width-wise sides stick to the left and to the right
    #   `sticky="ew"` or `sticky=tk.W+tk.E`
    btn1.grid(row=0, column=0, sticky=tk.W+tk.E)

    btn2 = tk.Button(buttonframe, text="2", font=("Arial", 18))
    btn3 = tk.Button(buttonframe, text="3", font=("Arial", 18))
    btn4 = tk.Button(buttonframe, text="4", font=("Arial", 18))
    btn5 = tk.Button(buttonframe, text="5", font=("Arial", 18))
    btn6 = tk.Button(buttonframe, text="6", font=("Arial", 18))
  
    btn2.grid(row=0, column=1, sticky=tk.W+tk.E)
    btn3.grid(row=0, column=2, sticky=tk.W+tk.E)
    btn4.grid(row=1, column=0, sticky=tk.W+tk.E)
    btn5.grid(row=1, column=1, sticky=tk.W+tk.E)
    btn6.grid(row=1, column=2, sticky=tk.W+tk.E)

    #   The `fill` makes the grid stretch in the x-dimension
    buttonframe.pack(fill="x")


    root.mainloop()

if __name__=="__main__":
    main()