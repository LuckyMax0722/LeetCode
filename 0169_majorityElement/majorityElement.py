from collections import Counter

class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        counts = Counter(nums)
        return max(counts.keys(), key=counts.get)

        # 获得最大键的值的键
        # 另一种解法，排序，众数必定在n/2的位置