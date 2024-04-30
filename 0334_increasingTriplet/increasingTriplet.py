class Solution:
    def increasingTriplet(self, nums: List[int]) -> bool:
        '''
        for i in range(1, len(nums) - 1):
            if min(nums[:i]) < nums[i] and nums[i] < max(nums[i+1:]):
                return True

        return False

        # 超时
        '''

        one = two = float('inf')

        for three in nums:
            if three > two:
                return True
            elif three <= one:
                one = three
            else:
                two = three

        return False
        # 天才
