class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """

        x = str(x)
        print(x[0])
        l, r = 0, len(x) - 1

        while l <= r:
            if x[l] != x[r]:
                return False

            l = l + 1
            r = r - 1
        return True