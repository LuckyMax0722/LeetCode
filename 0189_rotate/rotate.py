class Solution(object):
    def rotate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: None Do not return anything, modify nums in-place instead.
        """

        '''
        for _ in range(k):
            tmp = nums[-1]
            nums[1:] = nums[0:-1]
            nums[0] = tmp
        # 超时
        '''

        k = k % len(nums)
        # 遇到n < k 就不行了
        # 取余数

        nums.reverse()
        nums[:k] = nums[:k][::-1]
        nums[k:] = nums[k:][::-1]
        # 分段转换法

        '''
        tmp = nums[-k:]
        nums[k:] = nums[0:-k]
        nums[0:k] = tmp
        # 新列表
        '''

