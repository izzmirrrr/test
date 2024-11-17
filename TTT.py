# Tic-Tac-Toe Game
def print_board(board):
    """Prints the game board."""
    for row in board:
        print(" | ".join(row))
        print("-" * 9)


def check_winner(board):
    """Checks if there is a winner."""
    # Check rows and columns
    for i in range(3):
        if board[i][0] == board[i][1] == board[i][2] and board[i][0] != " ":
            return True
        if board[0][i] == board[1][i] == board[2][i] and board[0][i] != " ":
            return True

    # Check diagonals
    if board[0][0] == board[1][1] == board[2][2] and board[0][0] != " ":
        return True
    if board[0][2] == board[1][1] == board[2][0] and board[0][2] != " ":
        return True

    return False


def is_draw(board):
    """Checks if the game is a draw."""
    for row in board:
        if " " in row:
            return False
    return True


# Initialize the board
board = [[" " for _ in range(3)] for _ in range(3)]

# Game loop
current_player = "X"
while True:
    print_board(board)
    print(f"Player {current_player}, it's your turn!")

    # Get player input
    try:
        row = int(input("Enter the row (0-2): "))
        col = int(input("Enter the column (0-2): "))

        if board[row][col] != " ":
            print("That spot is already taken. Try again!")
            continue
    except (ValueError, IndexError):
        print("Invalid input! Please enter numbers between 0 and 2.")
        continue

    # Place the player's mark
    board[row][col] = current_player

    # Check for a winner or draw
    if check_winner(board):
        print_board(board)
        print(f"Player {current_player} wins!")
        break
    elif is_draw(board):
        print_board(board)
        print("It's a draw!")
        break

    # Switch players
    current_player = "O" if current_player == "X" else "X"
