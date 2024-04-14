class Solution(object):
    def titleToNumber(self, columnTitle):
        """
        :type columnTitle: str
        :rtype: int
        """

        '''
        idx = 0
        output = 0

        while columnTitle:
            num = ord(columnTitle[-1]) - ord('A') + 1
            output = output + num * (26 ** (idx))

            columnTitle = columnTitle[:-1]
            idx = idx + 1

        return output
        '''

        res = 0

        for i in range(len(columnTitle)):
            res = res * 26 + ord(columnTitle[i]) - ord('A') + 1

        return res
