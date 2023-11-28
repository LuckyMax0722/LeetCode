class Solution(object):
    def searchInsert(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """

        l, r = 0, len(nums)

        if target <= min(nums):
            return 0
        elif target > max(nums):
            return len(nums)
        elif target == max(nums):
            return len(nums) - 1

        while True:
            mid = (l + r) / 2
            if nums[mid] > target:
                if mid - 1 >= 0 and nums[mid - 1] < target:
                    return mid
                else:
                    r = mid
            elif nums[mid] < target:
                if mid + 1 <= len(nums) - 1 and nums[mid + 1] > target:
                    return mid + 1
                else:
                    l = mid
            else:
                return mid




