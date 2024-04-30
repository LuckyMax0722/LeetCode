class Solution(object):
    def isSubsequence(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """

        '''
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
        '''

        # 第二次写

        l, r = 0, 0
        n1, n2 = len(s), len(t)
        while l < n1 and r < n2:
            if s[l] == t[r]:
                l += 1
            r += 1

        if l == n1:
            return True
        else:
            return False
