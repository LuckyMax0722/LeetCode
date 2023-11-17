class Solution(object):
    def rotate(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: None Do not return anything, modify matrix in-place instead.
        """

        """
        matrix = np.array(matrix)
        temp  = matrix[0].copy()
        print(temp)
        matrix[0] = matrix[:, 0][::-1]
        print(matrix)
        matrix[:, 0] = matrix[-1]
        print(matrix)
        matrix[-1] = matrix[:, -1][::-1]
        print(matrix)
        matrix[:, -1] = temp
        matrix = matrix.tolist()

        # sb
        """

        matrix[:] = [row[::-1] for row in zip(*matrix)]
        # 草，太惊艳了
        # zip解压list
        # [：]创建并遍历列

