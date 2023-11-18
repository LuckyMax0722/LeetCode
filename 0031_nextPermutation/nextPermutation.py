class Solution(object):
    def nextPermutation(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """

        n = len(nums)
        if n > 1:
            i, j, k = n - 2, n - 1, n - 1

            while i >= 0 and nums[i] >= nums[j]:
                i -= 1
                j -= 1

            # 如果存在升序就会跳出，不然i=-1

            while k > j and nums[k] <= nums[i]:
                k -= 1

            if i != -1:
                nums[i], nums[k] = nums[k], nums[i]
                nums[:] = nums[:j] + nums[j:][::-1]  # 处理j后面的，必须是升序

            else:
                nums[:] = nums[::-1]
