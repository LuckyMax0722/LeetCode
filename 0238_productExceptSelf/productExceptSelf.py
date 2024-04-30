class Solution(object):
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """

        '''
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
        '''

        '''
        # 第二次写 左右数组乘积

        res = []

        l = [1] + [0] * (len(nums) - 1)
        r = [0] * (len(nums) - 1) + [1]

        for i in range(1, len(nums)):
            l[i] = l[i - 1] * nums[i - 1]

        for i in range(len(nums) - 2, -1, -1):
            r[i] = r[i + 1] * nums[i + 1]

        for i in range(len(nums)):
            res.append(l[i] * r[i])

        return res
        '''

        n = len(nums)
        res = [0] * n

        res[0] = 1

        for i in range(1, n):
            res[i] = res[i - 1] * nums[i - 1]

        temp = 1
        for i in reversed(range(n)):
            res[i] *= temp
            temp *= nums[i]

        return res
