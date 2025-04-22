"""
    Date: Mon-12-Aug-2024

    This episode demonstrates an introduction into animating Widgets using Kivy's built-in
    animation system.
"""

from kivy.app import App
from kivy.uix.widget import Widget
from kivy.lang import Builder
from kivy.animation import Animation
from kivy.core.window import Window

#   Designate the .kv ddesign file
Builder.load_file("base_style.kv")

class MyLayout(Widget):
    def animate_it(self, caller_widget, *args):
        """
            Doing `animate +=` assigns the animations to play in a queue
            so that when the prior is done, the next runs
        """
        #   Define animation effect to be done
        animate = Animation(
            background_color=(0, 0, 1, 1),
            duration=3,     #   in seconds
            opacity=0.2     #   changes opacity
        )
        animate += Animation(
            opacity = 0.7,
            duration=.5,
            background_color=(0.7, 0, 0.7, 1),
            size_hint=(.8, .8)
        )

        animate += Animation(
            size_hint=(.5, .5),
            background_color=(0, 0.7, 0.7, 1),
            pos_hint={"center_x": 0.2}
        )
        animate += Animation(
            pos_hint={"center_x": 0.8}
        )
        animate += Animation(
            pos_hint={"center_x": 0.5}
        )
        
        #   Start The Animation
        animate.start(caller_widget)

        #   Create a Callback -- runs when animation is done
        animate.bind(on_complete=self.animation_callback)

    def animation_callback(self, *args):
        #   Access the id of the Label Widget
        self.ids.my_label.text = "Pree the Animation!"


class MyApp(App):
    def build(self):
        self.title = "Animations"
        Window.clearcolor = (0.15, 0.07, 0.1, 1)
        return MyLayout()


if __name__ == "__main__":
    MyApp().run()