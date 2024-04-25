class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        ans = ''

        while word1 or word2:
            if word1:
                ans += word1[0]
                word1 = word1[1:]
            if word2:
                ans += word2[0]
                word2 = word2[1:]

        return ans