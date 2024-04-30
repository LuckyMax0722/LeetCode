class Solution(object):
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        '''
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
        '''

        # 第二次写

        l, cnt = 0, 1

        while cnt <= len(nums):
            cnt += 1

            if nums[l] == 0:
                nums.pop(l)
                nums.append(0)
            else:
                l += 1
