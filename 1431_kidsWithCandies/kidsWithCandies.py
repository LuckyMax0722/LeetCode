class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        res = [False] * len(candies)
        max_num = max(candies)

        for idx, num in enumerate(candies):
            if num + extraCandies >= max_num:
                res[idx] = True
            else:
                res[idx] = False

        return res