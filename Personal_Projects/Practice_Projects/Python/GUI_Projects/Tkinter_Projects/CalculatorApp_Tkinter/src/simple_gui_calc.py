"""
    There was an issue here:
        buttons.append(tk.Button(root, text=characters[index],
                            command=lambda chr=characters[index]: add_to_calculation(chr),
                            width=5, font=("Arial", 14)))

    I had to do
        ```
        lambda chr=characters[index]: add_to_calculation(chr)
        ```
        When I just did:
        ```
        lambda : add_to_calculation(chr=characters[index])
        ```
        it always printed that index was out of range; because index became 19 on finishing the loop/
        Anytime the `add_to_calculation` functin was called, no matter the button, index was 19.
        This is because the latter method never stored the values passed in at the appropriate time of
        iteration.
        But when `lambda` is used, it creates a lambda object stored in memory that captures
        what arguments were passed in at the appropriate time in iteration for that button.
        So when a button is clicked, its appropriate value is passed into the `add_to_calculation()`!
        function to call it!


"""

import tkinter as tk

calculation_expr = ""

def add_to_calculation(symbol):
    #   so that `calculation` can be manipulated inside this function
    global calculation_expr
    calculation_expr += str(symbol)
    #   Note 1.0=> line 1, character position 0 <-- beginning of area
    text_result.delete(1.0, tk.END)
    text_result.insert(1.0, calculation_expr)
    

def evaluate_calculation():
    """
        This uses the `eval` function to evaluate an expression
        It can also evaluate Python code. Hence someone can inject some code into it...
        this can be a SECURITY ISSUE.
    """
    global calculation_expr
    #   Use try in case of divide by zero-error
    try:
        calculation_expr = str(eval(calculation_expr))
        text_result.delete(1.0, "end")
        text_result.insert(1.0, calculation_expr)
    except:
        clear_field()   #   Clears the text_field
        text_result.insert(1.0, "Error")


def clear_field():
    global calculation_expr
    calculation_expr = ""
    text_result.delete(1.0, "end")



root = tk.Tk()
root.geometry("480x270")

root.columnconfigure([0, 1, 2, 3],minsize=(480/4))
root.rowconfigure([1, 2, 3, 4, 5],minsize=(270/7))


text_result = tk.Text(root, height=2, width=16, font=("Arial", 24), bg="gainsboro")
text_result.grid(columnspan=4, sticky="ew")

"""
    Formula to map each button with its row and column, to the corresponding indecx
    in the 1D list of tk.Button objects:

    index = row * rows + col
"""
rows, columns = 5, 4
row_diff = rows - columns
buttons: list[tk.Button] = []

#   For all the values for the buttons that form the grid
characters = "123+456-789*(0)/C="

#   Because of the text_area already takes the first row of the grid layout of the `root` widget...
#   let the index start from 0 (but in code, in adding the rows, I do `row + 1`)...
#   all the way to 5 (6-1 because of how range works) 
for row in range(0, rows):
    for col in range(columns):
        index = row*(rows-row_diff) + col
        if row != 4:
            ##  Creates each button appropriately, and get the appropriate character
            #   from the string of characters
            buttons.append(tk.Button(root, text=characters[index],
                                    command=lambda chr=characters[index]: add_to_calculation(chr),
                                    width=5, font=("Arial", 14)))
            ##  Then attaches it to the Grid Layout, with its respective row and column calue
            buttons[index].grid(row=row+1, column=col, padx=5, sticky="ew")
        else:
            if index == len(characters)-2:
                buttons.append(tk.Button(root, text=characters[index],
                                        command=clear_field,
                                        width=11, font=("Arial", 14)))
                buttons[index].grid(row=row+1, column=col, columnspan=2, padx=5, sticky="ew")
            elif index == len(characters)-1:
                buttons.append(tk.Button(root, text=characters[index],
                                        command=lambda: evaluate_calculation(),
                                        width=11, font=("Arial", 14)))
                buttons[index].grid(row=row+1, column=col+1, columnspan=2, padx=5, sticky="ew")
            else:
                pass


root.mainloop()