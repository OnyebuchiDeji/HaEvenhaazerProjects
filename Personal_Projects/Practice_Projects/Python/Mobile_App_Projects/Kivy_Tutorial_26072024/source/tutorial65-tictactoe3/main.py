"""
    Date: Mon-19-Aug-2024

    This episode is a continuation of episode 65, creating Tictactoe Game.
    Here the logic is changed, but is basically the same as the prior...
    but does not need the hard coding.
    There might be "magic numbers" though.
    These are the "algorithms" that we said we'll use in the last episode

    Apart from that, this episode shows how to keep track of the score until a new game.


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
    x_score = 0
    o_score = 0

    """
        These are the strides used in the algorithm for the logic to determine the winner
    """
    #   The (combinations, factor, and stride)
    across = (3, 3, 1)
    downward = (3, 1, 3)
    diagonal = (2, 2, 4)

    
    def oninit(self):
        self.title = "TicTacToe"
        Window.clearcolor = (0.3, 0.25, 0.3, 1)
        self.theme_cls.theme_style = "Light" if self.light_theme else "Dark"
        self.theme_cls.primary_palette = "Fuchsia"
        self.theme_cls.accent_palette = "Mediumorchid"
    

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
        self.root.ids['id_info_label'].score_text = self.turn + " GOES FIRST!"

        for btn_obj in (self.root.ids).values():
            if isinstance(btn_obj, Button):
                btn_obj.disabled = False
                btn_obj.text = ""
                btn_obj.color = "grey"
                btn_obj.bold = False
    
    def new_game(self):
        self.restart_game()
        self.x_score = 0
        self.y_score = 0
        self.update_score()

    def on_press(self, btn):
        if self.turn == "X":
            btn.text = self.turn
            self.turn = "O"
        else:
            btn.text = self.turn
            self.turn = "X"

        btn.disabled = True
        self.root.ids['id_info_label'].score_text = f"{self.turn}'s Turn!"
        self.execute_game_logic()
    
    def build_btns_ref_list(self):
        for btn_obj in (self.root.ids).values():
            if isinstance(btn_obj, Button):
                self.btns_ref_list.append(btn_obj)
        # print(len(self.btns_ref_list))

    def win_logic(self, combinations, factor, stride):
        """
            It uses those two parameters
        """
        start_index = 0
        if stride != 4:
            for i in range(combinations):
                start_index = i * factor
                a, b, c = (self.btns_ref_list[start_index],
                            self.btns_ref_list[start_index + stride * 1],
                            self.btns_ref_list[start_index + stride * 2])
                val = a.text == b.text == c.text
                self.winner = self.btns_ref_list[start_index + stride].text if val else ""
                if self.winner != "":
                    self.declare_winner(a, b, c)
                    #   Disable Other Buttons:
                    for btn_obj in self.btns_ref_list:
                        btn_obj.disabled = True

            return self.winner != ""
        else:
            for i in range(combinations):
                start_index = i * factor
                if start_index != 2:
                    a, b, c = (self.btns_ref_list[start_index],
                                self.btns_ref_list[start_index + stride * 1],
                                self.btns_ref_list[start_index + stride * 2])
                    val = a.text == b.text == c.text
                    self.winner = self.btns_ref_list[start_index + stride].text if val else ""
                    if self.winner != "":
                        self.declare_winner(a, b, c)
                        #   Disable Other Buttons:
                        for btn_obj in self.btns_ref_list:
                            btn_obj.disabled = True
                else:
                    stride = 2
                    a, b, c = (self.btns_ref_list[start_index],
                                self.btns_ref_list[start_index + stride * 1],
                                self.btns_ref_list[start_index + stride * 2])
                    val = a.text == b.text == c.text
                    self.winner = self.btns_ref_list[start_index + stride].text if val else ""
                    if self.winner != "":
                        self.declare_winner(a, b, c)
                        #   Disable Other Buttons:
                        for btn_obj in self.btns_ref_list:
                            btn_obj.disabled = True
            


    def execute_game_logic(self):
        """
            Keeps track of Win, Lose, or Draw
        """
        #   Across
        if (self.win_logic(*self.across)):
            return
        #   Down
        if (self.win_logic(*self.downward)):
            return
        #   Diagonal
        if (self.win_logic(*self.diagonal)):
            return

        ##  Check if there are no other turns
        filled_btn_count = 0
        for btn in self.btns_ref_list:
            if btn.text != "":
                filled_btn_count += 1
        draw = True if filled_btn_count >= 9 else False
        if draw: self.declare_draw()
    
    def update_score(self, newgame=False):
        is_winning = "Game Started"
        if not newgame:
            is_winning = "X is Winning!" if self.x_score > self.o_score else (lambda x: "Neck to Neck!" if self.x_score == self.o_score else "O is Winning!")(1)

        self.root.ids['id_score_label'].score_text = f"Player X: {self.x_score} | Player O: {self.o_score}\n{is_winning}"    

    def declare_winner(self, *btns):
        self.root.ids['id_info_label'].score_text = f"{self.winner} Wins!"    
        if btns[0].text == "X":
            self.x_score += 1
        else:
            self.o_score += 1

        self.update_score()

        ##  Change Color of Winning Button Match
        for btn in btns:
            btn.color = "red"
            btn.bold = True
    
    def declare_draw(self):
        self.root.ids['id_info_label'].score_text = f"Draw!"
        

    

        
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

