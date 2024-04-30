class Solution:
    def compress(self, chars: List[str]) -> int:

        n = len(chars)

        l, num = 0, 0

        while num < n:
            num = l
            while num < len(chars) and chars[l] == chars[num]:
                num += 1

            cnt = num - l
            if cnt > 1:
                digits = [char for char in str(cnt)]
                chars[l + 1:num] = digits

                l = l + len(digits)

            l += 1
