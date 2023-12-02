class Solution(object):
    def sortColors(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """

        n = len(nums)
        i = 1

        while i <= n:
            j = 0
            while j <= n - i - 1:
                if nums[j] >= nums[j + 1]:
                    nums[j], nums[j + 1] = nums[j + 1], nums[j]
                j += 1
            i += 1

