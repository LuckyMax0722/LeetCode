class Solution(object):
    def lengthOfLastWord(self, s):
        """
        :type s: str
        :rtype: int
        """

        s = s[::-1]
        idx = 0
        ans = ''

        word_begin = False
        word_finish = False

        while True:
            if s[idx] != ' ':
                word_begin = True

            if word_begin:
                ans = ans + s[idx]

            if idx == len(s) - 1 or s[idx + 1] == ' ' and len(ans) != 0:
                break

            idx = idx + 1

        return len(ans)