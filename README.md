1 - Snort
1.1 Rules of the game
This game was created in 1970 by Simon Norton.

Two players compete on a two-dimensional square board of n
squares by n
squares initially empty.

The first player has white pawns and the second has black pawns.

In turn, each player places a pawn on an empty square not orthogonally adjacent to a square containing an opponent's pawn.

The winner is the last player to be able to place one of his pawns. Or equivalently, a player loses the game as soon as he can no longer place one of his pawns on the board.

1.2 - Implementation of this game in Python
It is strongly recommended that you read this entire part before starting to code.

Important notes:

It may be possible to implement subroutines in addition to those requested.
The board will naturally be a two-dimensional list of integers equal to 0, 1 or 2. An empty square will be represented by 0, a pawn of the first player by 1 and a pawn of the second by 2.
Rather than regularly recalculating the dimension of this list, we will prefer to pass it as a parameter of our subroutines.
The example of the visual rendering of the program is only indicative, you can improve it.
Notations of the parameters of the subroutines that we will implement:

"board": two-dimensional list of integers equal to 0, 1 or 2 representing the game board.
"n": strictly positive integer equal to the number of rows and columns of "board".
"player": integer representing the player whose turn it is (for example 1 for the first player and 2 for the second).
"i", "j": any integers.
Implement the following subroutines:

A function "newBoard(n)" that returns a two-dimensional list representing the initial state of a game board of n squares by n squares.
A procedure "displayBoard(board, n)" that displays the board on the console. An empty square will be represented by a ‘.’, a white pawn by an ‘x’ and a black pawn by an ‘o’. The rows and columns will be numbered (starting at 1) so that players can easily identify the coordinates of a square. We will therefore have a display resembling this one (after a few rounds of play):

A function "possibleSquare(board, n, player, i, j)" that returns True if i and j are the coordinates of a square where the player player can place a pawn, and False otherwise.
A function "selectSquare(board, n, player)" that makes the player player enter the coordinates of a square where he can place a pawn. We will assume that there is such a square, we will not test this fact here. As long as these coordinates are not valid with respect to the rules of the game (and the dimensions of the board), we will ask him again to enter them. Finally, the function will return these coordinates.
A procedure "updateBoard(board, player, i, j)" where we assume here that i and j are the coordinates of a square where the player player can place a pawn. This procedure performs this placement.
A function "again(board, n, player)" which returns True if the player player can still place a pawn on the board and False otherwise.
A main program "snort(n)" which will use the previous subroutines (and others if necessary) in order to allow two players to play a complete game on a game board of n squares by n squares.


---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
2 - Dodgem
2.1 - Rules of the game
This game was created in 1972 by Colin Vout.

Two players compete on a two-dimensional square board of n
squares by n
squares.

The first player has white pawns and the second has black pawns.

Initially, the first player has n−1
pawns on the last row excluding the first square of it, and the second player has n−1
pawns on the first column excluding the last square of it.

In turn, each player moves one of his pawns to an empty square orthogonally adjacent.

The first player can only move a pawn up, left or right.

The second player can only move a pawn right, up or down.

If the first player has a pawn on the top row and decides to move it up, this pawn is permanently removed from the board.

If the second player has a pawn on the right column and decides to move it to the right, this pawn is permanently removed from the board.

A player wins the game if he manages to remove all his pawns from the board or if all his pawns are blocked by his opponent's pawns.

2.2 - Implementation of this game in Python
We strongly recommend that you read this entire part before starting to code.

Important notes:

We may eventually implement subroutines in addition to those requested.
The grid will naturally be a two-dimensional list of integers equal to 0, 1 or 2. An empty square will be represented by 0, a pawn of the first player by 1 and a pawn of the second by 2.
Rather than regularly recalculating the dimension of this list, we will prefer to pass it as a parameter of our subroutines.
The example of the visual rendering of the program is only indicative, you can improve it.
Notations of the parameters of the subroutines that we will implement:

"board": two-dimensional list of integers equal to 0, 1 or 2 representing the game board.
"n": strictly positive integer equal to the number of rows and columns of "board".
"player": integer representing the player whose turn it is (for example 1 for the first player and 2 for the second).
"i", "j": any integers.
"directions": a tuple of 4 couples constituting the 4 possible orthogonal directions directions = ((-1, 0), (0, 1), (1, 0), (0, -1)).
"m": integer between 1 and 4 that identifies one of the 4 directions.
Implement the following subprograms:

A function "newBoard(n)" that returns a two-dimensional list representing the initial state of a game board of n squares by n squares.
A procedure "displayBoard(board, n)" that displays the board on the console. An empty square will be represented by a ‘.’, a white pawn by an ‘x’ and a black pawn by an ‘o’. The rows and columns will be numbered (starting at 1) so that players can easily identify the coordinates of a square. The initial configuration of the board of 5 rows and 5 columns will therefore be displayed like this:
A function "possiblePawn(board, n, directions, player, i, j)" which returns True if i and j are the coordinates of a pawn that the player player can move, and False otherwise.
A function "selectPawn(board, n, directions, player)" which makes the player player enter the coordinates of a pawn that can move. We will assume that such a pawn exists, we will not test this fact here. As long as these coordinates are not valid with regard to the rules of the game and the dimensions of the board, we will ask him again to enter them. Finally, the function will return these coordinates.
A function "possibleMove(board, n, directions, player, i, j, m)" where we assume here that i and j are the coordinates of the pawn that the player player wants to move. This function returns True if the player player can move this pawn in direction m and False otherwise.
A function "selectMove(board, n, directions, player, i, j)" where we assume here that i and j are the coordinates of the pawn that the player player wants to move. This function makes the player player enter a direction in which he wants to move this pawn. As long as this direction is not valid with regard to the rules of the game and the dimensions of the board, he will be asked again to enter it. Finally, the function will return this direction.
A procedure "move(board, n, directions, player, i, j, m)" where we assume here that i and j are the coordinates of the pawn that the player player wants to move in direction m. This procedure performs this move.
A function "win(board, n, directions, player)" which returns True if the player player has won the game and False otherwise.
A main program "dodgem(n)" which will use the previous subroutines (and others if necessary) in order to allow two players to play a complete game on a game board of n squares by n squares.

