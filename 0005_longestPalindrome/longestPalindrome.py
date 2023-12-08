class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """

        '''
        n = len(s)
        ans = ""

        for i in range(n):
            for j in range(n, i, -1):
                if s[i:j] == s[i:j][::-1]:
                    if len(s[i:j]) > len(ans):
                        ans = s[i:j] 

        return ans
        #超时
        '''

        lens = len(s)
        for l in range(lens, 0, -1):
            for i in range(lens - l + 1):
                if s[i : i + l] == s[i : i + l][::-1]:
                    return s[i : i + l]


