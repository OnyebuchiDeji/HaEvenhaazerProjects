"""
    Date: Mon-19-Aug-2024

    This episode is a continuation of episode 64, creating Tictactoe Game.
    Here the logic is added.

    Tried to add delays but it didn't work. time.sleep and Clock.usleep()
    activate asynchronously. Hence the Label does not get enough time to change before execution is paused.

    Consider the logic that we made. It is not how it was done in the Episode.
    This one does not duplicate code and makes good use of for loops.
    
    These attributes represent the indices of each button in self.btns_ref_list = []
    which, if they have the same Text, that player wins.
    So for each of these combinations of indices, if the correspondng buttons from the list
    have the same text, then that is the winner
        accross_indices = [(0, 1, 2), (3, 4, 5), (6, 7, 8)]
        diagonal_indices = [(0, 4, 8), (2, 4, 6)]
        down_indices = [(0, 3, 6), (1, 4, 7), (2, 5, 8)]
    Here they are hard coded.
    But in the next tutorial, I use algorithms to get them.


"""

from kivymd.app import MDApp
from kivy.core.window import Window
from kivy.lang import Builder
from kivymd.uix.boxlayout import MDBoxLayout
from kivy.uix.button import Button
from kivy.clock import Clock

import time

class MyBoxLayout(MDBoxLayout):
    ...
    

#   The KivyMD app
class MyApp(MDApp):
    light_theme = False
    theme_text_l = "L"
    theme_text_d = "D"

    #   Game App Attributes
    game_turn = "X"
    turn = game_turn
    winner = ""
    btns_ref_list = []

    """
        These attributes represent the indices of each button in self.btns_ref_list = []
        which, if they have the same Text, that player wins.
        So for each of these combinations of indices, if the correspondng buttons from the list
        have the same text, then that is the winner
        Here it is hard coded.
    """
    #   The indices for each line that can be checked for a win
    ##  Accross
    accross_indices = [(0, 1, 2), (3, 4, 5), (6, 7, 8)]
    diagonal_indices = [(0, 4, 8), (2, 4, 6)]
    down_indices = [(0, 3, 6), (1, 4, 7), (2, 5, 8)]
    


    
    def oninit(self):
        self.title = "TicTacToe"
        Window.clearcolor = (0.3, 0.25, 0.3, 1)
        self.theme_cls.theme_style = "Light" if self.light_theme else "Dark"
        self.theme_cls.primary_palette = "Blueviolet"
        self.theme_cls.accent_palette = "Floralwhite"
    

    def build(self):
        self.oninit()
        #   Designate the .kv design file
        Builder.load_file("base_style.kv")
        self.root = MyBoxLayout()
        return self.root
    
    def on_start(self):
        self.build_btns_ref_list()

    def toggle_theme(self):
        self.light_theme = not self.light_theme
        self.theme_cls.theme_style = "Light" if self.light_theme else "Dark"
        self.root.ids.id_theme_btn.text = self.theme_text_l if self.light_theme else self.theme_text_d
    
    def restart_game(self):
        """Reset Everything"""
        # time.sleep(3)
        if self.game_turn == "X":
            self.game_turn = "O"
        else:
            self.game_turn = "X"
        self.turn = self.game_turn
        self.root.ids['id_score_label'].score_text = self.turn + " GOES FIRST!"

        for btn_obj in (self.root.ids).values():
            if isinstance(btn_obj, Button):
                btn_obj.disabled = False
                btn_obj.text = ""
                btn_obj.color = "grey"
                btn_obj.bold = False
            

    def on_press(self, btn):
        if self.turn == "X":
            btn.text = self.turn
            self.turn = "O"
        else:
            btn.text = self.turn
            self.turn = "X"

        btn.disabled = True
        self.root.ids['id_score_label'].score_text = f"{self.turn}'s Turn!"
        self.execute_game_logic()
    
    def build_btns_ref_list(self):
        for btn_obj in (self.root.ids).values():
            if isinstance(btn_obj, Button):
                self.btns_ref_list.append(btn_obj)
        # print(len(self.btns_ref_list))

    def win_logic(self, logic_indices):
        """
            It takes the corresponding indices to perform the logic that uses
            those indices to get whether there is a winner
        """
        for combination in logic_indices:
            a, b, c = (self.btns_ref_list[combination[0]], self.btns_ref_list[combination[1]], self.btns_ref_list[combination[2]])
            val = a.text == b.text == c.text
            self.winner = self.btns_ref_list[combination[0]].text if val else ""
            if self.winner != "":
                self.declare_winner(a, b, c)
                #   Disable Other Buttons:
                for btn_obj in self.btns_ref_list:
                    btn_obj.disabled = True

                return self.winner != ""

    def execute_game_logic(self):
        """
            Keeps track of Win, Lose, or Draw
        """
        #   Across
        if (self.win_logic(self.accross_indices)):
            return
        #   Down
        if (self.win_logic(self.down_indices)):
            return
        #   Diagonal
        if (self.win_logic(self.diagonal_indices)):
            return

        ##  Check if there are no other turns
        filled_btn_count = 0
        # count = 0
        for btn in self.btns_ref_list:
            # count += 1
            # print(btn)
            # print(count)
            if btn.text != "":
                filled_btn_count += 1
        draw = True if filled_btn_count >= 9 else False
        if draw: self.declare_draw()
    
    def declare_winner(self, *btns):
        self.root.ids['id_score_label'].score_text = f"{self.winner} Wins!"    
        for btn in btns:
            btn.color = "red"
            btn.bold = True
    
    def declare_draw(self):
        self.root.ids['id_score_label'].score_text = f"Draw!"
        

    
            
        
