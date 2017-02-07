from pip._vendor.distlib.compat import raw_input

UP, DOWN, LEFT, RIGHT, UP_LEFT, UP_RIGHT, DOWN_LEFT, DOWN_RIGHT = [(-1,0) , (1,0), (0,-1), (0,1), (-1,1) , (-1,1), (1,-1), (1,1)]
DIRECTIONS = (UP, DOWN, LEFT, RIGHT, UP_LEFT, UP_RIGHT, DOWN_LEFT, DOWN_RIGHT)
EMPTY, BLACK, WHITE, OUTER = '-', 'X', 'O', '?'
PIECES = (EMPTY, BLACK, WHITE, OUTER)
PLAYERS = {BLACK: 'X', WHITE: 'O'}
minVal = 0
maxVal = 0

boardSize = 8
board = []


    for row in range(boardSize):
        board.append([])
        for column in range(boardSize):
            if column == boardSize / 2 and row == boardSize / 2 or column == boardSize / 2 - 1 and row == boardSize / 2 - 1:
                board[row].append('O')
                # board[row-1].append('X')
            elif column == boardSize / 2 - 1 and row == boardSize / 2 or column == boardSize / 2 and row == boardSize / 2 - 1:
                board[row].append('X')
            else:
                board[row].append('-')

    def print_board(board):
        for row in board:
            print(" ".join(row))

    print_board(board)

    def find_possible_moves(board, player):
        valid_moves = []
        for j in range(row):
            for i in range(column):
                moves = 0
                if board[i][j] == player:
                    for d in DIRECTIONS:
                        new_row = i + d[0]
                        new_column = j + d[1]
                        if board[new_row][new_column] != player:
                            moves = 1
                            new_row += d[0]
                            new_column += d[1]
                            if board[new_row][new_column] == '-' and moves == 1:
                                valid_moves.append((new_row, new_column))
        return valid_moves

    def make_move(board, player, row, column):
        if (row, column) not in find_possible_moves(board, player):
            return 0
        board[row][column] = player
        flip(board, player, row, column)
        return 1

    def flip(board, player, row, column):
        flips = []
        for d in DIRECTIONS:
            new_row = row + d[0]
            new_column = column + d[1]
            while board[new_row][new_column] != player:
                flips.append(new_row, new_column)
                new_row += d[0]
                new_column += d[1]
                if board[new_row][new_column] == player:
                    for f in flips:
                        board[flips[0]][flips[1]] = player

    def calculate_points(board, player):
        count = 0
        for j in range(row):
            for i in range(column):
                if board[i][j] == player:
                    count += 1
        return count

    def calculate_winner(board):
        white = 0
        black = 0
        for j in range(row):
            for i in range(column):
                if board[i][j] == WHITE:
                    white += 1
                elif [i][j] == BLACK:
                    black += 1
        if black > white:
            return 'black won.'
        elif black == white:
            return 'equal.'
        else:
            return 'white won'



























