"""
    Date: Mon-12-Aug-2024

    This episode demonstrates the use of Kivy's progress bars.

    Here a progress bar is made to update anytime a Button is clicked which increments the value
    the progress bar is tracking.
"""

from kivy.app import App
from kivy.uix.widget import Widget
from kivy.lang import Builder
from kivy.uix.progressbar import ProgressBar
from kivy.core.window import Window

#   Designate the .kv design file
Builder.load_file("base_style.kv")

class MyLayout(Widget):
    def pressed_it(self):
        """This Changes the Value of the Progress Bar"""
        #   Get reference to Progress Bar object created in the .kv design file
        prog_bar_ref: ProgressBar = self.ids.my_progress_bar
        prog_label_ref = self.ids.progress_label

        #   If it's value is less than 1, increment
        if prog_bar_ref.value < 1.0:
            #   Value to Increment By
            incr_val = .25
            #   Increment and update the value of the progress bar
            prog_bar_ref.value += incr_val
        else:
            #   Reset and update the value of the progress bar
            prog_bar_ref.value = 0.0
        
        #   Updat ethe label
        prog_label_ref.text = f"{float(prog_bar_ref.value) * 100}% Progress"


class MyApp(App):
    def build(self):
        self.title = "Progress Bars"
        Window.clearcolor = (0.15, 0.07, 0.1, 1)
        return MyLayout()


if __name__ == "__main__":
    MyApp().run()