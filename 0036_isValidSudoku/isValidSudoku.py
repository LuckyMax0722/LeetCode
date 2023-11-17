from collections import Counter
import numpy as np


class Solution(object):
    def isValidSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: bool
        """
        board = np.array(board)

        for idx in range(9):
            hash = Counter(board[idx])
            del hash['.']
            for key in hash:
                if hash[key] > 1: return False

        for idx in range(9):
            hash = Counter(board.T[idx])
            del hash['.']
            for key in hash:
                if hash[key] > 1: return False

        for i in range(0, 9, 3):
            for j in range(0, 9, 3):
                temp = np.array(board[i:i + 3, j:j + 3]).flatten()
                hash = Counter(temp)
                del hash['.']
                for key in hash:
                    if hash[key] > 1: return False

        return True
