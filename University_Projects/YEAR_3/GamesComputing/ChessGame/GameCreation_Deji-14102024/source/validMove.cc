// C++ Guided Practical Exercise 2 - validMove.cc - code segments for student download
// This file contains the functions Piece::validMove and Player::validMove

#include <iostream>
#include <cstdlib>
#include <cstring>
#include "chess_game.h"
using namespace std;


int Piece::validMove(PlayerColour testColour,
                     int fromRow,int fromColumn,int toRow,int toColumn)
{ // Note: The function that calls validMove should have already checked that the four
  //       parameters fromRow, fromColumn, toRow and toColumn are each between 0 and 7.
  //       It would be to late to do that here, as this piece would not exist.
  if (board[fromRow][fromColumn] != this) // Check that this is the right piece
  { cerr << "Internal error WrongPiece detected by Piece::validMove" << endl;
    exit(1); // should never happen
  }
  if (testColour != colour)
  { cerr << "Error - You can only move your own pieces" << endl;
    return 0; // not a valid move
  }
  int dy=toRow-fromRow;        // dy and dx are the row and column differences
  int dx=toColumn-fromColumn;  //   between the From and To positions
  int ady=(dy>0)?dy:-dy;       // ady and adx are the absolute
  int adx=(dx>0)?dx:-dx;       //   values of dy and dx
  int sdy=ady?(dy/ady):0;      // sdy and sdx are the signs
  int sdx=adx?(dx/adx):0;      //   (1 if +ve, -1 if -ve, 0 if 0) of dy and dx
  if ((!adx) && (!ady))
  { cerr << "Error - You must MOVE a piece" << endl;
    return 0; // not a valid move
  }
  Piece* ptr_toPiece = board[toRow][toColumn];
  if (ptr_toPiece && (ptr_toPiece->colour == colour))
  { cerr << "Error - You cannot take one of your own pieces" << endl;
    return 0; // not a valid move
  }
  // Having done the obvious, remains to check legality of move, ignoring
  // en passant, pawn promotion, castling, check and checkmate.
  if (type != KNIGHT)                         // Only a knight can jump over pieces.
  { if (adx && ady && (adx != ady))           // And all other pieces move
    { cerr << "Error - illegal move" << endl; // horizontally/vertically/diagonally.
      return 0; // not a valid move
    }
    int r,c; // Now check that all the squares that the move passes over are empty:
    for (r=fromRow+sdy,c=fromColumn+sdx;(r!=toRow)||(c!=toColumn);r+=sdy,c+=sdx)
      if (board[r][c])
      { cerr << "Error - illegal move" << endl;
        return 0; // not a valid move
      }
  }
  switch (type)
  { case PAWN  : if ((colour==WHITE) && (dy<=0)) break; // Check going in the
                 if ((colour==BLACK) && (dy>=0)) break; // right direction.
                 if ((ady>2) || (adx>1)) break;
                 if (adx) // adx==1
                 { if (ady==2) break;
                   // ady==1
                   if (ptr_toPiece)                 return 1; // a valid move
                   // else break; // not needed
                 }
                 else     // adx==0
                   if (!ptr_toPiece)
                   { if (ady==1)                    return 1; // a valid move
                     // ady==2
                     if ((sdy== 1) && (fromRow==1)) return 1; // a valid move
                     if ((sdy==-1) && (fromRow==6)) return 1; // a valid move
                   }
                 break;
    case CASTLE: if ((!adx) || (!ady))              return 1; // a valid move
                 break;
    case KNIGHT: if ((adx==2) && (ady==1))          return 1; // a valid move
                 if ((adx==1) && (ady==2))          return 1; // a valid move
                 break;
    case BISHOP: if (adx == ady)                    return 1; // a valid move
                 break;
    case QUEEN :                                    return 1; // a valid move
                 // break; // not needed
    case KING  : if ((adx<=1) && (ady<=1))          return 1; // a valid move
                 break;
    default    : cerr << "Internal error BadType detected by Piece::validMove" << endl;
                 exit(1); // should never happen
  }
  cerr << "Error - illegal move" << endl;
  return 0; // if have reached here then not a valid move
}

// -------------------------------------------------------------------------------------

int Player::validMove()
{ int inRange=0; // now check and set to 1 if move is in range:
  if ((fromRow < 0) || (fromRow > 7))
    cerr << "Error - FromRow must be between 1 and 8" << endl;
  else if ((fromColumn < 0) || (fromColumn > 7))
    cerr << "Error - FromColumn must be between a and h" << endl;
  else if ((toRow < 0) || (toRow > 7))
    cerr << "Error - ToRow must be between 1 and 8" << endl;
  else if ((toColumn < 0) || (toColumn > 7))
    cerr << "Error - ToColumn must be between a and h" << endl;
  else inRange=1;
  if (!inRange) return 0; // not a valid move
  if (!(board[fromRow][fromColumn]))
  { cerr << "Error - There is no piece in your From position" << endl;
    return 0; // not a valid move
  }
  return board[fromRow][fromColumn]->validMove(colour,fromRow,fromColumn,toRow,toColumn);
}
