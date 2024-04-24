class Solution:
    def toLowerCase(self, s: str) -> str:
        res = ''
        for idx, letter in enumerate(s):
            if 65 <= ord(letter) <= 90:
                res += chr(ord(letter) + 32)
            else:
                res += s[idx]

        return res