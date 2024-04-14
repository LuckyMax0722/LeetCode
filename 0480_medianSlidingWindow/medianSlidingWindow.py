from sortedcontainers import SortedList


class Solution(object):
    def medianSlidingWindow(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[float]
        """
        '''
        res = []

        for i in range(len(nums) - k + 1):
            tmp = sorted(nums[i:i+k])

            if k % 2 == 0:
                res.append((tmp[k/2 - 1] + tmp[k/2]) / 2.0)
            else:
                res.append(tmp[k/2])

        return res

        # 超时
        '''

        median = lambda a: (a[(len(a) - 1) // 2] + a[len(a) // 2]) / 2.0
        a = SortedList(nums[:k])
        res = [median(a)]
        for i, j in zip(nums[:-k], nums[k:]):
            a.remove(i)
            a.add(j)
            res.append(median(a))
        return res
