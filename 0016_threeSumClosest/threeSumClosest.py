class Solution(object):
    def threeSumClosest(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """

        nums.sort()
        i = 0

        best = [100000000, 0]

        for i in range(len(nums) - 2):
            j, k = i + 1, len(nums) - 1
            while j < k:
                sum = nums[i] + nums[j] + nums[k]
                if sum > target:
                    k = k - 1
                else:
                    j = j + 1

                if abs(sum - target) < best[0]:
                    best[0] = abs(sum - target)
                    best[1] = sum

        return best[1]