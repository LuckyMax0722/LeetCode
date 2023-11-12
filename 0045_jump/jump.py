class Solution(object):
    def jump(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        count = 0
        start = 0
        end = 1

        while end < len(nums):
            maxPos = 0

            for i in range(start, end):  # 和之前那题一样 遍历下一个跳跃范围内最大的跳跃值
                maxPos = max(maxPos, i + nums[i])

            start = end
            end = maxPos + 1
            count = count + 1

        return count