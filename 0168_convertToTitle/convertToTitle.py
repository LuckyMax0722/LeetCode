class Solution(object):
    def convertToTitle(self, columnNumber):
        """
        :type columnNumber: int
        :rtype: str
        """

        res = ""

        while columnNumber:
            res = chr(ord('A') + (columnNumber - 1) % 26) + res
            columnNumber = (columnNumber - 1) // 26
        return res