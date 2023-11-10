class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        if len(nums) <= 2:
            return len(nums)

        l, r = (2, 2)

        while r < len(nums):
            if nums[l - 2] != nums[r]:
                nums[l] = nums[r]
                l = l + 1
            r = r + 1

        return l

        # 快慢指针 好聪明啊
        # l-2



