class Solution(object):
    def containsNearbyDuplicate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: bool
        """

        hash = {}

        for idx in range(len(nums)):
            if nums[idx] not in hash:
                hash[nums[idx]] = idx
            else:
                if idx - hash[nums[idx]] <= k:
                    return True
                else:
                    hash[nums[idx]] = idx
        return False