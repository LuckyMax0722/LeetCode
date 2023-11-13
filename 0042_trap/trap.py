class Solution(object):
    def trap(self, height):
        """
        :type height: List[int]
        :rtype: int
        """

        """
        max_height = max(height)
        ans = 0

        for i in range(1, max_height + 1):
            begin_count = False
            temp = 0
            for j in range(len(height)):
                if height[j] >= i and begin_count == False: # 计算开始
                    begin_count = True
                    temp = 0
                elif height[j] < i and begin_count == True: # 计算中
                    temp = temp + 1
                elif height[j] >= i and begin_count == True and temp != 0: # 计算结束
                    ans = ans + temp
                    temp = 0

        return ans
        # 行解法，超时
        """

        """
        ans = 0

        for i in range(1, len(height) - 1):
            # 找左边最高
            max_left = max(height[0:i])
            # 找右边最高
            max_right = max(height[i + 1:])

            if height[i] < max_left and height[i] < max_right:
                ans = ans + min(max_left, max_right) - height[i]

        return ans
        # 列解法， 看当前墙，左右两侧的高墙， 超时
        """

        """
        l, r = (0, len(height) - 1)
        left_max, right_max = (height[l], height[r])

        l = l + 1
        r = r - 1

        ans = 0

        while l <= r:
            left_max = max(left_max, height[l])
            right_max = max(right_max, height[r])

            if left_max < right_max:
                ans = ans + left_max - height[l]
                l = l + 1
            else:
                ans = ans + right_max - height[r]
                r = r - 1

        return ans

        # 双指针的做法， 由于水量取决于短板，移动最大里的矮的
        """

        ans = 0
        cur = 0
        st = []

        while cur < len(height):
            while st and height[cur] > height[st[-1]]:
                top = st.pop()
                if len(st) == 0:
                    break
                distance = cur - st[-1] - 1
                gaodu = min(height[cur], height[st[-1]]) - height[top]
                ans += distance * gaodu

            st.append(cur)
            cur = cur + 1

        return ans

        # 单调递增栈， 看不懂




