class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        '''
        dp = [1] * len(nums)

        for i in range(1, len(nums)):
            tmp_list = []
            for j in range(0, i):
                if nums[j] >= nums[i]:
                    tmp_list.append(0)
                    continue
                else:
                    tmp_list.append(dp[j])
                    dp[i] = max(tmp_list) + 1

        return max(dp)
        '''

        dp = [1] * len(nums)

        for i in range(len(nums)):
            for j in range(i):
                if nums[j] < nums[i]:
                    dp[i] = max(dp[i], dp[j] + 1)

        return max(dp)