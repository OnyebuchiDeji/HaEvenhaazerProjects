"""
    Date: Wed-31-July-2024

    This tutorial demonstrates an Image Viewing app that uses Kivy FileChooserIconView
    and Kivy FileChooserListView in Python.
    More on FileChooser here: https://kivy.org/doc/stable/api-kivy.uix.filechooser.html
"""

from kivy.app import App
from kivy.uix.widget import Widget
from kivy.lang import Builder
from kivy.core.window import Window


Builder.load_file('base_style.kv')

class MyLayout(Widget):
    def selected(self, filename):
        try:
            self.ids.my_image.source = filename[0]
            print(filename[0])
        except:
            ...

class MyApp(App):
    def build(self):
        self.title = "ImageViewer using FileChoosers"
        Window.clearcolor = (0.2, 0.2, 0.2, 1)
        return MyLayout()
        
if __name__ == "__main__":
    MyApp().run()