from collections import Counter


class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """

        hash_1 = Counter(s)
        hash_2 = Counter(t)

        for key in hash_1:
            if hash_1[key] != hash_2[key]:
                return False

        for key in hash_2:
            if hash_1[key] != hash_2[key]:
                return False

        return True