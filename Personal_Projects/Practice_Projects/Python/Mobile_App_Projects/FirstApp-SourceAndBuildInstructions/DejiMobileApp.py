import kivy
from kivy.lang import Builder
from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.boxlayout import BoxLayout

import random as rnd

"""
    This app was made in Mon-08-Jan-2024

    In here, I learn how to compile the app to be able to be installed on android.
    Using the BUILDOZER tool at: https://buildozer.readthedocs.io/en/latest/installation.html

    It can only run on linux, so a virtual machine or a linux subsystem!
    
    These are specifically for Ubuntu:
    To install the module: pip3 install --user --upgrade buildozer

    sudo apt update
    sudo apt install -y git zip unzip openjdk-17-jdk python3-pip autoconf libtool pkg-config zlib1g-dev libncurses5-dev libncursesw5-dev libtinfo5 cmake libffi-dev libssl-dev
    pip3 install --user --upgrade Cython==0.29.33 virtualenv  # the --user should be removed if you do this in a venv

    # add the following line at the end of your ~/.bashrc file
    export PATH=$PATH:~/.local/bin/
"""

kivy.require("2.0.0")

class MyRoot(BoxLayout):
    def __init__(self):
        super(MyRoot, self).__init__()
    
    def generate_number(self):
        self.randomLabelVar.text = str(rnd.randint(0, 1000))


"""
    Check it! Because I used the builder, and the file it loads is the same wuth the name of the class that inherits from App...
    see how it repeats the same thing by uncommenting
"""
# kv = Builder.load_file("dejimobileapp.kv")


class DejiMobileApp(App):
    def build(self):
        return MyRoot()



if __name__=="__main__":
    DejiMobileApp().run()
