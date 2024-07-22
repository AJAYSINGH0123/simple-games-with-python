# A two player tic tac toe game
def print_board(board):
    for row in board:
        print(" | ".join(row))
        print("-" * 5)

def check_winner(board, player):
    for row in board:
        if all(s == player for s in row):
            return True
    for col in range(3):
        if all(row[col] == player for row in board):
            return True
    if all(board[i][i] == player for i in range(3)) or all(board[i][2 - i] == player for i in range(3)):
        return True
    return False

def tic_tac_toe():
    board = [[" " for _ in range(3)] for _ in range(3)]
    players = ["X", "O"]
    current_player = 0

    for turn in range(9):
        print_board(board)
        row = int(input(f"Player {players[current_player]}, enter the row (0, 1, or 2): "))
        col = int(input(f"Player {players[current_player]}, enter the column (0, 1, or 2): "))

        if board[row][col] != " ":
            print("Cell already taken. Try again.")
            continue

        board[row][col] = players[current_player]
        if check_winner(board, players[current_player]):
            print_board(board)
            print(f"Player {players[current_player]} wins!")
            return
        current_player = 1 - current_player

    print_board(board)
    print("It's a tie!")

tic_tac_toe()
