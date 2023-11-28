class Solution(object):
    def fourSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[List[int]]
        """

        nums.sort()
        ans = []

        for i in range(len(nums) - 3):
            for j in range(i + 1, len(nums) - 2):
                l, r = j + 1, len(nums) - 1
                while l < r:
                    if nums[i] + nums[j] + nums[l] + nums[r] > target:
                        r -= 1
                    elif nums[i] + nums[j] + nums[l] + nums[r] < target:
                        l += 1
                    else:
                        if [nums[i], nums[j], nums[l], nums[r]] not in ans:
                            ans.append([nums[i], nums[j], nums[l], nums[r]])
                        l = l + 1

        return ans