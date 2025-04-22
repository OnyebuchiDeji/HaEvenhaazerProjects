import kivy
from kivy.lang import Builder
from kivy.app import App
from kivy.core.window import Window
from kivy.uix.boxlayout import BoxLayout

"""
    This project, made by following what NeuralNine did on Youtube, was made on Mon-08-01-2024!
    This app was not very complicated!

    1.
    A subtle correction was to be made, to correct the floating-point rounding error that occured...
    when 0.1 is added to 0.2. It gives this: 0.30000000000000004 -- it is a python-related issue

    2.
    To compile this app to android, I need linux. Either the windows subsystem in Linux or use a linux virtual machine
    Compiling to android form requires linux wsl or virtual machine!
    Instructions are here:
    https://buildozer.readthedocs.io/en/latest/installation.html

    These are specifically for Ubuntu:
    To install the module: pip3 install --user --upgrade buildozer

    sudo apt update
    sudo apt install -y git zip unzip openjdk-17-jdk python3-pip autoconf libtool pkg-config zlib1g-dev libncurses5-dev libncursesw5-dev libtinfo5 cmake libffi-dev libssl-dev
    pip3 install --user --upgrade Cython==0.29.33 virtualenv  # the --user should be removed if you do this in a venv

    # add the following line at the end of your ~/.bashrc file
    export PATH=$PATH:~/.local/bin/

"""

"""The below is just to ensure a proper kivy version for one's android phone and the window size"""
kivy.require("2.0.0")
Window.size = (640, 700)



class MyRoot(BoxLayout):
    """
        NOTE!
        1. in the kivy app, the MyRoot is put in angled brackets.
        Remember that because it is reutrned in the build method that inherits from App, there is no need to make an instance...
        in the kivy script
        TextInput:
            id: calc_field
            height: 200
            size_hint: (1, None) means that the size does not change, remains what it has been defined to be, in this case, 200

    """
    def __init__(self):
        super(MyRoot, self).__init__()

    ##  This is the function that adds the symbol of the buttons pressed to the text field
    def calc_symbol(self, symbol:str):
        self.calcTextField.text += symbol
    
    def clear(self):
        self.calcTextField.text = ""
    
    def calculate_result(self):
        self.calcTextField.text = str(eval(self.calcTextField.text))
        print(self.calcTextField.text)


#3  Since I am using this builder, it must be defined after every class's definition
kv = Builder.load_file("calc_app.kv")

class DejiCalc(App):
    def build(self):
        ##  This is the app's root
        return MyRoot()



if __name__ == "__main__":
    DejiCalc().run()