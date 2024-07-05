def print_board(board):
    print(f"{board[0]} | {board[1]} | {board[2]}")
    print("--+---+--")
    print(f"{board[3]} | {board[4]} | {board[5]}")
    print("--+---+--")
    print(f"{board[6]} | {board[7]} | {board[8]}")

def check_win(board):
    # Check rows
    for i in range(0, 9, 3):
        if board[i] == board[i+1] == board[i+2] != ' ':
            return board[i]

    # Check columns
    for i in range(3):
        if board[i] == board[i+3] == board[i+6] != ' ':
            return board[i]

    # Check diagonals
    if board[0] == board[4] == board[8] != ' ':
        return board[0]
    if board[2] == board[4] == board[6] != ' ':
        return board[2]

    # Check for tie
    if ' ' not in board:
        return 'Tie'

    return None

if __name__ == "__main__":
    board = [' '] * 9
    players = ['X', 'O']
    turn = 0  # Index of the current player in players list

    print("Welcome to Tic Tac Toe!")
    print_board(range(1, 10))  # Initial board positions

    while True:
        print(f"Player {players[turn]}'s turn")
        position = int(input("Enter position (1-9): ")) - 1

        if board[position] == ' ':
            board[position] = players[turn]
        else:
            print("That position is already taken! Try again.")
            continue

        print_board(board)
        winner = check_win(board)
        if winner:
            if winner == 'Tie':
                print("It's a tie!")
            else:
                print(f"Player {winner} wins!")
            break

        turn = (turn + 1) % 2