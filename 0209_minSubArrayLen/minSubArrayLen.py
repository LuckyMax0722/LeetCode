class Solution(object):
    def minSubArrayLen(self, target, nums):
        """
        :type target: int
        :type nums: List[int]
        :rtype: int
        """

        """
        for windows_length in range(1, len(nums) + 1):
            for start in range(len(nums)):
                if sum(nums[start:start + windows_length]) >= target:
                    return windows_length

        return 0
        # 暴力法 超时
        """

        """
        l, r = (0, 0)
        ans = 10000

        while r < len(nums):
            num_sum = sum(nums[l:r+1])

            if num_sum >= target:
                ans = min(ans, r - l + 1)
                l = l + 1

            else:
                r = r + 1

        if ans == 10000:
            return 0
        else:
            return ans

        # 我的滑动窗口，超时？ 
        """

        if not nums:
            return 0

        n = len(nums)
        ans = n + 1
        start, end = 0, 0
        total = 0
        while end < n:
            total += nums[end]
            while total >= target:
                ans = min(ans, end - start + 1)
                total -= nums[start]
                start += 1
            end += 1

        return 0 if ans == n + 1 else ans


