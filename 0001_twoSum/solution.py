class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """

        # 哈希表
        hasttable = dict()

        for i, num in enumerate(nums):
            if target - num in hasttable:  # 检查之前是否已经出现过另一个数字
                return [i, hasttable[target - num]]
            hasttable[num] = i  # 把数字和索引成对存在哈希表里
