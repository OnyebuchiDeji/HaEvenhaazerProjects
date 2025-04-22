Project Made By Ebenezer Ayo-Metibemu
This project was referenced from NeuralNine from YouTube. Simple Android Calculator App

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

LASTLY! When Installing with kivy, the main app file, with the entry point of the program must be named main.py
