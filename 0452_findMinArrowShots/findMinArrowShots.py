class Solution(object):
    def findMinArrowShots(self, points):
        """
        :type points: List[List[int]]
        :rtype: int
        """

        points.sort(key=lambda x: x[-1])

        arrow_x = 0
        count = 0

        for _, inter in enumerate(points):
            if arrow_x == 0:
                arrow_x = inter[1]
                count += 1
            elif inter[0] <= arrow_x <= inter[1]:
                pass
            elif arrow_x < inter[0]:
                arrow_x = inter[1]
                count += 1

        return count
