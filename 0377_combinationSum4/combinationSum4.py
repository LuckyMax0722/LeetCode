class Solution:
    def combinationSum4(self, nums: List[int], target: int) -> int:
        dp = [0] * (target + 1)
        tmp = []

        for num in nums:
            if num <= target:
                tmp.append(num)
                dp[num] = 1

        tmp.sort()

        for i in range(len(dp)):
            cur = 0
            for j in tmp:
                if i >= j:
                    cur += dp[i - j]
                else:
                    break
            dp[i] += cur

        return dp[-1]