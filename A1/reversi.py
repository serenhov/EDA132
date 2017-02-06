from pip._vendor.distlib.compat import raw_input

- 2 player
- provide a leagal move

EMPTY, BLACK, WHITE, OUTER = '-', 'X', 'O', '?'
PIECES = (EMPTY, BLACK, WHITE, OUTER)
PLAYERS = {BLACK: 'X', WHITE: 'O'}
minVal = 0
maxVal = 0

boardsize = 8
board = []
for row in range(boardsize):
    board.append([])
    for colum in range(boardsize):
        if colum == boardsize/2 and row == boardsize/2 or colum == boardsize/2 -1 and row == boardsize/2 -1 :
            board[row].append('O')
           # board[row-1].append('X')
        elif colum == boardsize/2 -1 and row == boardsize/2 or colum == boardsize/2  and row == boardsize/2 -1 :
            board[row].append('X')
        else:
            board[row].append('-')

def printBoard(board):
    for row in board:
        print(" ".join(row))
printBoard(board)


def minmax(player, board, alpha, beta, depth, evaluate):
    if depth == 0:
        return evaluate(player, board), None

    def value(board, alpha, beta):
        return -minmax(opponent(player), board, -beta, -alpha, depth - 1, evaluate)[0]

    moves = legal_moves(player, board)
    if not moves:
        if not any_legal_move(opponent(player), board):
            return final_value(player, board), None
        return value(board, alpha, beta), None
    best_move = moves[0]
    for move in moves:
        if alpha >= beta:
            break
        val = value(make_move(move, player, list(board)), alpha, beta)
        if val > alpha:
            alpha = val
            best_move = move
        return alpha, best_move

def alphabeta_searcher(depth, evaluate):
    def strategy(player, board):
        return minmax(player, board, minVal, maxVal, depth, evaluate)[1]

    return strategy






def AImove(board )
        return board









