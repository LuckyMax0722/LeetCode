class Solution(object):
    def hIndex(self, citations):
        """
        :type citations: List[int]
        :rtype: int
        """

        max_h = max(citations)
        possible_h = 0

        for h in range(max_h + 1):
            paper = sum(1 for value in citations if value >= h)

            if paper >= h:
                possible_h = h

        return possible_h
