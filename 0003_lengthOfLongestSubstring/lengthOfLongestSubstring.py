class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """

        r = 0
        ans = []
        max_len = 0

        while r < len(s):
            if s[r] not in ans:
                ans.append(s[r])
                r = r + 1
            else:
                max_len = max(max_len, len(ans))
                while s[r] in ans:
                    ans = ans[1:]
                ans.append(s[r])
                r = r + 1

        max_len = max(max_len, len(ans))

        return max_len