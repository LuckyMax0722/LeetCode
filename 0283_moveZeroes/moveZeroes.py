class Solution(object):
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        count = 0
        i = 0

        while count < n:
            if nums[i] == 0:
                nums.pop(i)
                nums.append(0)
            else:
                i += 1

            count += 1
