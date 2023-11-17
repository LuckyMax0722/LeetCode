class Solution(object):
    def spiralOrder(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[int]
        """

        h_start, v_start = (0, 0)
        h_end, v_end = (len(matrix[0]) - 1, len(matrix) - 1)

        ans = []

        while True:
            for idx in range(h_start, h_end + 1):
                ans.append(matrix[v_start][idx])
            v_start = v_start + 1
            if v_start > v_end: break

            for idx in range(v_start, v_end + 1):
                ans.append(matrix[idx][h_end])
            h_end = h_end - 1
            if h_end < h_start: break

            for idx in range(h_end, h_start - 1, -1):
                ans.append(matrix[v_end][idx])
            v_end = v_end - 1
            if v_start > v_end: break

            for idx in range(v_end, v_start - 1, -1):
                ans.append(matrix[idx][h_start])
            h_start = h_start + 1
            if h_end < h_start: break

        return ans


