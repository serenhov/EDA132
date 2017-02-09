import random
import time
from copy import deepcopy


UP, DOWN, LEFT, RIGHT, UP_LEFT, UP_RIGHT, DOWN_LEFT, DOWN_RIGHT = [(-1, 0), (1, 0), (0, -1), (0, 1), (-1, -1), (-1, 1), (1, -1), (1, 1)]
DIRECTIONS = (UP, DOWN, LEFT, RIGHT, UP_LEFT, UP_RIGHT, DOWN_LEFT, DOWN_RIGHT)
BLACK, WHITE = 1, -1
PLAYERS = (BLACK, WHITE)
depth = 20


# Prints the game board
def print_board(board):
    print("   1  2  3  4  5  6  7  8")
    i = 1
    for row in board:
        print(i, row)
        i += 1


# Checks if the coordinates are on the board
def on_board(i):
    return 0 <= i < 8


# Finds all possible moves for the current player
def find_possible_moves(board, player):
    valid_moves = []
    for j in range(8):
        for i in range(8):
            if board[i][j] == player:
                for d in DIRECTIONS:
                    new_row = i + d[0]
                    new_column = j + d[1]
                    while on_board(new_row) and on_board(new_column):
                        if board[new_row][new_column] == -player:
                            new_row += d[0]
                            new_column += d[1]
                            if on_board(new_row) and on_board(new_column) and board[new_row][new_column] == 0:
                                if (new_row, new_column) not in valid_moves:
                                    valid_moves.append((new_row, new_column))
                                break
                        else:
                            break
    return valid_moves


# Makes the actual move and call the flip method
def make_move(board, player, row, column):
    #if(row, column) not in find_possible_moves(board, player):
    #    return 0
    board[row][column] = player
    flip(board, player, row, column)
    return 1


# Flips the bricks in a certain move
def flip(board, player, row, column):
    flips = []
    for d in DIRECTIONS:
        new_row = row + d[0]
        new_column = column + d[1]
        flips.clear()
        while on_board(new_row) and on_board(new_column) and board[new_row][new_column] == -player:
            flips.append((new_row, new_column))
            new_row += d[0]
            new_column += d[1]
            if on_board(new_row) and on_board(new_column) and board[new_row][new_column] == player:
                i = 0
                for f in flips:
                    a = flips[i][0]
                    b = flips[i][1]
                    board[a][b] = player
                    i += 1


# Calculate points for current player
def calculate_points(board, player):
    count = 0
    for j in range(8):
        for i in range(8):
            if board[i][j] == player:
                count += 1
    return count


# Calculates the winner of the game
def calculate_winner(board):
    white = 0
    black = 0
    for j in range(8):
        for i in range(8):
            if board[i][j] == WHITE:
                white += 1
            elif board[i][j] == BLACK:
                black += 1
    if black > white:
        return 'BLACK!'
    elif black == white:
        return 'DRAW'
    else:
        return 'WHITE!'


# THE ALGORITHM!
# Returns the best move for the AI
def alpha_beta(alpha, beta, board, player, depth, time_limit):
    start_time = time.time()
    best_alpha = find_possible_moves(board, player)[0]
    while (time.time() - start_time) >= time_limit:
        for move in find_possible_moves(board, player):
            v = mini_max(alpha, beta, board, player, depth)
            if v > alpha:
                alpha = v
                best_alpha = move
    return best_alpha


# THE ALGORITHM!
# Our AI engine returns the best score
def mini_max(alpha, beta, board, player, depth):
    if depth == 0 or not find_possible_moves(board, player):
        return calculate_points(board, player)
    if player == 1:
        for move in find_possible_moves(board, player):
            print("player 1 ", move)
            board_with_move = deepcopy(board)
            make_move(board_with_move, player, move[0], move[1])
            alpha = max(alpha, mini_max(alpha, beta, board_with_move, -player, depth-1))
            if alpha >= beta:
                break
            return alpha
    elif player == -1:
        for move in find_possible_moves(board, player):
            print("player -1 ", move)
            #d += 1
            #i += 1
            board_with_move = deepcopy(board)
            make_move(board_with_move, player, move[0], move[1])
            beta = min(beta, mini_max(alpha, beta, board_with_move, -player, depth-1))
            if int(alpha) >= int(beta):
                break
            return beta


# If you want to play against a random
def random_strategy(player, board):
    return random.choice(find_possible_moves(player, board))


# Starts the game
def game_on(board, player):
    while find_possible_moves(board, player):
        if player == 1:
            print("These are your alternatives")
            print_moves = find_possible_moves(board, 1)
            i = 0
            for p in print_moves:
                print(i, "  :", p[0]+1, p[1]+1)
                i += 1
            players_move = int(input("Make a move:  "))
            make_move(board, 1, print_moves[players_move][0], print_moves[players_move][1])
            print_board(board)
            game_on(board, -player)
        else:
            if player == -1:
                #ai_move = random_strategy(board, -1)
                ai_move = alpha_beta(-64, 64, board, -1, depth, limit)
                print("AI-move: (", ai_move[0]+1, ",", ai_move[1]+1, ")")
                make_move(board, -1, ai_move[0], ai_move[1])
                print_board(board)
                game_on(board, -player)
        break


# Creates and prints the game board
w, h = 8, 8;
board = [[0 for x in range(w)] for y in range(h)]
board[3][3] = BLACK
board[4][4] = BLACK
board[4][3] = WHITE
board[3][4] = WHITE
print_board(board)

print("  ")
print("Hello, lets play Reversi!")
limit = int(input("What timelimit should you competitor have? (in seconds)  "))
print("Great! Timelimit is set to", limit, "seconds. You are player 1, good luck!")
game_on(board, 1)

print(" THE WINNER IS: ", calculate_winner(board), "Score - Black: ", calculate_points(board, 1), ", White: ", calculate_points(board, -1))






