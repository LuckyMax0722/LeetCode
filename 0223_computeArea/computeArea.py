class Solution(object):
    def computeArea(self, ax1, ay1, ax2, ay2, bx1, by1, bx2, by2):
        """
        :type ax1: int
        :type ay1: int
        :type ax2: int
        :type ay2: int
        :type bx1: int
        :type by1: int
        :type bx2: int
        :type by2: int
        :rtype: int
        """

        w = min(ax2, bx2) - max(ax1, bx1)
        h = min(ay2, by2) - max(ay1, by1)

        if w < 0 or h < 0:
            over_s = 0
        else:
            over_s = w * h
        a_s = (ax2 - ax1) * (ay2 - ay1)
        b_s = (bx2 - bx1) * (by2 - by1)

        return a_s + b_s - over_s