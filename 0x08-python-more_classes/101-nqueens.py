#!/usr/bin/python3
"""Solves the N-queens puzzle.

This program determines all possible solutions to placing N
non-attacking queens on an NxN chessboard.

Example:
    $ ./nqueens_solver.py N

N must be an integer greater than or equal to 4.

Attributes:
    chessboard (list): A list of lists representing the chessboard.
    solutions (list): A list of solutions, each represented as a list of queen
    positions.

Solutions are represented in the format [[r, c], [r, c], [r, c], [r, c]]
where `r` and `c` represent the row and column, respectively, where a
queen must be placed on the chessboard.
"""
import sys


def initialize_chessboard(n):
    """Initialize an `n`x`n` sized chessboard with empty squares."""
    chessboard = [[" " for _ in range(n)] for _ in range(n)]
    return chessboard


def copy_chessboard(chessboard):
    """Return a deep copy of a chessboard."""
    if isinstance(chessboard, list):
        return [copy_chessboard(row) for row in chessboard]
    return chessboard


def extract_solution(chessboard):
    """Return the list of lists representation of a solved chessboard."""
    solution = []
    for row in range(len(chessboard)):
        for col in range(len(chessboard)):
            if chessboard[row][col] == "Q":
                solution.append([row, col])
                break
    return solution


def mark_unavailable(chessboard, row, col):
    """Mark unavailable spots on the chessboard where queens cannot be placed.
    """
    # Mark all forward spots
    for c in range(col + 1, len(chessboard)):
        chessboard[row][c] = "x"
    # Mark all backward spots
    for c in range(col - 1, -1, -1):
        chessboard[row][c] = "x"
    # Mark all spots below
    for r in range(row + 1, len(chessboard)):
        chessboard[r][col] = "x"
    # Mark all spots above
    for r in range(row - 1, -1, -1):
        chessboard[r][col] = "x"
    # Mark all spots diagonally down to the right
    c = col + 1
    for r in range(row + 1, len(chessboard)):
        if c >= len(chessboard):
            break
        chessboard[r][c] = "x"
        c += 1
    # Mark all spots diagonally up to the left
    c = col - 1
    for r in range(row - 1, -1, -1):
        if c < 0:
            break
        chessboard[r][c]
        c -= 1
    # Mark all spots diagonally up to the right
    c = col + 1
    for r in range(row - 1, -1, -1):
        if c >= len(chessboard):
            break
        chessboard[r][c] = "x"
        c += 1
    # Mark all spots diagonally down to the left
    c = col - 1
    for r in range(row + 1, len(chessboard)):
        if c < 0:
            break
        chessboard[r][c] = "x"
        c -= 1


def solve_nqueens(chessboard, row, queens, solutions):
    """Recursively solve the N-queens puzzle.

    Args:
        chessboard (list): The current working chessboard.
        row (int): The current working row.
        queens (int): The current number of placed queens.
        solutions (list): A list of solutions.
    Returns:
        solutions
    """
    if queens == len(chessboard):
        solutions.append(extract_solution(chessboard))
        return solutions

    for col in range(len(chessboard)):
        if chessboard[row][col] == " ":
            temp_board = copy_chessboard(chessboard)
            temp_board[row][col] = "Q"
            mark_unavailable(temp_board, row, col)
            solutions = solve_nqueens(temp_board, row + 1, queens + 1,
                                      solutions)

    return solutions


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: nqueens_solver.py N")
        sys.exit(1)

    try:
        N = int(sys.argv[1])
        if N < 4:
            print("N must be at least 4")
            sys.exit(1)
    except ValueError:
        print("N must be a number")
        sys.exit(1)

    chessboard = initialize_chessboard(N)
    solutions = solve_nqueens(chessboard, 0, 0, [])
    for solution in solutions:
        print(solution)
