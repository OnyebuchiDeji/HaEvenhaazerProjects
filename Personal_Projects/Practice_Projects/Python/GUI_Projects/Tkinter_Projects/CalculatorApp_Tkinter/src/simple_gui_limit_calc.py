"""
    Date: wed-12-June-2024

    This is a calculator that can calculate LIMITS equation, from calculus-related maths.

    First example:
        Symbol: x
        Limit: 0
        Expression: '1/x'
        Click Calculate limit:
        This gives infinity represented by 'oo'
    Second:
        Symbol: x
        Limit: oo
        Expression: 1/x
        Result: 0
    Third:
        Symbol: x
        Limit: 5
        Expression: 1/x
        Result: 1/5
    Fourth:
        Symbol: x
        Limit: pi
        Expression: 1/x
        Result: 1/pi
            This 'pi' represents the actual value PI
    FourthB:
        Symbol: x
        Limit: pi
        Expression: sin(x)
        Result: 0
    Fifth:
        Symbol: x
        Limit: E
        Expression: ln(x)
        Result: 1
            This 'E' represents the actual value E - 2.71..
    FifthB:
        Symbol: x
        Limit: k
        Expression: ln(x)
        Result: log(k)
    Sixth:
        Symbol: n
        Limit: oo <- infinity
        Expression: (1+1/n) ^ n
        Result: E
            The limit of this expression when n goes toward inifinity is E
    Seventh:
        Symbol: n
        Limit: oo <- infinity
        Expression: Sum(1/k^2, (k, 1, n))
        Result: (pi**2)/6
            The limit of this expression as n goes toward infinity and k goes from 1 to n.
                (k, 1, n) means k goes from 1 to n
        
"""


import tkinter as tk
import sympy as sp



class LimitCalculator:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Limit Calculator")
        # self.root.geometry("480x270")
        # self.root.columnconfigure([0, 1], minsize=460/2)
        # self.root.rowconfigure([0, 1], minsize=260/4)
        self.oninit_widgets()

        self.root.mainloop()
    

    def oninit_widgets(self):
        self.symbol_label = tk.Label(self.root, text="Symbol")
        self.symbol_label.grid(row=0, column=0, padx=2, pady=2)
        self.symbol_text = tk.Entry(self.root)
        self.symbol_text.grid(row=0, column=1, padx=2, pady=2)

        self.limit_label = tk.Label(self.root, text="Limit")
        self.limit_label.grid(row=1, column=0, padx=2, pady=2)
        self.limit_text = tk.Entry(self.root)
        self.limit_text.grid(row=1, column=1, padx=2, pady=2)

        self.expression_label = tk.Label(self.root, text="Expression")
        self.expression_label.grid(row=2, column=0, padx=2, pady=2)

        self.expression_text = tk.Entry(self.root)
        self.expression_text.grid(row=2, column=1, padx=2, pady=2)

        self.calculate_button = tk.Button(self.root, text="Calculate Limit", command=self.calculate_limit)
        self.calculate_button.grid(row=3, column=0, columnspan=2, padx=2, pady=2)

        ##  Use 'highlightbackground="grey"' and 'highlightthickness=2'
        self.result_label = tk.Label(self.root, text="-", highlightbackground='grey', highlightthickness=2)
        self.result_label.grid(row=4, column=0, columnspan=2, padx=2, pady=2)

        self.sym = None
        self.lim = None


    def calculate_limit(self):
        """
            Get symbol from text entry
        """
        ##  .get() for a tk.Entry, but .get("1.0", tk.END or "end") for tk.Text (text field)
        self.sym = sp.symbols(self.symbol_text.get())

        ##  Get content of expression text entry
        expression = self.expression_text.get()

        ##  In the case of a SUM expression, one has to call a `doit` in the end to evaluate
        #   it
        expression = f"{expression}.doit()" if "Sum" in expression else expression
        self.lim = sp.limit(expression, self.sym, self.limit_text.get())
        self.result_label.config(text=str(self.lim))

        
    

def main():
    LimitCalculator()

if __name__=="__main__":
    main()