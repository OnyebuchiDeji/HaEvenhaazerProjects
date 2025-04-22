"""
    Date: Mon-19-Aug-2024

    This episode demonstrates how to add a Matplotlib Grapg to Kivy.
    Requirments:
        1.  `pip install kivy_garden` -- for matplotlib install support
        2.  `garden install matplotplib`
        3.  'pip install matplotlib'
    NOTE: garden.matplotlib was installed at: C:\\Users\\Ebenezer Ayo-Meti\\.kivy\\garden\\garden.matplotlib
    not into this Project's environment vaiable's "kivy/garden" directory/
    So we copied it to this local environment `.env`'s kivy's 'garden' ditrectory and renamed the folder
    from `garden.matplotlib` to just matplotlib   

    These were done:
        1.  Render the matplotlib graph
        2.  Add a name input text box and button to save the image with that entered name.

    However, the program did not work. It kept giving this error: 
        AttributeError: 'FigureCanvasKivyAgg' object has no attribute 'resize_event'
    The issue is hence with the file:
       File "C:\My_Practice_Projects\Python_Projects\Mobile_App_Projects\Kivy_Tutorial_26072024\.env\Lib\site-packages\kivy\garden\matplotlib\backend_kivy.py", line 1233, in _on_size_changed
     self.resize_event()
"""

from kivymd.app import MDApp
from kivy.core.window import Window
from kivy.lang import Builder
from kivymd.uix.boxlayout import MDBoxLayout
from kivy.garden.matplotlib.backend_kivyagg import FigureCanvasKivyAgg
import matplotlib.pyplot as plt

#   Define what to plot on the graph
x = [1, 2, 3, 4, 5]
y = [5, 12, 6, 9, 15]

plt.plot(x, y)
plt.ylabel("Y Axis")
plt.xlabel("X Axis")





class MattGraph(MDBoxLayout):
    # def __init__(self, **kwargs):
    #     super().__init__(**kwargs)
        # blayout_ref = self.ids.id_box_layout
        # blayout_ref.add_widget(FigureCanvasKivyAgg(plt.gcf()))
    # def on_start(self):

    def save_it(self):
        ...
    

#   The KivyMD app
class MyApp(MDApp):
    light_theme = False
    theme_text_l = "L"
    theme_text_d = "D"


    def build(self):
        self.title = "Matplotlib Graph with Kivy"
        Window.clearcolor = (0.3, 0.25, 0.3, 1)
        self.theme_cls.theme_style = "Light" if self.light_theme else "Dark"
        self.theme_cls.primary_palette = "Forestgreen"
        self.theme_cls.accent_palette = "Red"
        #   Designate the .kv design file
        Builder.load_file("base_style.kv")
        self.root = MattGraph()
        return self.root

    def toggle_theme(self):
        self.light_theme = not self.light_theme
        self.theme_cls.theme_style = "Light" if self.light_theme else "Dark"
        self.root.ids.id_theme_btn.text = self.theme_text_l if self.light_theme else self.theme_text_d
    
    def on_start(self):
        blayout_ref = self.root.ids.id_box_layout
        blayout_ref.add_widget(FigureCanvasKivyAgg(plt.gcf()))
        
        
if __name__ == "__main__":
    MyApp().run()
