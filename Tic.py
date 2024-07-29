def print_board(board):
    for row in board:
        print("|".join(row))
        print("-" * 5)

def check_winner(board, player):
    # Check rows
    for row in board:
        if all(cell == player for cell in row):
            return True
    # Check columns
    for col in range(3):
        if all(board[row][col] == player for row in range(3)):
            return True
    # Check diagonals
    if all(board[i][i] == player for i in range(3)) or all(board[i][2-i] == player for i in range(3)):
        return True
    return False

def is_board_full(board):
    for row in board:
        for cell in row:
            if cell == " ":
                return False
    return True

def main():
    board = [[" " for _ in range(3)] for _ in range(3)]
    players = ["X", "O"]
    turn = 0
    print("Welcome to Tic-Tac-Toe")
    print_board(board)
    while True:
        player = players[turn % 2]
        print(f"Player {player}'s turn")
        row = int(input("Enter row (0, 1, or 2): "))
        col = int(input("Enter column (0, 1, or 2): "))

        if board[row][col] == " ":
            board[row][col] = player
            print_board(board)
            if check_winner(board, player):
                print(f"Player {player} wins!")
                break
            elif is_board_full(board):
                print("It's a draw!")
                break
            turn += 1
        else:
            print("That cell is already occupied. Try again.")

if __name__ == "__main__":
    main()
