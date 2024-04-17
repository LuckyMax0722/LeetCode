class Solution:
    def tribonacci(self, n: int) -> int:
        if n == 0:
            return 0
        elif n == 1 or n == 2:
            return 1
        else:
            res = [0, 1, 1]

            while len(res) < n + 1:
                res.append(sum(res[-3:]))

            return res[-1]
