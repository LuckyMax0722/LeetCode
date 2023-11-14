class Solution(object):
    def convert(self, s, numRows):
        """
        :type s: str
        :type numRows: int
        :rtype: str
        """
        if numRows == 1:
            return s

        temp = ['' for _ in range(numRows)]
        ans = ''

        for i in range(len(s)):
            idx = i % (numRows * 2 - 2)
            if idx == 0:
                count = 2
            elif idx >= numRows:
                idx = idx - count
                count = count + 2

            temp[idx] = temp[idx] + s[i]

        for s in temp:
            ans = ans + s

        return ans