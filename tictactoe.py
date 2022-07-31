from bots import random_bot, my_bot
from game_functions import *
import time


def play_game():
    """
    m12_tictactoe game logic
    :return: (no return value)
    """

    board = init_board()
    print("Game started!")
    print("X: Player X, O: Player O, -: Empty spot")
    print("Enter the number (0-8) of an empty spot to fill it\n")

    print_board(board)
    turn = PLAYER_O
    # turn = random.choice([PLAYER_O, PLAYER_X])

    while not game_over(board):

        if turn == PLAYER_X:
            print(f"Player {turn}:")
            position = random_bot(board, turn)
        else:
            # uncomment line 26 and comment line 27 and 28 to let your bot play against the random bot
            position = my_bot(board, turn)
            # user_in = input(f"Player {turn}, place your piece: ")
            # position = valid_move(user_in, board)

        if position == -1:
            print("Invalid move.")
        else:
            # place piece on board
            time.sleep(1)
            # print board to screen
            print_board(perform_move(turn, position, board))

            # switch turns
            turn = PLAYER_X if turn == PLAYER_O else PLAYER_O
    # determine winner
    winner(board)


if __name__ == '__main__':
    play_game()
