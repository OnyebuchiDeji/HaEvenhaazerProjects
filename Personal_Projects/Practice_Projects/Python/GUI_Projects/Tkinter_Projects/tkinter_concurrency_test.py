def print_this():
    print("Entering While Loop")

    # start_time = time.time()
    while True: 
        print("This prints every 2 seconds")
        time.sleep(2)

        # current_time = time.now()

def print_sth_else():
    print("This is from Button 2")

    
def main():
    """The Below is Testing whether the GUI runs on a Different Thread/Process"""
    """
        Conclusion: The GUI indeed does not work in multiple processes.
        Why? Because while the command of button1 is executing, when I pressed Button2's command
        the program froze and kepr on doing Button1's command.
    """
    window = tk.Tk()
    window.title("Test GUI")
    window.geometry("480x270")

    button1 = tk.Button(window, text="button1", width=8, height=3, background="red", command=print_this)
    button2 = tk.Button(window, text="button2", width=8, height=3, background="blue", command=print_sth_else)

    button1.pack(padx=5, pady=5, expand=True)
    button2.pack(padx=5, pady=5, expand=True)

    window.mainloop()

    """
        This further proves that execution stops at window.mainloop()
        
        Because while the GUI is on, the below does not run.
    """
    print("this should run after the GUI's mainloop starts!")
    while True:
        print("This prints after every two seconds in main thread.")
        time.sleep(2)




if __name__=="__main__":
    main()