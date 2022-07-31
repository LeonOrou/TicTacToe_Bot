import random
from game_functions import *
turn_num = 1


def my_bot(board, current_player):
    if board[4] == '-':  # always start in middle as most win chances
        return 4
    elif board.count('-') == 7:  # random if 2nd move
        return random.choice(get_valid_moves(board))
    else:
        for i in range(0, 9):  # check if my bot can win
            if i in get_valid_moves(board):
                board_try = []
                for item in board:
                    board_try.append(item)
                board_try[i] = 'O'
                if has_won(board_try, PLAYER_O):
                    return i
        for i in range(0, 9):  # if I can't win, check if I can prevent opponent from winning
            if i in get_valid_moves(board):
                board_try = []
                for item in board:
                    board_try.append(item)
                board_try[i] = 'X'
                if has_won(board_try, PLAYER_X):
                    return i
        return random.choice(get_valid_moves(board))  # if no one can win this round, random move


def random_bot(board, current_player):
    # get all valid moves in the current board state
    valid_moves = get_valid_moves(board)
    # return a random move
    return random.choice(valid_moves)
