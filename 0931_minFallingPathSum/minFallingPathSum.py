import numpy as np


class Solution:
    def minFallingPathSum(self, matrix: List[List[int]]) -> int:
        '''
        m = len(matrix)
        for i in range(1, m):
            for j in range(m):
                if j == 0:
                    matrix[i][j] = min(matrix[i][j]+matrix[i-1][j], matrix[i][j]+matrix[i-1][j+1])
                elif j == m-1:
                    matrix[i][j] = min(matrix[i][j]+matrix[i-1][j], matrix[i][j]+matrix[i-1][j-1])
                else:
                    matrix[i][j] = min(matrix[i][j]+matrix[i-1][j], matrix[i][j]+matrix[i-1][j-1], matrix[i][j]+matrix[i-1][j+1])
        return min(matrix[-1])

        # 太慢
        '''

        n = len(matrix)
        ans = [[0] * n for _ in range(n)]
        ans[0] = matrix[0]

        for i in range(1, n):
            ans[i][0] = min(matrix[i][0] + ans[i - 1][0], matrix[i][0] + ans[i - 1][1])
            for j in range(1, n - 1):
                ans[i][j] = min(matrix[i][j] + ans[i - 1][j], matrix[i][j] + ans[i - 1][j - 1],
                                matrix[i][j] + ans[i - 1][j + 1])
            ans[i][n - 1] = min(matrix[i][n - 1] + ans[i - 1][n - 1], matrix[i][n - 1] + ans[i - 1][n - 2])

        return int(min(ans[n - 1]))
        # 太慢