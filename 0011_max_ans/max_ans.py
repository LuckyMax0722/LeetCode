class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """

        '''
        l, r = (0, len(height) - 1)
        max_ans = min(height[l], height[r]) * (r - l)

        while l < r:
            if height[l] > height[r]:
                r = r - 1
            else:
                l = l + 1

            ans = min(height[l], height[r]) * (r - l)
            max_ans = max(max_ans, ans)

        return max_ans
        
        '''

        # 第二次写

        l, r = 0, len(height) - 1
        res = 0
        while l < r:
            res = max(res, min(height[l], height[r]) * (r - l))

            if height[l] <= height[r]:
                l += 1
            else:
                r -= 1
        return res

