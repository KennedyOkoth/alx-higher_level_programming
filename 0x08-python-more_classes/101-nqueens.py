#!/usr/bin/python3

import sys


def init_board(n):
    """Initialize an `n`x`n` sized chessboard with 0's."""
    board = []
    [board.append([]) for i in range(n)]
    [row.append(" ") for i in range(n) for row in board]
    return board


def board_deepcopy(board):
    """Return a deepcopy of a chessboard."""
    if isinstance(board, list):
        return list(map(board_deepcopy, board))
    return board


def get_solution(board):
    """Return the list of lists representation of a solved chessboard."""
    solution = []
    for r in range(len(board)):
        for c in range(len(board)):
            if board[r][c] == "Q":
                solution.append([r, c])
                break
    return solution


def xout(board, row, col):
    """X out spots on a chessboard."""
    # ... (no changes to this function)


def recursive_solve(board, row, queens, solutions):
    """Recursively solve an N-queens puzzle."""
    # ... (no changes to this function)


def print_solution(solution):
    """Print a solution in the required format."""
    for row, col in solution:
        print(f"[{row}, {col}]", end=" ")
    print()


if __name__ == "__main__":
    # Check if the correct number of arguments is provided
    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        sys.exit(1)

    try:
        N = int(sys.argv[1])
        if N < 4:
            print("N must be at least 4")
            sys.exit(1)
    except ValueError:
        print("N must be a number")
        sys.exit(1)

    # Initialize the chessboard
    board = init_board(N)

    # Solve the N-queens puzzle recursively
    solutions = recursive_solve(board, 0, 0, [])

    # Print the solutions
    for solution in solutions:
        print_solution(solution)
