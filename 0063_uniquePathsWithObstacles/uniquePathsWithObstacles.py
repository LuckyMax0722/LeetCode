import numpy as np

class Solution(object):
    def uniquePathsWithObstacles(self, obstacleGrid):
        """
        :type obstacleGrid: List[List[int]]
        :rtype: int
        """
        row, col = len(obstacleGrid), len(obstacleGrid[0])
        ans = np.zeros((row, col), dtype=int)

        if obstacleGrid[0][0] == 1: return 0

        jump_0_col = False

        for i in range(row):
            for j in range(col):
                if i == 0 and j == 0:
                    ans[i][j] = 1
                elif i == 0:
                    if obstacleGrid[i][j] == 1:
                        break
                    else:
                        ans[i][j] = 1
                elif j == 0 and not jump_0_col:
                    if obstacleGrid[i][j] == 1:
                        jump_0_col = True
                    else:
                        ans[i][j] = 1
                else:
                    if obstacleGrid[i][j] == 0: ans[i][j] = ans[i - 1][j] + ans[i][j - 1]

        return ans[-1][-1]
