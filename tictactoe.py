# -*- coding: utf-8 -*-

import random

OPTIONS = ('|X|', '|O|')

BOARD = [
    '| |', '| |', '| |',
    '| |', '| |', '| |',
    '| |', '| |', '| |',
    ]

INDICATORS = ('0', '1', '2')

board = []


def display_board():
    """ Display the current view board."""
    print(' |%s||%s||%s|' % INDICATORS)
    for row in range(0, 3):
        display = INDICATORS[row]
        for clm in range(0, 3):
            display += board[row*3 + clm]
        print(display)


def make_a_move(turn, coordinate_x, coordinate_y):
    """Paints the movement on the board."""
    global board
    idx = coordinate_x*3 + coordinate_y
    if board[idx] == '| |':
        board[idx] = turn


def is_winner(current_turn):
    """Determines if there is a winner or not."""
    global board
    result = False
    for x in range(0, 3):
        if current_turn == board[3*x] and board[3*x] == board[3*x + 1] and board[3*x] == board[3*x + 2]:
            result = True
        if current_turn == board[x] and board[x] == board[3 + x] and board[x] == board[6 + x]:
            result = True
    if current_turn == board[0] and board[0] == board[4] and board[0] == board[8]:
        result = True
    if current_turn == board[2] and board[2] == board[4] and board[2] == board[6]:
        result = True
    return result


def is_it_the_turn_of(current_turn):
    """Indicates whose turn it is."""
    if current_turn is None:
        turn = random.choice(OPTIONS)
    else:
        a = {current_turn}
        b = set(OPTIONS)
        sub_cnj = a.symmetric_difference(b)
        turn = list(sub_cnj)[0]
    return turn


def run():
    global board
    board = BOARD
    winner = False
    turn = None
    while not winner:
        turn = is_it_the_turn_of(current_turn=turn)
        display_board()
        print('it\'s the turn of ' + turn)
        try:
            x = int(input('x: '))
            y = int(input('y: '))
        except ValueError:
            print('Oops! invalid values for x and y.')
            exit(0)
        make_a_move(turn=turn, coordinate_x=x, coordinate_y=y)
        winner = is_winner(current_turn=turn)
    display_board()


if __name__ == '__main__':
    run()
