class Solution(object):
    def canJump(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """

        k = 0

        for i in range(len(nums)):
            if i > k:
                return False
            k = max(k, i + nums[i])

        return True

        # k = 最远能够到达的距离
        # 每个i都会遍历一次最远能够到达的距离

