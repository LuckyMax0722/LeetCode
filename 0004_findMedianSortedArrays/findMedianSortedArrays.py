class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """

        nums = []

        while True:
            if nums1 and nums2:
                if nums1[0] <= nums2[0]:
                    nums.append(nums1[0])
                    nums1.pop(0)
                else:
                    nums.append(nums2[0])
                    nums2.pop(0)
            elif not nums1 and nums2:
                nums = nums + nums2
                break
            elif nums1 and not nums2:
                nums = nums + nums1
                break

        if len(nums) % 2 == 0:
            return (nums[len(nums) / 2] + nums[len(nums) / 2 - 1]) / 2.0
        else:
            return nums[len(nums) / 2]


