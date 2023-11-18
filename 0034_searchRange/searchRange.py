class Solution(object):
    def searchRange(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """

        if not nums:
            return [-1, -1]

        l, r = 0, len(nums) - 1
        find = False

        while l <= r:
            mid = (l + r) // 2

            if nums[mid] == target:
                find = True
                break

            if nums[0] <= target < nums[mid]:
                r = r - 1
            else:
                l = l + 1

        if find:
            l, r = mid, mid
            break_1 = False
            break_2 = False

            print(l, r)

            while True:
                if l - 1 >= 0 and nums[l - 1] == target:
                    l = l - 1
                else:
                    break_1 = True

                if r + 1 <= len(nums) - 1 and nums[r + 1] == target:
                    r = r + 1
                else:
                    break_2 = True

                if break_1 and break_2:
                    break

            return [l, r]
        else:
            return [-1, -1]

        # 笨蛋二分法
