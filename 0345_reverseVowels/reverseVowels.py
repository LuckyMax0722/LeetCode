class Solution:
    def reverseVowels(self, s: str) -> str:
        vowel= 'aeiouAEIOU'

        l, r = 0, len(s) - 1
        s_list = list(s)

        while l < r:
            if s_list[l] in vowel and s_list[r] in vowel:
                s_list[l], s_list[r] = s_list[r], s_list[l]
                l += 1
                r -= 1
            elif s_list[l] in vowel and s_list[r] not in vowel:
                r -= 1
            elif s_list[l] not in vowel and s_list[r] in vowel:
                l += 1
            else:
                l += 1
                r -= 1

        return ''.join(s_list)
