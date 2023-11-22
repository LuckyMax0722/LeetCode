class Solution(object):
    def insert(self, intervals, newInterval):
        """
        :type intervals: List[List[int]]
        :type newInterval: List[int]
        :rtype: List[List[int]]
        """

        ans = []

        if not intervals:
            ans.append(newInterval)
            return ans

        intervals.append(newInterval)
        intervals.sort()

        temp = []

        for i, inter in enumerate(intervals):
            if not temp: temp = inter

            l, r = inter[0], inter[1]
            if l > temp[1]:
                if temp not in ans:
                    ans.append(temp)
                temp = inter
            elif temp[0] <= l <= temp[1]:
                if r > temp[1]:
                    temp[1] = r
                    if temp not in ans:
                        ans.append(temp)

        if temp not in ans:
            ans.append(temp)

        return ans
