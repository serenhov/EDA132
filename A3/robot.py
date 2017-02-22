import random
import numpy as np

UP, DOWN, LEFT, RIGHT = [(-1, 0), (1, 0), (0, -1), (0, 1)]
DIRECTIONS = (UP, DOWN, LEFT, RIGHT)
WALL, NO_WALL, CORNER = (1, 0, -1)
STATE = (WALL, NO_WALL, CORNER)


def print_board(board):

    print("   1  2  3  4  5")
    i = 1
    for row in board:
        print(i, row)
        i += 1


def start_pos(board):
    x = random.randint(0, 4)
    y = random.randint(0, 4)
    print(x, y)
    board[x][y] = 1
    print_board(board)



def current_pos(board):
    for j in range(5):
        for i in range(5):
            if board[i][j] == 1:
                current = i, j
    return current


def on_board(i):
    return 0 <= i < 5

def find_possible_moves(board, current):
    valid_moves = []
    for d in DIRECTIONS:
        new_row = current[0] + d[0]
        new_column = current[1] + d[1]
        if on_board(new_row) and on_board(new_column):
            valid_moves.append((new_row, new_column))
    return len(valid_moves)


def robot_walk(board, current_pos):
    current = current_pos(board)
    state = find_possible_moves(board, current)
    if state == 2:
        state = WALL
    elif state == 3:



w, h = 5, 5;
board = [[0 for x in range(w)] for y in range(h)]
print_board(board)

current_pos = start_pos(board)
