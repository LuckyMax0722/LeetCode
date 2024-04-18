class Solution:
    def fib(self, n: int) -> int:
        dp = [0] * (n + 1)

        if n == 0:
            return 0
        elif n == 1:
            return 1
        else:
            dp[0] = 0
            dp[1] = 1
            i = 2
            while i <= n:
                dp[i] = dp[i - 1] + dp[i - 2]
                i += 1

            return dp[-1]
