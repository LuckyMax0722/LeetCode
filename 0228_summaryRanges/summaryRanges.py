class Solution(object):
    def summaryRanges(self, nums):
        """
        :type nums: List[int]
        :rtype: List[str]
        """

        l, r = 0, 0
        ans = []

        '''
        while r < len(nums) - 1:
            if nums[r] + 1 == nums[r + 1]:
                r = r + 1
            else:
                if l == r:
                    ans.append(str(nums[l]))
                else:
                    ans.append(str(nums[l]) + "->" + str(nums[r]))

                l = r + 1
                r = l
        '''

        while r < len(nums):
            if r != len(nums) - 1 and nums[r] + 1 == nums[r + 1]:
                r = r + 1
            elif r == len(nums) - 1 and nums[r - 1] + 1 == nums[r]:
                ans.append(str(nums[l]) + "->" + str(nums[r]))
                break
            else:
                if l == r:
                    ans.append(str(nums[l]))
                else:
                    ans.append(str(nums[l]) + "->" + str(nums[r]))

                l = r + 1
                r = l

        return ans