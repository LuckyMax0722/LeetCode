class Solution(object):
    def isSubsequence(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        count = 0
        start = 0

        for idx in range(len(s)):
            t = t[start:]
            index = t.find(s[idx])
            if  index >= 0:
                count = count + 1
                start = index + 1

        if count == len(s):
            return True
        else:
            return False
