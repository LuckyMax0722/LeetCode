class Solution:
    def vowelStrings(self, words: List[str], left: int, right: int) -> int:
        ans = 0
        table = "aeiou"

        for i in range(left, right + 1):
            if words[i][0] in table and words[i][-1] in table:
                ans += 1

        return ans