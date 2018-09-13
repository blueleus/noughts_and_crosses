# -*- coding: utf-8 -*-

import random

OPTIONS = ('|X|', '|O|')


BOARD = [
    '| |', '| |', '| |',
    '| |', '| |', '| |',
    '| |', '| |', '| |',
    ]

INDEX_COLUMN = ('0', '1', '2')
INDEX_ROW = ('A', 'B', 'C')


def display_board(board):
    """ Display the current view board."""
    print(' |%s||%s||%s|' % INDEX_COLUMN)
    for row in range(0, 3):
        display = INDEX_ROW[row]
        for clm in range(0, 3):
            display += board[row*3 + clm]
        print(display)


def is_winner(turn):
    return False


def run():
    board = BOARD
    turn = random.choice(OPTIONS)
    winner = False
    while not winner:
        display_board(board)
        coordinates = str(input('it\'s the turn of ' + turn + ': '))
        winner = is_winner(turn)


if __name__ == '__main__':
    run()
