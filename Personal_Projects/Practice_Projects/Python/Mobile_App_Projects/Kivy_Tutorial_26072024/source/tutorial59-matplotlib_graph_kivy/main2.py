"""
    Date: Mon-19-Aug-2024

    This episode demonstrates how to add a Matplotlib Graph to Kivy.
    This `main2.py` works!
    The one in `main.py` did not work for some reason.

    So as an alternative, we did:
        ```pip install kivy-matplotlib-widget```
    
    Here where I got the example from: https://github.com/jeysonm82/kivy_matplotlib
    The kivy_matplotlib_widget was made building on the above project.

    The site at https://pypi.org/project/kivy-matplotlib-widget/ explains this.

    The `Save` button method is also implemented
"""

from kivymd.app import MDApp
from kivy.core.window import Window
from kivy.lang import Builder
from kivymd.uix.boxlayout import MDBoxLayout
# from kivy.uix.floatlayout import FloatLayout
from kivy_matplotlib_widget.tools.interactive_converter import interactive_graph_ipython
# from kivy_matplotlib_widget.uix import MatplotFigure, MatplotNavToolbar
from kivy_matplotlib_widget.uix.graph_widget import MatplotFigure
from matplotlib import figure as fg
import matplotlib.pyplot as plt
import numpy as np
import os

#   Define what to plot on the graph
x = [1, 2, 3, 4, 5]
y = [5, 12, 6, 9, 15]

plt.plot(x, y)
plt.ylabel("Y Axis")
plt.xlabel("X Axis")





class MattGraph(MDBoxLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    def save_it(self):
        """Images are saved as .png by default."""
        name_tb_ref = self.ids['id_tb_name']
        dir_ = os.path.join(os.path.dirname(__file__), "output")
        if len(name_tb_ref.text) > 1:
            plt.savefig(os.path.join(dir_, name_tb_ref.text))
            self.ids['id_log_label'].text = f"{name_tb_ref.text} Saved to:\n {dir_}!"
        else:
            self.ids['id_log_label'].text = "Enter an actual file name!"
            print("Enter an actual file name!")
            return
    

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
        Builder.load_file("base_style2.kv")
        self.root = MattGraph()
        return self.root

    def toggle_theme(self):
        self.light_theme = not self.light_theme
        self.theme_cls.theme_style = "Light" if self.light_theme else "Dark"
        self.root.ids.id_theme_btn.text = self.theme_text_l if self.light_theme else self.theme_text_d
    
    def on_start(self):
        blayout_ref = self.root.ids['id_box_layout']
        # figure_widget_ref = self.root.ids["id_figure_wgt"]
        fig_widget1 = MatplotFigure()
        fig_widget1.figure = plt.gcf()
        blayout_ref.add_widget(fig_widget1)

        fig = fg.Figure(figsize=(2, 2))
        t = np.arange(0.0, 100.0, 0.01)
        s = np.sin(0.08 * np.pi * t)
        axes = fig.gca()
        axes.plot(t, s)
        axes.set_xlim(0, 50)
        axes.grid(True)
        fig_widget2 = MatplotFigure()
        fig_widget2.figure = fig
        blayout_ref.add_widget(fig_widget2)
        
        
if __name__ == "__main__":
    MyApp().run()
