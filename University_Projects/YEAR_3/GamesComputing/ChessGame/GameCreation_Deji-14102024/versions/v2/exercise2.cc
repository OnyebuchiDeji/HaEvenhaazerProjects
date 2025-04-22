/**
*	This implements classes
*	It has the logic to reject illegal moves
*	
*/

#include <iostream>
#include <cstdlib>
#include "chess_game.h"

using namespace std;



Piece::Piece(PieceType type, PlayerColour colour)
{
	this->type = type;
	this->colour = colour;

}

int Player::player_count = 0;
int Player::starting_row = 0;


Player::Player(PlayerColour colour)
{
    //  To determine player 1 and 2
    //  to decide which to make in CAPS
	player_count += 1;
    if (player_count == 1) starting_row = 0;
    else starting_row = 6;

	player_colour = colour;
    from_row = 0;
    from_column = 0;
    to_row = 0;
    to_column = 0;
	arrangePieces();
}

void Player::arrangePieces()
{
    int r, c; for (r = starting_row; r < starting_row + 2; r++) for (c = 0; c < 8; c++) 
    {
        //  All pawns by default
        enum PieceType piece_type = PAWN;

        int pawn_row = 0;
        if (starting_row == 0) pawn_row = 1;
        else pawn_row = 6;

        if (r != pawn_row) {
            switch (c)
            {
            case 3:
                piece_type = KING;
                break;
            case 4:
                piece_type = QUEEN;
                break;
            case 0:
            case 7:
                piece_type = CASTLE;
                break;
            case 1:
            case 6:
                piece_type = KNIGHT;
                break;
            case 2:
            case 5:
                piece_type = BISHOP;
                break;
            }
        }

        board[r][c] = new Piece(piece_type, player_colour);
    }
}



void Player::inputMove()
{
    char fromColumnChar, toColumnChar;
    while (true)
    {
        cout << endl << "Please enter a move in the form" << endl
            << "FromRow FromColumn ToRow ToColumn, eg. 1 b 3 c :" << endl;
        cin >> from_row >> fromColumnChar >> to_row >> toColumnChar;
        if (!cin.fail()) break;
        cerr << "Error - Bad input type" << endl;
        cin.clear();          // clear error flags
        cin.ignore(999, '\n'); // ignore rest of input
    }
    from_row--; to_row--;
    from_column = ((int)fromColumnChar) - ((int)'a');
    to_column = ((int)toColumnChar) - ((int)'a');
}

