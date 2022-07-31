EMPTY = '-'
PLAYER_X = 'X'
PLAYER_O = 'O'

N_FIELDS = 9


def print_board(board):
    """
    Prints the current board in a readable form to the screen
    :param board: list of length N_FIELDS with all board elements representing the current game state
    :return: (No return value)
    """

    # TODO print the tictactoe board to console
    print(f''' 
    {board[0]} | {board[1]} | {board[2]}
    ----------
    {board[3]} | {board[4]} | {board[5]}
    ----------
    {board[6]} | {board[7]} | {board[8]}
    ''')
    # Hint: You can access the first position of the board by "board[0]"


def perform_move(player, position, board):
    """
    Places the piece for a player on the given position of the board
    :param player: the player which performs the move
    :param position: the position where to place the stone (0-8)
    :param board: list of length N_FIELDS with all board elements representing the current game state
    :return: (no return value)
    """
    board[position] = player
    return board
    # TODO place the piece on the given position of the board
    # Hint: assign "player" to the given position in the board


def board_full(board):
    """
    Checks if there is an empty spot on the board
    :param board: list with all board elements
    :return: True if there is an empty spot otherwise False
    """
    return EMPTY not in board


def has_won(board, player):
    """
    Check if there are three equal pieces for this player in some row, column or one of the two diagonals

    :param board: list of length N_FIELDS with all board elements representing the current game state
    :param player: symbol of player that should be checked
    :return: True if three pieces in a row
    """
    if board[0] == board[1] == board[2] == player or board[3] == board[4] == board[5] == player or board[6] == board[7] == board[8] == player or board[0] == board[3] == board[6] == player or board[1] == board[4] == board[7] == player or board[2] == board[5] == board[8] == player or board[0] == board[4] == board[8] == player or board[2] == board[4] == board[6] == player:
        return True


def game_over(board):
    """
    Checks if the game is over, i.e., no more moves are possible
    :param board: list of length N_FIELDS with all board elements representing the current game state
    :return: True if the game is over (no more empty pieces left or one of the players won the game) otherwise False
    """
    return board_full(board) or has_won(board, PLAYER_X) or has_won(board, PLAYER_O)


def valid_move(user_in, board):
    """
    Checks whether the input of the user is a valid move.
    A move is valid if it is a number between 0 and 8 (inclusive) and if the position on the board is empty.
    :param user_in: string input of the user
    :param board: list of length N_FIELDS with all board elements representing the current game state
    :return: integer between 0-8 indicating a valid position where the piece should be placed otherwise -1
    """
    if user_in.isnumeric():
    # TODO optional check if the input is a valid integer number
    # Hint: Checkout the isnumeric() function https://www.programiz.com/python-programming/methods/string/isnumeric

    # TODO cast the user input to an integer number
        user_in = int(user_in)
    # TODO check if the move is valid
    # Hint: A move is valid if the input is between 0 and 8 and if the position on the board contains the "EMPTY"-symbol
        if 0 <= user_in <= 8 and board[user_in] == EMPTY:
            return user_in
    return -1

    # TODO return the number indicating the valid move or -1 if the move is not valid


def init_board():
    """
    Initializes the game board
    :return: list of length N_FIELDS filled with the EMPTY symbol representing the board
    """
    board = []
    for x in range(N_FIELDS):
        board.append(EMPTY)
    return board


def winner(board):
    """
    Prints the outcome of the game to the console. Either PLAYER_X or PLAYER_O has won or it is a tie.
    :param board: list of length N_FIELDS with all board elements representing the current game state
    :return: (no return value)
    """
    if has_won(board, PLAYER_X):
        print('Player X won!')
    elif has_won(board, PLAYER_O):
        print('Player O won!')
    elif board_full(board):
        print('Tie!')


def get_valid_moves(board):
    """
    Get all valid moves for the current game state
    :param board: list of length N_FIELDS with all board elements representing the current game state
    :return: list off all possible moves, i.e., all position of the board that are filled with EMPTY
    """

    valid_moves = []
    for i in range(N_FIELDS):
        if board[i] == EMPTY:
            valid_moves.append(i)

    return valid_moves

