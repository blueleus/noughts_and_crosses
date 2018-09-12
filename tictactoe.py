# -*- coding: utf-8 -*-

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


def run():
    board = BOARD
    display_board(board)


if __name__ == '__main__':
    run()
