'''

Welcome to GDB Online.
GDB online is an online compiler and debugger tool for C, C++, Python, Java, PHP, Ruby, Perl,
C#, OCaml, VB, Swift, Pascal, Fortran, Haskell, Objective-C, Assembly, HTML, CSS, JS, SQLite, Prolog.
Code, Compile, Run and Debug online from anywhere in world.

'''
# ============================================================
# CATEGORY 6 - 2
# ALPHA-BETA PRUNING FOR CHESS GAME
# ============================================================

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
# Evaluation Function
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

            # WHITE
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

            # BLACK
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
# Make Move
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
# ALPHA-BETA SEARCH
# ------------------------------------------------------------

def alpha_beta(board, depth, alpha, beta, maximizing_player):

    # Terminal condition
    if depth == 0:

        return evaluate(board)

    # MAX
    if maximizing_player:

        max_eval = float('-inf')

        moves = generate_moves(board, 'W')

        for move in moves:

            new_board = make_move(board, move)

            evaluation = alpha_beta(
                new_board,
                depth - 1,
                alpha,
                beta,
                False
            )

            max_eval = max(max_eval, evaluation)

            alpha = max(alpha, evaluation)

            # PRUNING
            if beta <= alpha:

                print("Branch pruned at MAX")

                break

        return max_eval

    # MIN
    else:

        min_eval = float('inf')

        moves = generate_moves(board, 'B')

        for move in moves:

            new_board = make_move(board, move)

            evaluation = alpha_beta(
                new_board,
                depth - 1,
                alpha,
                beta,
                True
            )

            min_eval = min(min_eval, evaluation)

            beta = min(beta, evaluation)

            # PRUNING
            if beta <= alpha:

                print("Branch pruned at MIN")

                break

        return min_eval


# ------------------------------------------------------------
# FIND BEST MOVE
# ------------------------------------------------------------

def find_best_move(board, depth):

    best_score = float('-inf')
    best_move = None

    alpha = float('-inf')
    beta = float('inf')

    moves = generate_moves(board, 'W')

    for move in moves:

        new_board = make_move(board, move)

        score = alpha_beta(
            new_board,
            depth - 1,
            alpha,
            beta,
            False
        )

        if score > best_score:

            best_score = score
            best_move = move

        alpha = max(alpha, score)

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

print("Initial Chess Board:")

print_board(board)

print("\nInitial Evaluation:", evaluate(board))

depth = 3

best_move, score = find_best_move(
    board,
    depth
)

print("\nBest Move:", best_move)

print("Alpha-Beta Score:", score)

if best_move:

    board = make_move(
        board,
        best_move
    )

    print("\nBoard After AI Move:")

    print_board(board)