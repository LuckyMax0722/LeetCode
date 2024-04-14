class Solution(object):
    def firstUniqChar(self, s):
        """
        :type s: str
        :rtype: int
        """
        letter = {}

        for i in range(len(s)):
            if s[i] not in letter:
                letter[s[i]] = 1
            else:
                letter[s[i]] = letter[s[i]] + 1

        for i, char in enumerate(s):
            if letter[char] == 1:
                return i

        return -1