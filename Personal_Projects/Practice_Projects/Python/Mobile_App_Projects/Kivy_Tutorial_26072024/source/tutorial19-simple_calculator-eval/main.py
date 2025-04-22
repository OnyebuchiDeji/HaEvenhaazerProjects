"""
    Date: Wed-21-July-2024
    
    This tutorial demonstrates a Simple Calculator App

    Here, fixed the decimal point button
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
Builder.load_file("source/tutorial19-simple_calculator-eval/base_style.kv")

g_error_count = 0

class MyLayout(Widget):
    
    def clear_input(self):
        self.ids.calc_input.text = "0"

    def button_press(self, button):
        #   Get what was previously in the calc input space
        prior = self.ids.calc_input.text

        if prior == "0" or prior == "N/A":
            self.ids.calc_input.text = ""
            self.ids.calc_input.text = f'{button}'
        else:
            self.ids.calc_input.text = f'{prior}{button}'

    def math_button(self, sign):
        prior = self.ids.calc_input.text
        if prior[-1] != sign:
            self.ids.calc_input.text = f'{prior}{sign}'

    
    def equals_button(self):
        global g_error_count
        prior:str = self.ids.calc_input.text
        try:
            prior = prior.replace("x", "*")
            self.ids.calc_input.text = str(eval(prior))
        except (ZeroDivisionError, SyntaxError) as err:
            if (g_error_count >= 3):
                self.ids.calc_input.text = "BRO"
                g_error_count = 0
            else:
                g_error_count += 1
                self.ids.calc_input.text = "N/A"


        
    def remove_button(self):
        prior = self.ids.calc_input.text
        self.ids.calc_input.text = prior[:-1]

    def switch_sign_button(self):
        prior:str = self.ids.calc_input.text
        index_offset = 0
        # print(prior.find("(", -1))
        for i in range(len(prior) - 1, 0, -1):
            if prior.find("(", -1) != -1:
                index = prior.find("(-", -1)
                val = prior[index::1]
                new_val = val.strip("-")
                new_val = val.strip(")")
                new_val = val.strip("(")
                print(val)
                print("th")
                # self.ids.calc_input.text = prior[0:index_offset] + new_val
            elif prior[i] == '-' or prior[i] == "+":
                val = prior[len(prior) -index_offset::1]
                new_val = f"(-{val})"
                self.ids.calc_input.text = prior[0:len(prior) - index_offset] + new_val
                print(val)
                print(new_val)
                print(prior[0:index_offset+1] + new_val)
            index_offset += 1








class CalculatorApp(App):
    def build(self):
        self.title = "My Calculator App"
        Window.clearcolor = (0.65, 0.65, 0.65, 1)
        return MyLayout()


if __name__ == "__main__":
    CalculatorApp().run()