import random


def random_strategy(player, board):
    return random.choise(find_possible_moves(player, board))
