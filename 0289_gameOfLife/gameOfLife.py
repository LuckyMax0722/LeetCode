import numpy as np
from collections import Counter


class Solution(object):
    def gameOfLife(self, board):
        """
        :type board: List[List[int]]
        :rtype: None Do not return anything, modify board in-place instead.
        """

        row, col = (len(board), len(board[0]))
        board_array = np.array(board)
        board_array = np.pad(board_array, ((1, 1), (1, 1)), 'constant', constant_values=2)

        live = []
        die = []

        for i in range(1, row + 1):
            for j in range(1, col + 1):
                temp = board_array[i - 1: i + 2, j - 1: j + 2].flatten()
                hash = Counter(temp)

                if board_array[i, j] == 1:
                    if hash[1] == 3 or hash[1] == 4:
                        live.append([i - 1, j - 1])
                    else:
                        die.append([i - 1, j - 1])
                elif board_array[i, j] == 0:
                    if hash[1] == 3:
                        live.append([i - 1, j - 1])

        for i in live:
            board[i[0]][i[1]] = 1
        for i in die:
            board[i[0]][i[1]] = 0

        # 笨蛋补全
