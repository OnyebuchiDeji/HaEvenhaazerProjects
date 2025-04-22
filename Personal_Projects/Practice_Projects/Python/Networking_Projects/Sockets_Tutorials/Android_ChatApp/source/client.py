
"""
    Experienced an issue with the fact hat Kivy no longer allowed a thread
    to update the graphics instruction outside the main Kivy thread.
    But I needed the thread to constantly check for messages without
    blocking the Kivy loop.

    The solution was to use a kind of event callback. But there was no normal
    one that didn't require clicking, pressing, touching, etc...
    Hence we searched for one and found the solution:

        def on_motion(self, etype, me):
            # will receive all motion events.
            pass

        Window.bind(on_motion=self.on_motion)

    where self.on_motion is defined in the class, and is bound to the kivy.window.Window
    in the __init__ method.

    There are more solutions, such as this custom EventManager.
    But will do that separately.
"""

import kivy
from kivy.app import App
import kivy.clock
import kivy.input
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.uix.layout import Layout
from kivy.core.window import Window

import socket as sck
import threading

kivy.require("1.9.0")


client = sck.socket(sck.AF_INET, sck.SOCK_STREAM)



class MyRoot(BoxLayout):
    def __init__(self, *args, **kwargs):
        super(MyRoot, self).__init__(*args, **kwargs)
        self.current_text = ""
        Window.bind(on_motion=self.on_motion)

    def send_message(self):
        strToSend = f"{str(self.username_text.text)}: {str(self.message_text.text)}"
        client.send(strToSend.encode('utf-8'))
        self.message_text.text = ""
    
    def update_chat(self):
        self.chat_text.disabled = False
        self.chat_text.readonly = False
        self.chat_text.text = self.current_text
        self.chat_text.disabled = True
        self.chat_text.readonly = True

    def update_current_text(self, msg):
        self.current_text += msg + "\n"
        
    def connect_to_server(self):
        if self.username_text != "":
            #   connect
            client.connect((self.ip_text.text.strip(), 9999))
            message = client.recv(1024).decode('utf-8')
            if message == "USER":
                client.send(self.username_text.text.encode('utf-8'))
                #   disable all connection widgets
                #   enable all others
                self.send_btn.disabled = False
                self.message_text.disabled = False
                self.connect_btn.disabled = True
                self.ip_text.disabled = True


                self.make_invisible(self.connection_grid)
                self.make_invisible(self.connect_btn)

                #   Receive the You have Connected Message
                
                """
                    Kivy didn't allow one to update any graphics component
                    from outside of the main Kivy Thread.

                    But the reason why I need to thread this is so that other things
                    can run, lest everything will be stuck in the while loop
                """
                thread = threading.Thread(target=self.receive)
                thread.start()

            msg2 = client.recv(1024).decode('utf-8')
            self.update_current_text(msg2)
            
    
    def make_invisible(self, widget):
        """Make the specified element invisible"""
        widget.visible = False
        widget.size_hint_x = None
        widget.size_hint_y = None
        widget.height = 0
        widget.width = 0
        widget.text = ""
        widget.opacity = 0


    def on_motion(self, etype, me, *args):
        """
            This will detect all motion events.
            it is bound to the Window in the __init__ method

            1.  The etype is the Window object the event comes from
            2.  The Me is the type of MouseMotionEvent, as a string:
                There are two types:
                    i.  `update`: When the mouse is moving withing the Window
                    ii. `end`: When the mouse exits the window
            3.  The *args is information about the event, it shows
                that it is a MouseMotionEvent object and gives the mouse positions
            
            Here are examples of the output:
                Event Type:  <kivy.core.window.window_sdl2.WindowSDL object 
                at 0x0000018F1EBA8FA0>
                Me:  update
                Args:  <MouseMotionEvent spos=(1.0, 0.001669449081803005) pos=(0.0, 0.0)>

                Event Type:  <kivy.core.window.window_sdl2.WindowSDL object 
                at 0x0000018F1EBA8FA0>
                Me:  end
                Args:  <MouseMotionEvent spos=(1.0, 0.001669449081803005) pos=(0.0, 0.0)>

            Hence I use the Me == "end".
            Then changed it to every time
        """

        # if (me == "end"):
        self.update_chat()



    def receive(self):
        """Here, wait for new messages and add to the GUI"""
        stop = False
        while not stop:
            try:
                msg = client.recv(1024).decode('utf-8')
                print(msg)
                self.update_current_text(msg)
            
            except Exception as e:
                print("ERROR")
                print(str(e))
                stop = True
                client.close()
            
        






class KhaylemWebChat(App):
    def build(self):
        return MyRoot()

    
def main():
    khaylemWebChat = KhaylemWebChat()
    khaylemWebChat.run()



if __name__ == "__main__":
    main()
