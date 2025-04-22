// C++ Guided Practical Exercise 1

#include <iostream>
#include <cstdlib>
#include "chess_game.h"
using namespace std;




int main()
{
    /*
        This is the clearing of the board
        they are set to 0 because ENUMS are ints in this example
    */
    int r,c; for (r=0;r<8;r++) for (c=0;c<8;c++) board[r][c]=0; // board elements all 0
    //cout << "Lengths: " << std::size(board[r]) << "\n";
    Player p1 = Player(WHITE);
    Player p2 = Player(BLACK);
    while (true)
    {
        Player::displayBoard();
        p1.takeTurn();
        p2.takeTurn();
    }
    return 0;
}
