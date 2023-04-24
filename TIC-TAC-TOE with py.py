def print_board(board):
    for i in range(3):
        for j in range(3):
            print(board[3 * i + j], end=" ")
        print()


def is_winning_move(board, player):
    # Check rows
    for i in range(3):
        if (board[3 * i] == player and board[3 * i + 1] == player and board[3 * i + 2] == player):
            return True

    # Check columns
    for i in range(3):
        if (board[i] == player and board[i + 3] == player and board[i + 6] == player):
            return True

    # Check diagonals
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
        # Player 1's turn
        print_board(board)
        move = int(input("Player 1, enter your move (1-9): "))
        board[move - 1] = "X"

        if is_winning_move(board, "X"):
            print_board(board)
            print("Player 1 wins!")
            break

        if is_tie(board):
            print_board(board)
            print("It's a tie!")
            break

        # Player 2's turn
        print_board(board)
        move = int(input("Player 2, enter your move (1-9): "))
        board[move - 1] = "O"

        if is_winning_move(board, "O"):
            print_board(board)
            print("Player 2 wins!")
            break

        if is_tie(board):
            print_board(board)
            print("It's a tie!")
            break


play_game()