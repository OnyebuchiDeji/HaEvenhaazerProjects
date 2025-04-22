#pragma once


enum PieceType { PAWN, CASTLE, KNIGHT, BISHOP, QUEEN, KING };
enum PlayerColour { BLACK, WHITE };


struct Piece
{
	PieceType type;
	PlayerColour colour;

};


/*------Globals --------*/

//For the sake of this solution only, four global move variables:
int fromRow, fromColumn, toRow, toColumn;
Piece* board[8][8]; // [row,bottom=0][column,left=0]

/*---------------------------*/
