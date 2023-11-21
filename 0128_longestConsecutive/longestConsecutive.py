class Solution(object):
    def longestConsecutive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        nums = set(nums)

        max_len = 0

        for num in nums:
            if num - 1 not in nums:
                current_num = num
                len = 1

                while current_num + 1 in nums:
                    current_num = current_num + 1
                    len = len + 1

                max_len = max(max_len, len)

        return max_len

        # set 竟然是O(n) 可以排序并去掉重复的
        # 遍历这个哈希表