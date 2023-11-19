class Solution(object):
    def wordPattern(self, pattern, s):
        """
        :type pattern: str
        :type s: str
        :rtype: bool
        """
        s = s.split()

        if len(pattern) != len(s):
            return False

        hash_table_pattern = {}
        hash_table_s = {}

        for idx in range(len(pattern)):
            if pattern[idx] not in hash_table_pattern:
                hash_table_pattern[pattern[idx]] = s[idx]
            else:
                if hash_table_pattern[pattern[idx]] != s[idx]:
                    return False

            if s[idx] not in hash_table_s:
                hash_table_s[s[idx]] = pattern[idx]
            else:
                if hash_table_s[s[idx]] != pattern[idx]:
                    return False

        return True
