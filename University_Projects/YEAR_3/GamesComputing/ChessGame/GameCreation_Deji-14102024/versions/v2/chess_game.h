#pragma once


enum PieceType { PAWN, CASTLE, KNIGHT, BISHOP, QUEEN, KING };
enum PlayerColour { BLACK, WHITE };


class Piece
{
public:
	PieceType type;
	PlayerColour colour;

public:
	Piece() = default;
	Piece(PieceType, PlayerColour);
	int validMove(PlayerColour, int, int, int, int);
};


/**
*	This has access to the global board
*/
class Player
{
private:
	static int player_count;
	static int starting_row;

public:
	PlayerColour player_colour;
	int from_row, from_column, to_row, to_column;
	
public:
	//Player();
	Player(PlayerColour);

	void arrangePieces();
	static void displayBoard();
	void inputMove();
	int validMove();
	void takeTurn();
	void carryOutMove();

	PlayerColour getColour() const { return player_colour; }

};

/*------Globals --------*/

//For the sake of this solution only, four global move variables:
//int fromRow, fromColumn, toRow, toColumn;
inline Piece* board[8][8]; // [row,bottom=0][column,left=0]

/*---------------------------*/

