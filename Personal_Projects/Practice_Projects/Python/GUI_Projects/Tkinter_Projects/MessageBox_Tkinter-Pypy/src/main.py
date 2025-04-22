from tkinter import *
from tkinter import messagebox




def main():
    window = Tk()
    #   This centers the window on the screen and puts it in the top level...
    #   in front of every other window.
    window.eval("tk::PlaceWindow %s center" % window.winfo_toplevel())
    #   Makes window invisible; makes it invisible so just the message box pop up
    #   without it the window behind will be seen
    window.withdraw()

    #   There's these icons for the popup box `showinfo`, `showwarning`, `showerror`
    messagebox.showinfo("Message", "question is do you eat beans?")

    #messagebox.askyesno("Question", "do you eat beans?")
    #   Can change icon:
    if messagebox.askyesno("Question", "do you eat beans?", icon="warning") == True:
        print("A beans eater!")
        messagebox.showerror("Question", "You eat beans?")
        messagebox.showwarning("Message", "Of course you eat beans.")
        if messagebox.askokcancel("Question", "Answer if you want: why do you eat beans?", icon="error"):
            print("Because beans are good to eat; rich in protein.")
        
    else:
        print("Not a beans eater.")
        messagebox.showinfo("Message", "What... why? Who doesn't eat beans?")
        messagebox.showerror("Message", "Well apparently you don't :/ ")
        if messagebox.askretrycancel("Message", "Is it because it makes you gassy?"):
            print("O, that's a MED reason")
        else:
            print("Cool. Then you're chill.")

    
    window.deiconify()
    window.destroy()
    window.quit()

if __name__=="__main__":
    main()