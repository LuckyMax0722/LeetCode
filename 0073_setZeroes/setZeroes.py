from collections import Counter


class Solution(object):
    def setZeroes(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: None Do not return anything, modify matrix in-place instead.
        """

        """
        zero_col = []

        for i,list in enumerate(zip(*matrix)):
            hash = Counter(list)
            if hash[0]:
                zero_col.append(i)

        for i, list in enumerate(matrix):
            hash = Counter(list)
            if hash[0]:
                matrix[i] =  [0] * len(matrix[i])

        for i in zero_col:
            for row in matrix:
                row[i] = 0

        # 我的笨蛋办法
        """

        m, n = len(matrix), len(matrix[0])
        row, col = [False] * m, [False] * n
        print(row, col)
        for i in range(m):
            for j in range(n):
                if matrix[i][j] == 0:
                    row[i] = col[j] = True

        for i in range(m):
            for j in range(n):
                if row[i] or col[j]:
                    matrix[i][j] = 0

        # 官方就是加了个TF矩阵来标记