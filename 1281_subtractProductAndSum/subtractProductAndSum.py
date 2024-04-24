class Solution:
    def subtractProductAndSum(self, n: int) -> int:
        temp = []
        res = 0

        while n:
            temp.append(n % 10)
            n = (n - n % 10) // 10
        return prod(temp) - sum(temp)