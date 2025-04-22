"""
    02-JAN-2024 - 03-JAN-2024
    In this version, FloatLayout is used for Dynamic Placement!
    GridLayouts where cool but there were issues with resizability and overlapping and such...
    So, FloatLayouts turn out to be the best!

"""

import kivy
from kivy.app import App
from kivy.uix.floatlayout import FloatLayout

"""
    The kivy script acts like css in a way. Every FloatLayout created will have the properties as defined in the kivy tag...
    <FloatLayout>

    Likewise, the Buttons made in the <FloatLayout> tag gain the properties that are defined in the <Button> tag
    
    FloatLayouts enables dynamic placements, that is, using pos_hint: {"x":0-1, "y":0-1, "top":0-1, "bottom":0-1, "left":0-1, "right":0-1}
    they take values between 0 and 1.
    It acts just like the top, left, down, right of css!

"""
"""
    Note This code!
    An if statement can be used on the below:
    text:"Mobile App" if btn.state == "normal" else "Mobile Dev" 
    But an if statement will only work here if I put the colors in normal braces!
    E.G:
    background_color: (0.2, 0.2, 0.5, 1) if btn.state=="normal" else (0.9, 0.2, 0.2, 1)
    As for the colors, this is how they are:
"""

class App6(App):
    def build(self):
        return FloatLayout()

if __name__== "__main__":
    App6().run()