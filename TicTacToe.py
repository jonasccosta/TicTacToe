# TicTacToe Game in Python
# Made with https://www.youtube.com/watch?v=BHh654_7Cmw

# Game board
board = ["-", "-", "-",
         "-", "-", "-",
         "-", "-", "-"]

# If game is still going
game_still_going = True

# Current player
current_player = "X"

# Winner
winner = None


def display_board():
    print(board[0] + " | " + board[1] + " | " + board[2])
    print(board[3] + " | " + board[4] + " | " + board[5])
    print(board[6] + " | " + board[7] + " | " + board[8])


def play_game():
    # Display initial board
    display_board()

    while game_still_going:
        handle_turn(current_player)

        check_if_game_over()

        flip_player()

    # The game has ended
    if winner == "X" or winner == "O":
        print("Player " + winner + " won")

    elif winner is None:
        print("Tie")


def handle_turn(player):
    print("Player " + player + "'s turn")
    position = input("Choose a position from 1-9: ")

    valid = False
    while not valid:
        while position not in ["1", "2", "3", "4", "5", "6", "7", "8", "9"]:
            position = input("Invalid input. Choose a position from 1-9: ")

        position = int(position) - 1

        if board[position] == "-":
            valid = True

        else:
            print("You can't go there. Go again")

    board[position] = player
    display_board()


def check_if_game_over():
    check_if_win()
    check_if_tie()


def check_if_win():

    # Set global variables
    global winner

    # Check rows
    row_winner = check_rows()

    # Check columns
    column_winner = check_columns()

    # Check diagonals
    diagonal_winner = check_diagonals()

    if row_winner:
        winner = row_winner
    elif column_winner:
        winner = column_winner
    elif diagonal_winner:
        winner = diagonal_winner
    else:
        winner = None

    return


def check_rows():
    # Set up global variables
    global game_still_going

    # Check if any of the rows have all the same non-empty values
    row_1 = board[0] == board[1] == board[2] != "-"
    row_2 = board[3] == board[4] == board[5] != "-"
    row_3 = board[6] == board[7] == board[8] != "-"

    if row_1 or row_2 or row_3:
        game_still_going = False

    # Return winner
    if row_1:
        return board[0]

    elif row_2:
        return board[3]

    elif row_1:
        return board[6]

    return


def check_columns():
    # Set up global variables
    global game_still_going

    # Check if any of the rows have all the same non-empty values
    column_1 = board[0] == board[3] == board[6] != "-"
    column_2 = board[1] == board[4] == board[7] != "-"
    column_3 = board[2] == board[5] == board[8] != "-"

    if column_1 or column_2 or column_3:
        game_still_going = False

    # Return winner
    if column_1:
        return board[0]

    elif column_2:
        return board[1]

    elif column_3:
        return board[2]

    return


def check_diagonals():
    # Set up global variables
    global game_still_going

    # Check if any of the rows have all the same non-empty values
    diagonal_1 = board[0] == board[4] == board[8] != "-"
    diagonal_2 = board[2] == board[4] == board[6] != "-"

    if diagonal_1 or diagonal_2:
        game_still_going = False

    # Return winner
    if diagonal_1:
        return board[0]

    elif diagonal_2:
        return board[2]

    return


def check_if_tie():
    global game_still_going
    if "-" not in board:
        game_still_going = False
    return


def flip_player():
    global current_player

    if current_player == "X":
        current_player = "O"

    elif current_player == "O":
        current_player = "X"

play_game()
