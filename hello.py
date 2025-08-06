"""
Sudoku Solver

This script attempts to solve a 9x9 Sudoku puzzle using backtracking.
"""

from typing import List


def is_safe(num: int, x: int, y: int, sudoku: List[List[int]]) -> bool:
    """Check whether placing 'num' at position (x, y) is safe."""

    # Check 3x3 subgrid
    corner_x = (x // 3) * 3
    corner_y = (y // 3) * 3
    for i in range(corner_x, corner_x + 3):
        for j in range(corner_y, corner_y + 3):
            if sudoku[i][j] == num:
                return False

    # Check row and column
    for i in range(9):
        if num in (sudoku[i][y], sudoku[x][i]):
            return False

    return True



def solve_sudoku(sudoku: List[List[int]]) -> bool:
    """Attempt to solve the Sudoku puzzle using backtracking."""
    for i in range(9):
        for j in range(9):
            if sudoku[i][j] != 0:
                continue

            for num in range(1, 10):
                if not is_safe(num, i, j, sudoku):
                    continue

                sudoku[i][j] = num
                if solve_sudoku(sudoku):
                    return True
                sudoku[i][j] = 0

            return False
    return True



def print_sudoku(sudoku: List[List[int]]) -> None:
    """Print the Sudoku board."""
    for row in sudoku:
        print(" ".join(str(num) if num != 0 else '.' for num in row))


def main() -> None:
    """Main function to drive the Sudoku solver."""
    sudoku = [
        [5, 3, 0, 0, 7, 0, 0, 0, 0],
        [6, 0, 0, 1, 9, 5, 0, 0, 0],
        [0, 9, 8, 0, 0, 0, 0, 6, 0],
        [8, 0, 0, 0, 6, 0, 0, 0, 3],
        [4, 0, 0, 8, 0, 3, 0, 0, 1],
        [7, 0, 0, 0, 2, 0, 0, 0, 6],
        [0, 6, 0, 0, 0, 0, 2, 8, 0],
        [0, 0, 0, 4, 1, 9, 0, 0, 5],
        [0, 0, 0, 0, 8, 0, 0, 7, 9],
    ]

    print("\nOriginal Sudoku:")
    print_sudoku(sudoku)

    if solve_sudoku(sudoku):
        print("\nSolved Sudoku:")
        print_sudoku(sudoku)
    else:
        print("No solution exists.")


if __name__ == "__main__":
    main()
