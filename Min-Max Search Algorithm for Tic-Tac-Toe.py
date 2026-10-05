'''

Welcome to GDB Online.
GDB online is an online compiler and debugger tool for C, C++, Python, Java, PHP, Ruby, Perl,
C#, OCaml, VB, Swift, Pascal, Fortran, Haskell, Objective-C, Assembly, HTML, CSS, JS, SQLite, Prolog.
Code, Compile, Run and Debug online from anywhere in world.

'''
# ============================================================
# CATEGORY 6 - 3
# MIN-MAX SEARCH ALGORITHM FOR TIC-TAC-TOE
# ============================================================


# ------------------------------------------------------------
# Display Board
# ------------------------------------------------------------

def print_board(board):

    print()

    for i in range(3):

        print(
            " " + " | ".join(board[i])
        )

        if i < 2:
            print("---+---+---")

    print()


# ------------------------------------------------------------
# Check Winner
# ------------------------------------------------------------

def check_winner(board):

    # Rows
    for row in board:

        if row[0] == row[1] == row[2] and row[0] != ' ':
            return row[0]

    # Columns
    for col in range(3):

        if (
            board[0][col] ==
            board[1][col] ==
            board[2][col] and
            board[0][col] != ' '
        ):

            return board[0][col]

    # Main diagonal
    if (
        board[0][0] ==
        board[1][1] ==
        board[2][2] and
        board[0][0] != ' '
    ):

        return board[0][0]

    # Other diagonal
    if (
        board[0][2] ==
        board[1][1] ==
        board[2][0] and
        board[0][2] != ' '
    ):

        return board[0][2]

    return None


# ------------------------------------------------------------
# Check Board Full
# ------------------------------------------------------------

def board_full(board):

    for row in board:

        for cell in row:

            if cell == ' ':
                return False

    return True


# ------------------------------------------------------------
# MINIMAX
# ------------------------------------------------------------

def minimax(board, depth, maximizing):

    winner = check_winner(board)

    # AI wins
    if winner == 'O':
        return 10 - depth

    # Human wins
    if winner == 'X':
        return depth - 10

    # Draw
    if board_full(board):
        return 0

    # MAX - AI
    if maximizing:

        best_score = float('-inf')

        for i in range(3):

            for j in range(3):

                if board[i][j] == ' ':

                    board[i][j] = 'O'

                    score = minimax(
                        board,
                        depth + 1,
                        False
                    )

                    board[i][j] = ' '

                    best_score = max(
                        best_score,
                        score
                    )

        return best_score

    # MIN - Human
    else:

        best_score = float('inf')

        for i in range(3):

            for j in range(3):

                if board[i][j] == ' ':

                    board[i][j] = 'X'

                    score = minimax(
                        board,
                        depth + 1,
                        True
                    )

                    board[i][j] = ' '

                    best_score = min(
                        best_score,
                        score
                    )

        return best_score


# ------------------------------------------------------------
# FIND BEST MOVE
# ------------------------------------------------------------

def best_move(board):

    best_score = float('-inf')

    move = None

    for i in range(3):

        for j in range(3):

            if board[i][j] == ' ':

                board[i][j] = 'O'

                score = minimax(
                    board,
                    0,
                    False
                )

                board[i][j] = ' '

                if score > best_score:

                    best_score = score

                    move = (i, j)

    return move


# ------------------------------------------------------------
# MAIN GAME
# ------------------------------------------------------------

board = [
    [' ', ' ', ' '],
    [' ', ' ', ' '],
    [' ', ' ', ' ']
]


print("TIC-TAC-TOE")
print("You = X")
print("AI  = O")

print_board(board)


while True:

    # -------------------------
    # HUMAN MOVE
    # -------------------------

    try:

        row = int(
            input("Enter row (1-3): ")
        ) - 1

        col = int(
            input("Enter column (1-3): ")
        ) - 1

    except ValueError:

        print("Please enter numbers only.")

        continue


    if row < 0 or row > 2 or \
       col < 0 or col > 2:

        print("Invalid position.")

        continue


    if board[row][col] != ' ':

        print("Cell already occupied.")

        continue


    board[row][col] = 'X'

    print_board(board)


    # Check human winner
    winner = check_winner(board)

    if winner == 'X':

        print("You win!")

        break


    if board_full(board):

        print("It's a draw!")

        break


    # -------------------------
    # AI MOVE
    # -------------------------

    print("AI is thinking...")

    move = best_move(board)

    if move:

        board[move[0]][move[1]] = 'O'

    print_board(board)


    # Check AI winner
    winner = check_winner(board)

    if winner == 'O':

        print("AI wins!")

        break


    if board_full(board):

        print("It's a draw!")

        break