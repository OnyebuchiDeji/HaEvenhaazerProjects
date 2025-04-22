"""
    Episode 6-9: Rock Paper Scissors Game
"""

class Game:
    def __init__(self, id):
        self.p1_went = False
        self.p2_went = False
        self.ready = False
        self.id = id
        self.moves = [None, None]
        self.wins = [0, 0]
        self.ties = 0
    
    def get_player_move(self, p):
        """
            p is in range [0, 1] -> player 1 and player 2
            Gets the move of the next player
        """
        return self.moves[p]
    
    def play(self, player, move):
        """
            Updates the moves list with that Player's move
        """
        self.moves[player] = move
        if player == 0:
            self.p1_went = True
        else:
            self.p2_went = True
        
    def connected(self):
        """
            Tells if the Players are connected.
            With this, we can determine whether to show "waiting for player"
            or not
        """
        return self.ready
    
    def both_went(self):
        return self.p1_went and self.p2_went
    
    def winner(self):
        """
            Tells which player has won the game.
            It involves checking the 9 possible cases
            since there's three moves each player can do.
        """
        #   This gets the first letter of the move...
        #   as it's easier to store R, P, S rather than
        #   Rock, Paper, Scissors
        p1 = self.moves[0].upper()[0]
        p2 = self.moves[1].upper()[0]

        winner = -1 #   Default for a tie

        if p1 == "R" and p2 == "S":
            winner = 0
        elif p1 == "S" and p2 == "R":
            winner = 1
        elif p1 == "P" and p2 == "R":
            winner = 0
        elif p1 == "R" and p2 == "P":
            winner = 1
        elif p1 == "S" and p2 == "P":
            winner = 0
        elif p1 == "P" and p2 == "S":
            winner = 1
        
        return winner

    def reset_went(self):
        self.p1_went = False
        self.p2_went = False