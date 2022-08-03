"""

ask (c) 2022. All rights reserved.
"""
from itertools import product
from typing import List


class Solution:
    SHAPE = 9
    GRID = 3
    EMPTY = '.'
    DIGITS = set([str(num) for num in range(1, SHAPE + 1)])

    def solveSudoku(self, board: List[List[str]]) -> None:
        self.search(board)

    def is_valid_state(self, board):
        # check if it is a valid solution
        for row in self.get_rows(board):
            if set(row) != self.DIGITS:
                return False

        for col in self.get_cols(board):
            if set(col) != self.DIGITS:
                return False

        for grid in self.get_grids(board):
            if set(grid) != self.DIGITS:
                return False
        return True

    def get_candidates(self, board, row, col):
        # remove digits already used in row col or grid
        used_digits = set()
        used_digits.update(self.get_row(board, row))
        used_digits.update(self.get_col(board, col))
        used_digits.update(self.get_grid_at_row_col(board, row, col))
        used_digits -= set([self.EMPTY])
        candidates = self.DIGITS - used_digits
        return candidates

    def search(self, board):
        if self.is_valid_state(board):
            return True

        for row in range(self.SHAPE):
            for col in range(self.SHAPE):
                if board[row][col] == self.EMPTY:
                    for candidate in self.get_candidates(board, row, col):
                        board[row][col] = candidate
                        if self.search(board):
                            return True
                        board[row][col] = self.EMPTY
                    return False

        return True

    def get_rows(self, board):
        for row in range(self.SHAPE):
            yield board[row]

    def get_cols(self, board):
        for col in range(self.SHAPE):
            yield [board[row][col] for row in range(self.SHAPE)]

    def get_grid_at_row_col(self, board, row, col):
        row = row // self.GRID * self.GRID
        col = col // self.GRID * self.GRID
        return [board[r][c] for r, c in product(range(row, row + self.GRID), range(col, col + self.GRID))]

    def get_grids(self, board):
        for row in range(0, self.SHAPE, self.GRID):
            for col in range(0, self.SHAPE, self.GRID):
                grid = [
                    board[r][c] for r, c in
                    product(range(row, row + self.GRID), range(col, col + self.GRID))
                ]
                yield grid

    def get_row(self, board, row):
        return board[row]

    def get_col(self, board, col):
        return [board[row][col] for row in range(self.SHAPE)]


if __name__ == "__main__":
    input_board = [
        ["5", "3", ".", ".", "7", ".", ".", ".", "."],
        ["6", ".", ".", "1", "9", "5", ".", ".", "."],
        [".", "9", "8", ".", ".", ".", ".", "6", "."],
        ["8", ".", ".", ".", "6", ".", ".", ".", "3"],
        ["4", ".", ".", "8", ".", "3", ".", ".", "1"],
        ["7", ".", ".", ".", "2", ".", ".", ".", "6"],
        [".", "6", ".", ".", ".", ".", "2", "8", "."],
        [".", ".", ".", "4", "1", "9", ".", ".", "5"],
        [".", ".", ".", ".", "8", ".", ".", "7", "9"]
    ]

    sol = Solution()
    sol.solveSudoku(input_board)
    print(input_board)