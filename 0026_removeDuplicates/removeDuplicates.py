class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        idx = 1
        l = nums[0]

        while idx < len(nums):
            if l == nums[idx]:
                del nums[idx]
            else:
                l = nums[idx]
                idx = idx + 1

        # 双指针也可以解