if __name__ == "__main__":
    MyApp().run()


#   'Red', 'Pink', 'Purple', 'DeepPurple',
#   'Indigo', 'Blue', 'LightBlue', 'Cyan',
#   'Teal', 'Green', 'LightGreen', 'Lime',
#   'Yellow', 'Amber', 'Orange', 'DeepOrange',
#   'Brown', 'Gray', 'BlueGray'.

"""
ThemeManager.primary_palette must be one of:
 ['Aliceblue', 'Antiquewhite', 'Aqua', 'Aquamarine', 'Azure', 'Beige', 'Bisque', 'Black', 'Blanchedalmond',
 'Blue', 'Blueviolet', 'Brown', 'Burlywood', 'Cadetblue', 'Chartreuse', 'Chocolate', 'Coral', 'Cornflowerblue',
 'Cornsilk', 'Crimson', 'Cyan', 'Darkblue', 'Darkcyan', 'Darkgoldenrod', 'Darkgray', 'Darkgrey', 'Darkgreen',
 'Darkkhaki', 'Darkmagenta', 'Darkolivegreen', 'Darkorange', 'Darkorchid', 'Darkred', 'Darksalmon', 'Darkseagreen', 'Darkslateblue',
 'Darkslategray', 'Darkslategrey', 'Darkturquoise', 'Darkviolet', 'Deeppink', 'Deepskyblue', 'Dimgray', 'Dimgrey',
 'Dodgerblue', 'Firebrick', 'Floralwhite', 'Forestgreen', 'Fuchsia', 'Gainsboro', 'Ghostwhite', 'Gold', 'Goldenrod', 'Gray',
 'Grey', 'Green', 'Greenyellow', 'Honeydew', 'Hotpink', 'Indianred', 'Indigo', 'Ivory', 'Khaki', 'Lavender', 'Lavenderblush',
 'Lawngreen', 'Lemonchiffon', 'Lightblue', 'Lightcoral', 'Lightcyan', 'Lightgoldenrodyellow', 'Lightgreen', 'Lightgray', 'Lightgrey',
 'Lightpink', 'Lightsalmon', 'Lightseagreen', 'Lightskyblue', 'Lightslategray', 'Lightslategrey', 'Lightsteelblue', 'Lightyellow', 'Lime',
 'Limegreen', 'Linen', 'Magenta', 'Maroon', 'Mediumaquamarine', 'Mediumblue', 'Mediumorchid', 'Mediumpurple', 'Mediumseagreen', 'Mediumslateblue',
 'Mediumspringgreen', 'Mediumturquoise', 'Mediumvioletred', 'Midnightblue', 'Mintcream', 'Mistyrose', 'Moccasin', 'Navajowhite', 'Navy', 'Oldlace',
 'Olive', 'Olivedrab', 'Orange', 'Orangered', 'Orchid', 'Palegoldenrod', 'Palegreen', 'Paleturquoise', 'Palevioletred', 'Papayawhip', 'Peachpuff', 'Peru',
 'Pink', 'Plum', 'Powderblue', 'Purple', 'Red', 'Rosybrown', 'Royalblue', 'Saddlebrown', 'Salmon', 'Sandybrown', 'Seagreen', 'Seashell', 'Sienna', 'Silver',
 'Skyblue', 'Slateblue', 'Slategray', 'Slategrey', 'Snow', 'Springgreen', 'Steelblue', 'Tan', 'Teal', 'Thistle', 'Tomato', 'Turquoise', 'Violet', 'Wheat', 'White',
 'Whitesmoke', 'Yellow', 'Yellowgreen']
"""

