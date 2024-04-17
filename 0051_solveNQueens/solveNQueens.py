import numpy as np


class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        self.n = n

        board = [['.'] * n for _ in range(n)]
        res = []

        def backtrack(row):
            if row == n:
                tmp = [''.join(i) for i in board]
                res.append(tmp)
                return

            for col in range(n):
                if not self.isValid(board, row, col):
                    continue
                board[row][col] = 'Q'
                backtrack(row + 1)
                board[row][col] = '.'

        backtrack(0)
        return res

    def isValid(self, board, row, col):

        # 检查上方
        for i in range(row):
            if board[i][col] == 'Q':
                return False

        # 检查左上方
        for i, j in zip(range(row - 1, -1, -1), range(col - 1, -1, -1)):
            if board[i][j] == 'Q':
                return False

        # 检查右上方
        for i, j in zip(range(row - 1, -1, -1), range(col + 1, self.n, 1)):
            if board[i][j] == 'Q':
                return False

        return True