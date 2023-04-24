def print_board(board):
    for i in range(3):
        for j in range(3):
            print(board[3 * i + j], end=" ")
        print()


def is_winning_move(board, player):

    # Check rows
    # ---

    for i in range(3):
        if (board[3 * i] == player and board[3 * i + 1] == player and board[3 * i + 2] == player):
            return True

    # Check columns
    # |||

    for i in range(3):
        if (board[i] == player and board[i + 3] == player and board[i + 6] == player):
            return True

    # Check diagonals
    #   / and \
    #  /       \
    # /         \ give and take

    if (board[0] == player and board[4] == player and board[8] == player):
        return True
    elif (board[2] == player and board[4] == player and board[6] == player):
        return True

    return False


def is_tie(board):
    for i in range(9):
        if board[i] == " ":
            return False
    return True


def play_game():
    board = [" "] * 9

    while True:
        # Player 1 turn
        print_board(board)
        move = int(input("First Person enter your move (1-9): "))
        board[move - 1] = "T"

        if is_winning_move(board, "T"):
            print_board(board)
            print("\'First Person\' wins! -wooo Tiham is the best. Eat shit second person ")
            break

        if is_tie(board):
            print_board(board)
            print("It's a tie!")
            break

        # Player 2 turn
        print_board(board)
        move = int(input("Second Person enter your move (1-9): "))
        board[move - 1] = "L"

        if is_winning_move(board, "L"):
            print_board(board)
            print("\'Second\' Person wins!")
            break

        if is_tie(board):
            print_board(board)
            print("It's a tie!")
            break


play_game()
