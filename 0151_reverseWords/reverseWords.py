class Solution(object):
    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """

        """
        if not s:
            return ''

        s = s.strip()

        s = s[::-1]
        temp = ''
        ans = ''
        for i in range(len(s)):
            if s[i] != ' ':
                temp = temp + s[i]
            else:
                temp = temp[::-1]
                if temp:
                    ans = ans + temp + ' '
                temp = ''

        ans = ans + temp[::-1]

        return ans
        # 笨办法
        """

        if not s:
            return ''

        s = s.strip()

        s = s[::-1]

        strs = s.split()  # 直接用.split()

        ans = ''

        for i in range(len(strs)):
            strs[i] = strs[i][::-1]
            ans = ans + strs[i] + ' '

        return ans.strip()
