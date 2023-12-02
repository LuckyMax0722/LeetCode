class Solution(object):
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """

        for idx in range(len(matrix)):
            if matrix[idx][-1] < target:
                continue
            else:
                if target in matrix[idx]:
                    return True
                else:
                    return False
        return False