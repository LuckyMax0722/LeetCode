class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """

        if len(s) % 2 != 0:
            return False

        temp = []
        hash = {')': '(', ']': '[', '}': '{'}

        for i in range(len(s)):
            if s[i] == '(' or s[i] == '[' or s[i] == '{':
                temp.append(s[i])
            else:
                if temp and temp[-1] == hash[s[i]]:
                    temp = temp[:-1]
                else:
                    return False

        if not temp:
            return True
        else:
            return False


