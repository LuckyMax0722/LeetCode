class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        minus = False
        if x == 0:
            return 0
        elif x < 0:
            minus = True

        x = abs(x)
        x = str(x)
        x = x[::-1]
        x = int(x)

        if minus:
            x = -x

        if -2 ** 31 <= x <= 2 ** 31 - 1:
            return x
        else:
            return 0