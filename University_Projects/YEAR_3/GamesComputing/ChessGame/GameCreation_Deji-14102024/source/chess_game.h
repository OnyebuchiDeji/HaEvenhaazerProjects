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
	virtual int validMove(PlayerColour, int, int, int, int);
	virtual char getType() const = 0;
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
	Player() = default;
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


class Pawn : public Piece
{
public:
	Pawn(PlayerColour colour);
	char getType() const override { return 'P'; }
	//int validMove (PlayerColour, int, int, int, int) override;
};

class Castle : public Piece
{
public:
	Castle (PlayerColour colour);
	char getType() const override { return 'C'; }
	//int validMove (PlayerColour, int, int, int, int) override;
};

class Knight : public Piece
{
public:
	Knight(PlayerColour colour);
	char getType() const override { return 'N'; }
	//int validMove (PlayerColour, int, int, int, int) override;
};

class Bishop : public Piece
{
public:
	Bishop(PlayerColour colour);
	char getType() const override { return 'B'; }
	//int validMove (PlayerColour, int, int, int, int) override;
};

class Queen : public Piece
{
public:
	Queen(PlayerColour colour);
	char getType() const override { return 'Q'; }
	//int validMove (PlayerColour, int, int, int, int) override;
};

class King : public Piece
{
public:
	King(PlayerColour colour);
	char getType() const override { return 'K'; }
	//int validMove (PlayerColour, int, int, int, int) override;
};