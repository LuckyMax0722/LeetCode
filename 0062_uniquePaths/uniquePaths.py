import numpy as np

class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        board = np.zeros((m, n))

        for i in range(m):
            for j in range(n):
                if i == 0:
                    board[i, j] = 1
                elif j == 0:
                    board[i, j] = 1
                else:
                    board[i, j] = board[i - 1, j] + board[i, j - 1]

        return int(board[m-1, n-1])