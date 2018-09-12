# -*- coding: utf-8 -*-

OPTIONS = ('|X|', '|O|')


BOARD = [
    '| |', '| |', '| |',
    '| |', '| |', '| |',
    '| |', '| |', '| |',
    ]


def display_board(board):
    """ Display the current view board."""
    for row in range(0, 3):
        display = ''
        for clm in range(0, 3):
            display += board[row*3 + clm]
        print(display)


def run():
    board = BOARD
    display_board(board)


if __name__ == '__main__':
    run()
