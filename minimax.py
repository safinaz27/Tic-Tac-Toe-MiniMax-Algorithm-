import random
import time

currPlayer = 'X'
Board = [['','',''],
         ['','',''],
         ['','','']]

def checkWinner(Board) :
    # winner = None
    # Check Horizontal
    for i in range(3):
        if (Board[i][0] == Board[i][1] and Board[i][1] == Board[i][2] and Board[i][0]!= '' ):
            return Board[i][0]
    # Check Vertical
    for i in range(3):
        if(Board[0][i] == Board[1][i] and  Board[1][i] == Board[2][i] and Board[0][i]!= '' ):
            return Board[0][i]
    # Check Diagonals
    if(Board[0][0] == Board[1][1] and Board[1][1] == Board[2][2] and Board[0][0]!= '' ):
        return Board[0][0]
    if(Board[2][0] == Board[1][1] and Board[1][1] == Board[0][2] and Board[2][0]!= '' ):
        return Board[2][0]
    for row in Board:
            for cell in row:
                if cell == '':
                    return None  # Still playing

    return "Tie"

def AI_Move(Board):
    empty_cells = [(i, j) for i in range(3) for j in range(3) if Board[i][j] == '']
    if empty_cells:
        i, j = random.choice(empty_cells)
        return i , j
# print(checkWinner(Board))
