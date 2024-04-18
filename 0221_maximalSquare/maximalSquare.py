class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        n, m = len(matrix), len(matrix[0])
        dp = [[0] * m for _ in range(n)]

        for i in range(n):
            for j in range(m):
                if i == 0:
                    dp[0][j] = 1 if matrix[0][j] == '1' else 0
                elif j == 0:
                    dp[i][0] = 1 if matrix[i][0] == '1' else 0
                else:
                    if matrix[i][j] == '1':
                        dp[i][j] = min(dp[i-1][j], dp[i][j-1], dp[i-1][j-1]) + 1

        max_value = max(max(row) for row in dp)
        return max_value * max_value