#Write a program to implement the game of Tic-Tac-Toe (Noughts and Crosses) where 
#the computer plays against a human user. Use the Minimax algorithm (or Alpha-Beta 
#Pruning) to enable the computer to play an optimal game.


# Tic-Tac-Toe using Minimax Algorithm

board = [" "] * 9

def display_board():
    print()
    for i in range(0, 9, 3):
        print(" " + " | ".join(board[i:i+3]))
        if i < 6:
            print("---+---+---")
    print()

def check_winner(b):
    winning_positions = [
        (0, 1, 2), (3, 4, 5), (6, 7, 8),
        (0, 3, 6), (1, 4, 7), (2, 5, 8),
        (0, 4, 8), (2, 4, 6)
    ]

    for a, b1, c in winning_positions:
        if b[a] == b[b1] == b[c] != " ":
            return b[a]

    if " " not in b:
        return "Draw"

    return None

def minimax(b, is_maximizing):
    result = check_winner(b)

    if result == "O":
        return 1
    if result == "X":
        return -1
    if result == "Draw":
        return 0

    if is_maximizing:
        best_score = float("-inf")

        for i in range(9):
            if b[i] == " ":
                b[i] = "O"
                score = minimax(b, False)
                b[i] = " "
                best_score = max(best_score, score)

        return best_score

    else:
        best_score = float("inf")

        for i in range(9):
            if b[i] == " ":
                b[i] = "X"
                score = minimax(b, True)
                b[i] = " "
                best_score = min(best_score, score)

        return best_score

def computer_move():
    best_score = float("-inf")
    move = None

    for i in range(9):
        if board[i] == " ":
            board[i] = "O"
            score = minimax(board, False)
            board[i] = " "

            if score > best_score:
                best_score = score
                move = i

    if move is not None:
        board[move] = "O"
        print("Computer chooses position:", move + 1)

def play_game():
    print("TIC-TAC-TOE")
    print("You are X. Computer is O.")
    print("Positions are numbered 1 to 9:")
    print(" 1 | 2 | 3")
    print("---+---+---")
    print(" 4 | 5 | 6")
    print("---+---+---")
    print(" 7 | 8 | 9")

    while True:
        display_board()

        try:
            position = int(input("Enter your position (1-9): ")) - 1
        except ValueError:
            print("Please enter a valid number.")
            continue

        if position < 0 or position > 8 or board[position] != " ":
            print("Invalid position! Try again.")
            continue

        board[position] = "X"

        result = check_winner(board)
        if result:
            display_board()
            break

        computer_move()

        result = check_winner(board)
        if result:
            display_board()
            break

    if result == "X":
        print("Congratulations! You win!")
    elif result == "O":
        print("Computer wins!")
    else:
        print("Game Draw!")

play_game()
