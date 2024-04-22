class Solution:
    def sumSubarrayMins(self, arr: List[int]) -> int:
        '''
        res = 0

        for i in range(len(arr)):
            for j in range(i + 1, len(arr) + 1):
                res += min(arr[i:j])

        return res

        # 超时
        '''

        arr.append(-1)
        ans, st = 0, [-1]  # 哨兵
        for r, x in enumerate(arr):
            while len(st) > 1 and arr[st[-1]] >= x:
                i = st.pop()
                ans += arr[i] * (i - st[-1]) * (r - i)  # 累加贡献
            st.append(r)
        return ans % (10 ** 9 + 7)