void Player::displayBoard()
{
    int row, column;
    cout << endl << "  ";
    for (column = 0; column <= 7; column++) cout << (char)(((int)'a') + column);
    cout << endl << " ."; for (column = 0; column <= 7; column++) cout << '-';
    cout << "." << endl;
    for (row = 7; row >= 0; row--)
    {
        cout << 1 + row << "|";
        for (column = 0; column <= 7; column++)
        {
            if (board[row][column])
            {
                Piece& piece = *(board[row][column]);
                char pieceCharacter;
                switch (piece.type)
                {
                case PAWN: pieceCharacter = 'P'; break;
                case CASTLE: pieceCharacter = 'C'; break;
                case KNIGHT: pieceCharacter = 'N'; break;
                case BISHOP: pieceCharacter = 'B'; break;
                case QUEEN: pieceCharacter = 'Q'; break;
                case KING: pieceCharacter = 'K'; break;
                }
                if (piece.colour == WHITE)
                    pieceCharacter = (char)((int)pieceCharacter + (int)'a' - (int)'A');
                cout << pieceCharacter;
            }
            else cout << ' ';
        }
        cout << "|" << 1 + row << "   ";
        switch (row)
        {
        case 7: cout << "Black is upper case: PCNBQK"; break;
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
    for (column = 0; column <= 7; column++) cout << '-'; cout << "." << endl << "  ";
    for (column = 0; column <= 7; column++) cout << (char)(((int)'a') + column);
    cout << endl;
}

void Player::takeTurn()
{
    cout << "\n\nPlayer " << player_colour << "'s Turn\n";
    while (true)
    {
        displayBoard();
        inputMove();
        if (validMove()) {
            break;
        }
    }
    carryOutMove();
}

/**
*   Need error checking.
*   Must ensure that the fromPiece and toPiece are actual Piece struct objects
*   i.e. tThe player did not try to move from a place with no piece to another with no piece
*/
void Player::carryOutMove()
{
    //  Make sure the from Piece is an actual Piece object/is initialized
    Piece*& ptr_fromPiece = board[from_row][from_column]; // References to pointers, so
    Piece*& ptr_toPiece = board[to_row][to_column];       // changing them will change board

    //  If it points to nothing
    if (!ptr_fromPiece)
    {
        std::cout << "\n\nInvalid move! Need to move an actual piece!\n";
        return;
    }
    cout << "from piece: colour = " << ptr_fromPiece->colour << " type = " << ptr_fromPiece->type << "\n";

    //  Initialize the to Piece area
    ptr_toPiece = new Piece();
    ptr_toPiece->colour = ptr_fromPiece->colour;
    ptr_toPiece->type = ptr_fromPiece->type;

    cout << "to piece: colour = " << ptr_toPiece->colour << " type = " << ptr_toPiece->type << "\n";

    //  Now clear the fromPiece
    ptr_fromPiece = 0;
}

/*--------------    FROM THE `validMove.cpp`    ----------------*/
// C++ Guided Practical Exercise 2 - validMove.cc - code segments for student download
// This file contains the functions Piece::validMove and Player::validMove

#include <cstring>


int Piece::validMove(PlayerColour testColour,
    int fromRow, int fromColumn, int toRow, int toColumn)
{ // Note: The function that calls validMove should have already checked that the four
  //       parameters fromRow, fromColumn, toRow and toColumn are each between 0 and 7.
  //       It would be to late to do that here, as this piece would not exist.
    if (board[fromRow][fromColumn] != this) // Check that this is the right piece
    {
        cerr << "\nInternal error WrongPiece detected by Piece::validMove" << endl;
        exit(1); // should never happen
    }
    if (testColour != colour)
    {
        cerr << "\nError - You can only move your own pieces" << endl;
        return 0; // not a valid move
    }
    int dy = toRow - fromRow;        // dy and dx are the row and column differences
    int dx = toColumn - fromColumn;  //   between the From and To positions
    int ady = (dy > 0) ? dy : -dy;       // ady and adx are the absolute
    int adx = (dx > 0) ? dx : -dx;       //   values of dy and dx
    int sdy = ady ? (dy / ady) : 0;      // sdy and sdx are the signs
    int sdx = adx ? (dx / adx) : 0;      //   (1 if +ve, -1 if -ve, 0 if 0) of dy and dx
    if ((!adx) && (!ady))
    {
        cerr << "\nError - You must MOVE a piece" << endl;
        return 0; // not a valid move
    }
    Piece* ptr_toPiece = board[toRow][toColumn];
    if (ptr_toPiece && (ptr_toPiece->colour == colour))
    {
        cerr << "\nError - You cannot take one of your own pieces" << endl;
        return 0; // not a valid move
    }
    // Having done the obvious, remains to check legality of move, ignoring
    // en passant, pawn promotion, castling, check and checkmate.
    if (type != KNIGHT)                         // Only a knight can jump over pieces.
    {
        if (adx && ady && (adx != ady))           // And all other pieces move
        {
            cerr << "\nError - illegal move" << endl; // horizontally/vertically/diagonally.
            return 0; // not a valid move
        }
        int r, c; // Now check that all the squares that the move passes over are empty:
        for (r = fromRow + sdy, c = fromColumn + sdx; (r != toRow) || (c != toColumn); r += sdy, c += sdx)
            if (board[r][c])
            {
                cerr << "\nError - illegal move" << endl;
                return 0; // not a valid move
            }
    }
    switch (type)
    {
    case PAWN: if ((colour == WHITE) && (dy <= 0)) break; // Check going in the
        if ((colour == BLACK) && (dy >= 0)) break; // right direction.
        if ((ady > 2) || (adx > 1)) break;
        if (adx) // adx==1
        {
            if (ady == 2) break;
            // ady==1
            if (ptr_toPiece)                 return 1; // a valid move
            // else break; // not needed
        }
        else     // adx==0
            if (!ptr_toPiece)
            {
                if (ady == 1)                    return 1; // a valid move
                // ady==2
                if ((sdy == 1) && (fromRow == 1)) return 1; // a valid move
                if ((sdy == -1) && (fromRow == 6)) return 1; // a valid move
            }
        break;
    case CASTLE: if ((!adx) || (!ady))              return 1; // a valid move
        break;
    case KNIGHT: if ((adx == 2) && (ady == 1))          return 1; // a valid move
        if ((adx == 1) && (ady == 2))          return 1; // a valid move
        break;
    case BISHOP: if (adx == ady)                    return 1; // a valid move
        break;
    case QUEEN:                                    return 1; // a valid move
        // break; // not needed
    case KING: if ((adx <= 1) && (ady <= 1))          return 1; // a valid move
        break;
    default: cerr << "\nInternal error BadType detected by Piece::validMove" << endl;
        exit(1); // should never happen
    }
    cerr << "\nError - illegal move" << endl;
    return 0; // if have reached here then not a valid move
}

// -------------------------------------------------------------------------------------

int Player::validMove()
{
    int inRange = 0; // now check and set to 1 if move is in range:
    if ((from_row < 0) || (from_row > 7))
        cerr << "\nError - FromRow must be between 1 and 8" << endl;
    else if ((from_column < 0) || (from_column > 7))
        cerr << "\nError - FromColumn must be between a and h" << endl;
    else if ((to_row < 0) || (to_row > 7))
        cerr << "\nError - ToRow must be between 1 and 8" << endl;
    else if ((to_column < 0) || (to_column > 7))
        cerr << "\nError - ToColumn must be between a and h" << endl;
    else inRange = 1;
    if (!inRange) return 0; // not a valid move
    if (!(board[from_row][from_column]))
    {
        cerr << "\nError - There is no piece in your From position" << endl;
        return 0; // not a valid move
    }
    return board[from_row][from_column]->validMove(player_colour, from_row, from_column, to_row, to_column);
}
