import numpy as np


class Solution(object):
    def generateMatrix(self, n):
        """
        :type n: int
        :rtype: List[List[int]]
        """

        ans = np.zeros((n, n), dtype=int)

        h_start, v_start, h_end, v_end = 0, 0, n - 1, n - 1

        count = 0

        while count <= n * n:
            for col in range(h_start, h_end + 1):
                count += 1
                ans[v_start][col] = count
            v_start += 1
            if v_start > v_end: break

            for row in range(v_start, v_end + 1):
                count += 1
                ans[row][h_end] = count
            h_end -= 1
            if h_start > h_end: break

            for col in range(h_end, h_start - 1, -1):
                count += 1
                ans[v_end][col] = count
            v_end -= 1
            if v_start > v_end: break

            for row in range(v_end, v_start - 1, -1):
                count += 1
                ans[row][h_start] = count
            h_start += 1
            if h_start > h_end: break

        return ans.tolist()


import numpy as np


class Solution(object):
    def generateMatrix(self, n):
        """
        :type n: int
        :rtype: List[List[int]]
        """

        ans = np.zeros((n, n), dtype=int)

        h_start, v_start, h_end, v_end = 0, 0, n - 1, n - 1

        count = 0

        while count <= n * n:
            for col in range(h_start, h_end + 1):
                count += 1
                ans[v_start][col] = count
            v_start += 1
            if v_start > v_end: break

            for row in range(v_start, v_end + 1):
                count += 1
                ans[row][h_end] = count
            h_end -= 1
            if h_start > h_end: break

            for col in range(h_end, h_start - 1, -1):
                count += 1
                ans[v_end][col] = count
            v_end -= 1
            if v_start > v_end: break

            for row in range(v_end, v_start - 1, -1):
                count += 1
                ans[row][h_start] = count
            h_start += 1
            if h_start > h_end: break

        return ans.tolist()
