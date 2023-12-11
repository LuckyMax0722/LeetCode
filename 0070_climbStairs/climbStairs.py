class Solution(object):
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """

        '''
        self.ans = 0

        def dfs(remain, step):
            if remain == 0:
                self.ans += 1
                return
            elif remain < 0:
                return
            else:
                for i in range(1, 3):
                    dfs(remain - i, i)

        remain = n
        step = 0

        dfs(remain, step)
        return self.ans
        # dfs超时
        '''

        # 斐波那契数列
        i = 1

        two_step_before = 1
        one_step_before = 2
        cur = 0

        while i <= n:
            if i == 1:
                cur = two_step_before
            elif i == 2:
                cur = one_step_before
            else:
                cur = one_step_before + two_step_before
                two_step_before = one_step_before
                one_step_before = cur

            i += 1

        return cur
