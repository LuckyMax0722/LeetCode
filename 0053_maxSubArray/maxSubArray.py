class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        '''
        n = len(nums)

        if n == 1:
            return nums[0]

        l,r = 0, 1
        ans = -1000000

        for l in range(n):
            for r in range(l, n):
                ans = max(ans, sum(nums[l:r + 1]))

        return ans
        # 超时
        '''

        pre = 0
        max_ans = nums[0]

        for x in nums:
            pre = max(pre + x, x)  # 当前数x和先前数pre的和是否能超过当前数x，不能就从当前数x开始
            max_ans = max(max_ans, pre)

        return max_ans
