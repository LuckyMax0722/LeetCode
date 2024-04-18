class Solution:
    def deleteAndEarn(self, nums: List[int]) -> int:
        max_num = max(nums)

        total = [0] * (max_num + 1)

        for val in nums:
            total[val] += val

        total = [0] + total

        dp = [0] * (max_num + 2)

        for i in range(2, max_num + 2):
            dp[i] = max(dp[i - 2] + total[i], dp[i - 1])

        return max(dp)