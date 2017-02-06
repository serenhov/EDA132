from pip._vendor.distlib.compat import raw_input


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












