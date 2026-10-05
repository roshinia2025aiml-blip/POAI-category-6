'''

Welcome to GDB Online.
GDB online is an online compiler and debugger tool for C, C++, Python, Java, PHP, Ruby, Perl,
C#, OCaml, VB, Swift, Pascal, Fortran, Haskell, Objective-C, Assembly, HTML, CSS, JS, SQLite, Prolog.
Code, Compile, Run and Debug online from anywhere in world.

'''
# ============================================================
# CATEGORY 6 - 1
# MIN-MAX SEARCH ALGORITHM FOR CHESS GAME
# ============================================================

# Piece values
PIECE_VALUES = {
    'K': 1000,
    'Q': 9,
    'k': -1000,
    'q': -9
}


# ------------------------------------------------------------
# Display Board
# ------------------------------------------------------------

def print_board(board):

    print("\n  0 1 2 3 4 5 6 7")

    for i in range(8):
        print(i, end=" ")

        for j in range(8):
            print(board[i][j], end=" ")

        print()


# ------------------------------------------------------------
# Evaluate Board
# ------------------------------------------------------------

def evaluate(board):

    score = 0

    for row in board:
        for piece in row:

            if piece in PIECE_VALUES:
                score += PIECE_VALUES[piece]

    return score


# ------------------------------------------------------------
# Generate Moves
# ------------------------------------------------------------

def generate_moves(board, player):

    moves = []

    for r in range(8):
        for c in range(8):

            piece = board[r][c]

            # White pieces
            if player == 'W' and piece.isupper():

                for nr in range(8):
                    for nc in range(8):

                        if (nr, nc) == (r, c):
                            continue

                        # Queen
                        if piece == 'Q':

                            if (
                                nr == r or
                                nc == c or
                                abs(nr-r) == abs(nc-c)
                            ):

                                if board[nr][nc] == '.' or \
                                   board[nr][nc].islower():

                                    moves.append(
                                        ((r, c), (nr, nc))
                                    )

                        # King
                        elif piece == 'K':

                            if abs(nr-r) <= 1 and \
                               abs(nc-c) <= 1:

                                if board[nr][nc] == '.' or \
                                   board[nr][nc].islower():

                                    moves.append(
                                        ((r, c), (nr, nc))
                                    )

            # Black pieces
            elif player == 'B' and piece.islower():

                for nr in range(8):
                    for nc in range(8):

                        if (nr, nc) == (r, c):
                            continue

                        # Queen
                        if piece == 'q':

                            if (
                                nr == r or
                                nc == c or
                                abs(nr-r) == abs(nc-c)
                            ):

                                if board[nr][nc] == '.' or \
                                   board[nr][nc].isupper():

                                    moves.append(
                                        ((r, c), (nr, nc))
                                    )

                        # King
                        elif piece == 'k':

                            if abs(nr-r) <= 1 and \
                               abs(nc-c) <= 1:

                                if board[nr][nc] == '.' or \
                                   board[nr][nc].isupper():

                                    moves.append(
                                        ((r, c), (nr, nc))
                                    )

    return moves


# ------------------------------------------------------------
# Apply Move
# ------------------------------------------------------------

def make_move(board, move):

    new_board = [row[:] for row in board]

    start, end = move

    sr, sc = start
    er, ec = end

    new_board[er][ec] = new_board[sr][sc]
    new_board[sr][sc] = '.'

    return new_board


# ------------------------------------------------------------
# MINIMAX
# ------------------------------------------------------------

def minimax(board, depth, maximizing_player):

    if depth == 0:

        return evaluate(board)

    if maximizing_player:

        best_score = float('-inf')

        moves = generate_moves(board, 'W')

        for move in moves:

            new_board = make_move(board, move)

            score = minimax(
                new_board,
                depth - 1,
                False
            )

            best_score = max(best_score, score)

        return best_score

    else:

        best_score = float('inf')

        moves = generate_moves(board, 'B')

        for move in moves:

            new_board = make_move(board, move)

            score = minimax(
                new_board,
                depth - 1,
                True
            )

            best_score = min(best_score, score)

        return best_score


# ------------------------------------------------------------
# FIND BEST MOVE
# ------------------------------------------------------------

def find_best_move(board, depth):

    best_score = float('-inf')
    best_move = None

    moves = generate_moves(board, 'W')

    for move in moves:

        new_board = make_move(board, move)

        score = minimax(
            new_board,
            depth - 1,
            False
        )

        if score > best_score:

            best_score = score
            best_move = move

    return best_move, best_score


# ------------------------------------------------------------
# MAIN
# ------------------------------------------------------------

board = [

    ['.', '.', '.', '.', '.', '.', '.', 'k'],
    ['.', '.', '.', '.', '.', '.', '.', '.'],
    ['.', '.', '.', '.', '.', '.', '.', '.'],
    ['.', '.', '.', 'Q', '.', '.', '.', '.'],
    ['.', '.', '.', '.', '.', '.', '.', '.'],
    ['.', '.', '.', '.', '.', '.', '.', '.'],
    ['.', '.', '.', '.', '.', '.', '.', '.'],
    ['K', '.', '.', '.', '.', '.', '.', '.']
]

print("Initial Chess Position:")
print_board(board)

print("\nInitial Evaluation:", evaluate(board))

depth = 2

best_move, score = find_best_move(board, depth)

print("\nBest Move:", best_move)
print("Minimax Score:", score)

if best_move:
    board = make_move(board, best_move)

    print("\nBoard After AI Move:")
    print_board(board)