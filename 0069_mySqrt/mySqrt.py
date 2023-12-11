class Solution(object):
    def mySqrt(self, x):
        """
        :type x: int
        :rtype: int
        """

        '''
        i = 0

        while i <= x:
            if i ** 2 == x:
                return i
            elif i ** 2 >= x:
                return i - 1

            i += 1
        # 暴力法
        '''

        l, r = 0, x
        ans = 0

        while l <= r:
            mid = (l + r) // 2

            if mid ** 2 <= x:
                ans = mid
                l = mid + 1
            else:
                r = mid - 1

        return ans