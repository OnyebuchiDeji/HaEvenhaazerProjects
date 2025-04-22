"""
    Date: Wed-21-July-2024
    
    This tutorial demonstrates a Simple Calculator App
"""

from kivy.app import App
from kivy.uix.widget import Widget
from kivy.properties import ObjectProperty
from kivy.lang import Builder
from kivy.core.window import Window

"""
    Something for automating the size depending on the device platform
    if(platform == 'android' | platform == 'ios' | paltform == 'android'):
            Window.maximize()
        else:
            Window.size = (620, 1024)

        return kv
"""

#   Set App Size
# desired_size = 
Window.size = (324, 666)
Builder.load_file("source/tutorial16-simple_calculator_p2/base_style.kv")


class MyLayout(Widget):
    
    def clear_input(self):
        self.ids.calc_input.text = "0"

    def button_press(self, button):
        #   Get what was previously in the calc input space
        prior = self.ids.calc_input.text

        if prior == "0":
            self.ids.calc_input.text = ""
            self.ids.calc_input.text = f'{button}'
        else:
            self.ids.calc_input.text = f'{prior}{button}'

    def add_button(self):
        prior = self.ids.calc_input.text
        self.ids.calc_input.text = f'{prior}+'
    
    def subtract_button(self):
        prior = self.ids.calc_input.text
        self.ids.calc_input.text = f'{prior}-'
        ...
    def multiply_button(self):
        prior = self.ids.calc_input.text
        self.ids.calc_input.text = f'{prior}x'
        ...
    
    def divide_button(self):
        prior = self.ids.calc_input.text
        self.ids.calc_input.text = f'{prior}/'
        ...

    def decimal_button(self):
        prior = self.ids.calc_input.text
        self.ids.calc_input.text = f'{prior}.'
        ...

    def equals_button(self):
        prior = self.ids.calc_input.text
        
        #   Addition
        if "+" in prior:
            num_list = prior.split("+")
            answer = 0
            for number in num_list:
                answer += int(number)
            
            #   add answer to text box:
            self.ids.calc_input.text = str(answer)




class CalculatorApp(App):
    def build(self):
        self.title = "My Calculator App"
        Window.clearcolor = (0.65, 0.65, 0.65, 1)
        return MyLayout()


if __name__ == "__main__":
    CalculatorApp().run()