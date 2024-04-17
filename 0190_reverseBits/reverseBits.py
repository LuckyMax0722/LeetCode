class Solution:
    def reverseBits(self, n: int) -> int:
        tmp_bin = format(n, '032b')
        num = int(tmp_bin[::-1], 2)

        return num
