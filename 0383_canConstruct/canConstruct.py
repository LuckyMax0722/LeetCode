from collections import Counter


class Solution(object):
    def canConstruct(self, ransomNote, magazine):
        """
        :type ransomNote: str
        :type magazine: str
        :rtype: bool
        """

        hash_ransomNote = Counter(ransomNote)
        hash_magazine = Counter(magazine)

        for key in hash_ransomNote:
            if hash_ransomNote[key] > hash_magazine[key]:
                return False

        return True