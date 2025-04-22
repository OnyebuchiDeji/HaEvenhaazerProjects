"""
    The threading module might not be needed, apart from, perhaps processing the logic, because
    the players take turns and wait.
"""

import socket as sck
import threading


class TicTacToe:
    def __init__(self):
        #   row, column
        self.board = [[" ", " ", " "],
                      [" ", " ", " "],
                      [" ", " ", " "]]
        self.turn = "X"
        self.you = "X"
        self.opponent = "O"
        self.winner = ""
        self.game_over = False

        self.counter = 0

        print("----------------------------------------------")
        print("\tWELCOME TO THE TIC-TACT-TOE\t")
        print("----------------------------------------------")
    
    """
        One Client Runs `host_game`, and another runs `connect_to_game`
    """
    def host_game(self, host: str, port: int):
        server = sck.socket(sck.AF_INET, sck.SOCK_STREAM)
        server.bind((host, port))
        #   Listen for one connection
        server.listen(1)

        client, addr = server.accept()

        self.you = "X"
        self.opponent = "O"
        print(f"You are Player {self.you}")
        threading.Thread(target=self.handle_connection, args=(client,)).start()
        """
           Once a connection is made, close the server right away
           because this server only works with one client
           so no need to wait for more connections

           This shows that all the server does is get a client's details and create
           a socket in the current script to communicate with that client.
        """
        server.close()
    

    def connect_to_game(self, host: str, port: int):
        """Because this client is the connector, they are made to be 'O' """
        client = sck.socket(sck.AF_INET, sck.SOCK_STREAM)
        client.connect((host, port))

        self.you = "O"
        self.opponent = "X"
        print(f"You are Player {self.you}")
        threading.Thread(target=self.handle_connection, args=(client,)).start()
    
    def handle_connection(self, client: sck.socket):
        while not self.game_over:
            if self.turn == self.you:
                #   Get Move from command line
                print(f"\nPlayer {self.you}'s turn\n")
                move = input("\nEnter a move (row, column): ")
                if self.check_valid_move(move.split(',')):
                    #   send this first before exiting to make sure other side
                    #   can process this move to process their win or loss
                    client.send(move.encode('utf-8'))
                    self.apply_move(move.split(','), self.you)
                    self.turn = self.opponent
                else:
                    print("\nInvalid move. Try again.")
            else:
                #   If not your turn, receive play from opponent
                print(f"\nPlayer {self.opponent}'s turn\n")
                data = client.recv(1024)
                if not data:
                    break
                else:
                    #   Update your state values.
                    self.apply_move(data.decode('utf-8').split(','), self.opponent)
                    self.turn = self.you
        client.close()

    def apply_move(self, move: str, player: str):
        """Puts the move in the appropriate position"""
        if self.game_over:
            return
        self.counter += 1
        #   Set the appropriate index to the play the plater made
        self.board[(int(move[0]))][int(move[1])] = player
        self.print_board()
        if self.check_if_won():
            if self.winner == self.you:
                print(f"\nYou Win!\n")
                exit()
            elif self.winner == self.opponent:
                print(f"\n{self.opponent} Won!\n")
                exit()
        else:
            if self.counter == 9:
                print("\nIt is a tie!\n")
                exit()
    
    def check_valid_move(self, move):
        return self.board[int(move[0])][int(move[1])] == " "
    
    def check_if_won(self):
        for row in range(3):
            if self.board[row][0] == self.board[row][1] == self.board[row][2] != " ":
                self.winner = self.board[row][0]
                self.game_over = True
                return True

        for col in range(3):
            if self.board[0][col] == self.board[1][col] == self.board[2][col] != " ":
                self.winner = self.board[0][col]
                self.game_over = True
                return True
                
        #   For diagonals
        if self.board[0][0] == self.board[1][1] == self.board[2][2] != " ":
            self.winner = self.board[0][0]
            self.game_over = True
            return True
        if self.board[0][2] == self.board[1][1] == self.board[2][0] != " ":
            self.winner = self.board[0][2]
            self.game_over = True
            return True
            
        #   If none of the above, return false
        return False

    def print_board(self):
        for row in range(3):
            print("\t|\t".join(self.board[row]))
            if row != 2:
                print("-------------------------------------")


def main():
    game = TicTacToe()
    while True:
        prompt = input("Do you want to be host or not (Y/N) or q to quit?: ")
        prompt = prompt.lower()
        if prompt == "y" or prompt == "n":
            if prompt == "y":
                game.host_game("localhost", 9999)
            else:
                game.connect_to_game("localhost", 9999)
            break
        elif prompt == "q":
            break
        else:
            print("Input Y or N.")
    



if __name__ == "__main__":
    main()
        