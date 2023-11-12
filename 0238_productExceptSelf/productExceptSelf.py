class Solution(object):
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """

        left = []
        right = [0 for _ in range(len(nums))]
        answer = []

        for idx in range(len(nums)):
            idx_reserve = len(nums) - idx - 1

            if idx == 0:
                i = 1
                j = 1
            else:
                i = i * nums[idx - 1]
                j = j * nums[idx_reserve + 1]

            left.append(i)
            right[idx_reserve] = j

        for idx in range(len(nums)):
            answer.append(left[idx] * right[idx])

        return answer

        # 左乘积列表 右乘积列表
