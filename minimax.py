currPlayer = 'X'
Board = [['','',''],
         ['','',''],
         ['','','']]

def checkWinner(board):
    # Check rows
    for row in board:
        if row[0] == row[1] == row[2] != '':
            return row[0]
    
    # Check columns
    for col in range(3):
        if board[0][col] == board[1][col] == board[2][col] != '':
            return board[0][col]
    
    # Check diagonals
    if board[0][0] == board[1][1] == board[2][2] != '':
        return board[0][0]
    if board[0][2] == board[1][1] == board[2][0] != '':
        return board[0][2]
    
    # Check for tie
    if all(all(cell != '' for cell in row) for row in board):
        return "Tie"
    
    return None

def available_moves(board):
    return [(i, j) for i in range(3) for j in range(3) if board[i][j] == '']

# Minimax with Alpha-Beta Pruning
def minimax(board, depth, is_maximizing, alpha, beta):
    result = checkWinner(board)
    if result is not None:
        if result == 'X':
            return -10 + depth
        elif result == 'O':
            return 10 - depth
        else:
            return 0

    if is_maximizing:
        best_score = -float('inf')
        for i, j in available_moves(board):
            board[i][j] = 'O'
            score = minimax(board, depth + 1, False, alpha, beta)
            board[i][j] = ''
            best_score = max(score, best_score)
            alpha = max(alpha, best_score)
            if beta <= alpha:
                break
        return best_score
    else:
        best_score = float('inf')
        for i, j in available_moves(board):
            board[i][j] = 'X'
            score = minimax(board, depth + 1, True, alpha, beta)
            board[i][j] = ''
            best_score = min(score, best_score)
            beta = min(beta, best_score)
            if beta <= alpha:
                break
        return best_score

def AI_Move(board):
    best_score = -float('inf')
    best_move = None
    for i, j in available_moves(board):
        board[i][j] = 'O'
        score = minimax(board, 0, False, -float('inf'), float('inf'))
        board[i][j] = ''
        if score > best_score:
            best_score = score
            best_move = (i, j)
    return best_move