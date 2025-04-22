import socket as sck
import threading
import tkinter
import tkinter.scrolledtext
from tkinter import simpledialog
import time



HOST = "127.0.0.1"
PORT = 9090

class Client:
    def __init__(self, host: str, port: int):
        self.sock = sck.socket(sck.AF_INET, sck.SOCK_STREAM)
        self.sock.connect((host, port))

        msg = tkinter.Tk()
        msg.withdraw()

        self.username = simpledialog.askstring("Username", "Please choose a username", parent=msg)

        self.gui_done = False
        
        self.running = True

        gui_thread = threading.Thread(target=self.gui_loop)
        receive_thread = threading.Thread(target=self.receive)

        gui_thread.start()
        receive_thread.start()

    def gui_loop(self):
        """Just builds the Frontend, the GUI"""
        self.win = tkinter.Tk()
        self.win.configure(bg="lightgray")

        self.chat_label = tkinter.Label(self.win, text="Chat:", bg="lightgray")
        self.chat_label.config(font=("Arial", 12))
        self.chat_label.pack(padx=20, pady=5)


        self.text_area = tkinter.scrolledtext.ScrolledText(self.win)
        self.text_area.pack(padx=20, pady=5)
        #   When set to disable, users cannot directly type into this chat area
        #   ... meaning to modify it, one has to enable it first
        self.text_area.config(state="disabled")

        self.msg_label = tkinter.Label(self.win, text="Message:", bg="lightgray")
        self.msg_label.config(font=("Arial", 12))
        self.msg_label.pack(padx=20,pady=5)

        self.input_area = tkinter.Text(self.win, height=3)
        self.input_area.pack(padx=20, pady=5)

        #   When it's clicked, `self.write` is called
        self.send_button = tkinter.Button(self.win, text="Send", command=self.write)
        self.send_button.config(font=("Arial", 12))
        self.send_button.pack(padx=20, pady=5)

        self.gui_done = True


        #   To run the code in the `self.stop` method to do some cleaning up and shutdown
        #   the program, for example, of the server and clients, when the Window is deleted
        self.win.protocol("WM_DELETE_WINDOW", self.stop)

        self.win.mainloop()


    def write(self):
        """
            Get text from Message Box, send to server and clear message box

            The .get('1.0', 'end') means start from beginning of text line
            till the end
        """
        message = f"{self.username}:\t{self.input_area.get('1.0', 'end')}"
        print(message)
        self.sock.send(message.encode('utf-8'))
        self.input_area.delete('1.0', 'end')

    def stop(self):
        """Runs cleanup and stops running routines"""
        self.running = False
        self.win.destroy()
        self.sock.close()
        exit(0)
        
        
    def receive(self):
        """
            The client socket logic that listens for messages
            from the server.
            It gets the message and puts it into the text area
        """
        while self.running:
            try:
                message = self.sock.recv(1024).decode('utf-8')
                if message == 'USER':
                    #   message, if 'USER', means send your username
                    self.sock.send(self.username.encode('utf-8'))
                else:
                    #   Ensure the GUI has finished loading before sending messages
                    if self.gui_done:
                        # time.sleep(5)
                        #   Note how the text area is enabled, then edited, and then disabled.
                        self.text_area.config(state='normal')
                        self.text_area.insert('end', message + "\n")
                        self.text_area.yview('end') #   Always scroll down to the end while adding messages
                        self.text_area.config(state='disabled')
            except ConnectionAbortedError as e:
                #   In case of a connection error
                break
            except:
                print("Error")
                self.sock.close()
                break

if __name__ == "__main__":
    Client(HOST, PORT)