// C++ Guided Practical Exercise 1

#include <iostream>
#include <cstdlib>
#include "chess_game.h"
using namespace std;




void putPlayersPieces(PlayerColour colour)
{ // Hint: best done with if, for and switch statements
    if (colour == BLACK) {
        int r, c; for (r = 6; r < 8; r++) for (c = 0; c < 8; c++) {
            //  MUST ALWAYS CREATE IT FIRST
            board[r][c] = new Piece;
            (*board[r][c]).colour = colour;

            //  If the row is the 6th, then all are PAWNS
            (*board[r][c]).type = PAWN;

            //  For the 7th row, the unique pieces
            if (r != 6) {
                switch (c)
                {
                    case 3:
                        (*board[r][c]).type = KING;
                        break;
                    case 4:
                        (*board[r][c]).type = QUEEN;
                        break;
                    case 0:
                    case 7:
                        (*board[r][c]).type = CASTLE;
                        break;
                    case 1:
                    case 6:
                        (*board[r][c]).type = KNIGHT;
                        break;
                    case 2:
                    case 5:
                        (*board[r][c]).type = BISHOP;
                        break;
                    }
            }
        }
    }
    else {
        int r, c; for (r = 0; r < 2; r++) for (c = 0; c < 8; c++) {
            board[r][c] = new Piece;
            (*board[r][c]).colour = colour;

            //  If the row is the 2nd, then all are PAWNS
            (*board[r][c]).type = PAWN;

            //  For the first row, the unique PIECES
            if (r != 1) {
                switch (c)
                {
                    case 3:
                        (*board[r][c]).type = KING;
                        break;
                    case 4:
                        (*board[r][c]).type = QUEEN;
                        break;
                    case 0:
                    case 7:
                        (*board[r][c]).type = CASTLE;
                        break;
                    case 1:
                    case 6:
                        (*board[r][c]).type = KNIGHT;
                        break;
                    case 2:
                    case 5:
                        (*board[r][c]).type = BISHOP;
                        break;
                }
            }
        }
    }
}

void displayBoard()
{ int row,column;
  cout << endl << "  ";
  for (column=0;column<=7;column++) cout << (char) (((int)'a')+column);
  cout << endl << " ."; for (column=0;column<=7;column++) cout << '-';
  cout << "." << endl;
  for (row=7;row>=0;row--)
  { cout << 1+row << "|";
    for (column=0;column<=7;column++)
    { if (board[row][column])
      { Piece& piece = *(board[row][column]);
        char pieceCharacter;
        switch (piece.type)
        { case PAWN  : pieceCharacter='P'; break;
          case CASTLE: pieceCharacter='C'; break;
          case KNIGHT: pieceCharacter='N'; break;
          case BISHOP: pieceCharacter='B'; break;
          case QUEEN : pieceCharacter='Q'; break;
          case KING  : pieceCharacter='K'; break;
        }
        if (piece.colour == WHITE)
          pieceCharacter = (char) ((int) pieceCharacter + (int) 'a' - (int) 'A');
        cout << pieceCharacter;
      }
      else cout << ' ';
    }
    cout << "|" << 1+row << "   ";
    switch (row)
    { case 7: cout << "Black is upper case: PCNBQK"; break;
      case 6: cout << "P = Pawn";                    break;
      case 5: cout << "C = Castle";                  break;
      case 4: cout << "N = kNight";                  break;
      case 3: cout << "B = Bishop";                  break;
      case 2: cout << "Q = Queen";                   break;
      case 1: cout << "K = King";                    break;
      case 0: cout << "White is lower case: pcnbqk"; break;
    }
    cout << endl;
  }
  cout << " .";
  for (column=0;column<=7;column++) cout << '-'; cout << "." << endl << "  ";
  for (column=0;column<=7;column++) cout << (char) (((int)'a')+column);
  cout << endl;
}



void inputMove()
{ char fromColumnChar,toColumnChar;
  while (true)
  { cout << endl << "Please enter a move in the form" << endl
         << "FromRow FromColumn ToRow ToColumn, eg. 1 b 3 c :" << endl;
    cin >> fromRow >> fromColumnChar >> toRow >> toColumnChar;
    if (!cin.fail()) break;
    cerr << "Error - Bad input type" << endl;
    cin.clear();          // clear error flags
    cin.ignore(999,'\n'); // ignore rest of input
  }
  fromRow--; toRow--;
  fromColumn = ((int) fromColumnChar) - ((int) 'a');
  toColumn   = ((int) toColumnChar  ) - ((int) 'a');
}

/**
*   Need error checking.
*   Must ensure that the fromPiece and toPiece are actual Piece struct objects
*   i.e. tThe player did not try to move from a place with no piece to another with no piece
*/
void carryOutMove()
{
    //  Make sure the from Piece is an actual Piece object/is initialized
    Piece*& ptr_fromPiece = board[fromRow][fromColumn]; // References to pointers, so
    Piece*& ptr_toPiece = board[toRow][toColumn];       // changing them will change board

    //  If it points to nothing
    if (!ptr_fromPiece)
    {
        std::cout << "\n\nInvalid move! Need to move an actual piece!\n";
        return;
    }
    cout << "from piece: colour = " << ptr_fromPiece->colour << " type = " << ptr_fromPiece->type << "\n";

    //  Initialize the to Piece area
    ptr_toPiece = new Piece;
    ptr_toPiece->colour = ptr_fromPiece->colour;
    ptr_toPiece->type= ptr_fromPiece->type;

    cout << "to piece: colour = " << ptr_toPiece->colour << " type = " << ptr_toPiece->type << "\n";

    //  Now clear the fromPiece
    ptr_fromPiece = 0;
}

int main()
{
       /*   This is the clearing of the board
         they are set to 0 because ENUMS are ints in this example  */
      int r,c; for (r=0;r<8;r++) for (c=0;c<8;c++) board[r][c]=0; // board elements all 0
      //cout << "Lengths: " << std::size(board[r]) << "\n";
      putPlayersPieces(WHITE);
      putPlayersPieces(BLACK);
      while (true)
      { displayBoard();
        inputMove();
        carryOutMove();
      }
      return 0;

      /*int c = 1;
    int myvar[3] = {19, 14, 128};
    std::cout << myvar[c + 1] << "/n";*/
}
