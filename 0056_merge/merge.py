class Solution(object):
    def merge(self, intervals):
        """
        :type intervals: List[List[int]]
        :rtype: List[List[int]]
        """
        ans = []
        cur = []

        intervals.sort()

        for idx, inter in enumerate(intervals):
            if not cur:
                cur = inter
            else:
                l, r = inter[0], inter[1]

                if r < cur[0] or l > cur[1]:
                    ans.append(cur)
                    cur = inter
                elif l == cur[0] and r == cur[1]:
                    pass
                elif l <= cur[0]:
                    if cur[0] <= r <= cur[1]:
                        cur[0] = l
                    elif r > cur[1]:
                        cur[0] = l
                        cur[1] = r
                elif cur[0] <= l <= cur[1]:
                    if l <= r <= cur[1]:
                        pass
                    elif r > cur[1]:
                        cur[1] = r
        ans.append(cur)
        return ans
