# Snort & Dodgem: Python Game Implementations  

## Table of Contents  
1. [Snort](#1-snort)  
   - [Rules of the Game](#11-rules-of-the-game)  
   - [Implementation in Python](#12-implementation-in-python)  
2. [Dodgem](#2-dodgem)  
   - [Rules of the Game](#21-rules-of-the-game)  
   - [Implementation in Python](#22-implementation-in-python)  

---

## 1. Snort  

### 1.1 Rules of the Game  
- **Origin**: Snort was created in 1970 by Simon Norton.  
- **Players**: Two players compete on a 2D square board of size `n x n`.  
  - Player 1 has white pawns (`x`), and Player 2 has black pawns (`o`).  

#### Gameplay  
1. Players alternate turns.  
2. On each turn, a player places a pawn on an **empty square** that is **not orthogonally adjacent** to a square containing an opponent's pawn.  
3. The game ends when no player can make a move.  
4. The **winner** is the last player to place a pawn. A player **loses** if they cannot make a move.  

---

### 1.2 Implementation in Python  

#### Key Notes  
- The board is a 2D list of integers (`0`, `1`, `2`):  
  - `0`: Empty square.  
  - `1`: Pawn of Player 1.  
  - `2`: Pawn of Player 2.  
- The dimensions of the board (`n`) are passed as parameters to subroutines.  

#### Subroutines  
1. **`newBoard(n)`**:  
   - Returns a 2D list representing an empty board of size `n x n`.  

2. **`displayBoard(board, n)`**:  
   - Displays the board in the console.  
   - Empty squares are represented as `.`.  
   - Player 1's pawns (`x`) and Player 2's pawns (`o`) are displayed.  
   - Rows and columns are numbered (starting from 1).  

3. **`possibleSquare(board, n, player, i, j)`**:  
   - Returns `True` if Player `player` can place a pawn at coordinates `(i, j)`; otherwise, returns `False`.  

4. **`selectSquare(board, n, player)`**:  
   - Prompts Player `player` to input valid coordinates for placing a pawn.  
   - Repeats the prompt until valid coordinates are provided.  
   - Returns the chosen coordinates.  

5. **`updateBoard(board, player, i, j)`**:  
   - Places a pawn for Player `player` at `(i, j)`.  

6. **`again(board, n, player)`**:  
   - Returns `True` if Player `player` can still make a move; otherwise, returns `False`.  

7. **Main Program: `snort(n)`**:  
   - Combines the above subroutines to play a full game of Snort.  

---

## 2. Dodgem  

### 2.1 Rules of the Game  
- **Origin**: Dodgem was created in 1972 by Colin Vout.  
- **Players**: Two players compete on a 2D square board of size `n x n`.  
  - Player 1 has white pawns (`x`), and Player 2 has black pawns (`o`).  

#### Gameplay  
1. **Starting Positions**:  
   - Player 1's pawns occupy the **last row** (excluding the first square).  
   - Player 2's pawns occupy the **first column** (excluding the last square).  

2. **Movements**:  
   - Player 1 can move pawns **up**, **left**, or **right**.  
   - Player 2 can move pawns **up**, **down**, or **right**.  

3. **Pawn Removal**:  
   - If Player 1 moves a pawn **up** from the top row, the pawn is permanently removed.  
   - If Player 2 moves a pawn **right** from the right column, the pawn is permanently removed.  

4. **Victory Condition**:  
   - A player wins if they remove all their pawns from the board or block all opposing pawns.  

---

### 2.2 Implementation in Python  

#### Key Notes  
- The board is a 2D list of integers (`0`, `1`, `2`):  
  - `0`: Empty square.  
  - `1`: Pawn of Player 1.  
  - `2`: Pawn of Player 2.  
- Four possible directions are defined:  
  - `(-1, 0)`: Up.  
  - `(0, 1)`: Right.  
  - `(1, 0)`: Down.  
  - `(0, -1)`: Left.  

#### Subroutines  
1. **`newBoard(n)`**:  
   - Returns a 2D list representing the initial game board.  

2. **`displayBoard(board, n)`**:  
   - Displays the board in the console.  
   - Empty squares are represented as `.`.  
   - Player 1's pawns (`x`) and Player 2's pawns (`o`) are displayed.  

3. **`possiblePawn(board, n, directions, player, i, j)`**:  
   - Returns `True` if Player `player` can move the pawn at `(i, j)`; otherwise, returns `False`.  

4. **`selectPawn(board, n, directions, player)`**:  
   - Prompts Player `player` to input valid coordinates for a pawn to move.  
   - Repeats the prompt until valid coordinates are provided.  
   - Returns the chosen coordinates.  

5. **`possibleMove(board, n, directions, player, i, j, m)`**:  
   - Returns `True` if Player `player` can move the pawn at `(i, j)` in direction `m`.  

6. **`selectMove(board, n, directions, player, i, j)`**:  
   - Prompts Player `player` to input a valid direction for the pawn at `(i, j)`.  
   - Repeats the prompt until a valid direction is provided.  
   - Returns the chosen direction.  

7. **`move(board, n, directions, player, i, j, m)`**:  
   - Moves the pawn at `(i, j)` in direction `m`.  

8. **`win(board, n, directions, player)`**:  
   - Returns `True` if Player `player` has won the game.  

9. **Main Program: `dodgem(n)`**:  
   - Combines the above subroutines to play a full game of Dodgem.  

---

## How to Run  

1. Clone the repository:  
   ```bash
   git clone <repository_url>
