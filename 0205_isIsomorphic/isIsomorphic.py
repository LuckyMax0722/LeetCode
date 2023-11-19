class Solution(object):
    def isIsomorphic(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        hast_table = {}
        hast_table_t = {}

        for idx in range(len(s)):
            if s[idx] not in hast_table:
                hast_table[s[idx]] = t[idx]
            else:
                if t[idx] != hast_table[s[idx]]:
                    return False

            if t[idx] not in hast_table_t:
                hast_table_t[t[idx]] = s[idx]
            else:
                if s[idx] != hast_table_t[t[idx]]:
                    return False

        return True
