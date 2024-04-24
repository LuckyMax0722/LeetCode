class Solution:
    def xorOperation(self, n: int, start: int) -> int:
        res = 0

        for i in range(start, start + n * 2, 2):
            res = res ^ i

        return res