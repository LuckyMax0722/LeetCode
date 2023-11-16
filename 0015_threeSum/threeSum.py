class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        nums.sort()
        ans = []

        for i in range(len(nums) - 2):
            j, k = (i + 1, len(nums) - 1)
            goal = 0 - nums[i]

            while j < k:
                sum = nums[j] + nums[k]
                if sum > goal:
                    k = k - 1
                elif sum < goal:
                    j = j + 1
                else:
                    if [nums[i], nums[j], nums[k]] not in ans:
                        ans.append([nums[i], nums[j], nums[k]])
                    k = k - 1
                    j = j + 1

        return ans
